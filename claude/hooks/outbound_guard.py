#!/usr/bin/env python3
"""PreToolUse guard: nothing leaves the machine or gets committed without the user's OK.

Asks (never silently blocks) before git push/commit/remote changes and outward-facing
gh writes. Matches on the raw command string, so compositions (&&, ;, |, $(), bash -c "...")
are covered too. Runs before the permission check, so it also works in bypass modes.
Deliberately over-matches: a false "ask" costs one keypress, a missed push can break a
shared branch.
"""
import datetime
import json
import os
import re
import sys

# Statement-local match: [^\n;&|] keeps `git log | grep push` from matching.
GIT = r"\bgit\b[^\n;&|]*?\b"
GH = r"\bgh\s+"

RULES = [
    (GIT + r"push\b", "git push (alle Varianten): geht aufs Remote"),
    (GIT + r"remote\s+(add|set-url|set-head|rename|remove|rm)\b", "git remote ändern"),
    (GIT + r"send-pack\b", "git send-pack: geht aufs Remote"),
    (GH + r"pr\s+(create|merge|close|reopen|edit|comment|review|ready)\b", "gh pr: schreibt auf GitHub"),
    (GH + r"issue\s+(create|close|reopen|edit|comment|delete|transfer)\b", "gh issue: schreibt auf GitHub"),
    (GH + r"release\s+(create|edit|delete|upload)\b", "gh release: schreibt auf GitHub"),
    (GH + r"repo\s+(create|delete|sync|fork|edit|rename|archive)\b", "gh repo: ändert GitHub-Repo"),
    (GH + r"(workflow\s+run|gist\s+(create|edit|delete)|secret\s+(set|delete)|variable\s+(set|delete))\b", "gh: schreibt auf GitHub"),
]
# gh api writes: explicit non-GET method, or any body flag (which makes gh switch to POST).
GH_API = re.compile(r"\bgh\s+api\b[^\n;&|]*")
GH_API_WRITE = re.compile(
    r"(-X|--method)[\s=]+['\"]?(POST|PUT|PATCH|DELETE)\b|(\s-f\b|\s-F\b|--field\b|--raw-field\b|--input\b)",
    re.I,
)


def ask(reason: str) -> None:
    # Audit trail: only the matched rule, never the command (it may contain tokens).
    try:
        with open(os.path.expanduser("~/.claude/hooks/outbound_guard.log"), "a") as fh:
            fh.write(f"{datetime.datetime.now().isoformat(timespec='seconds')} ask: {reason}\n")
    except OSError as exc:
        print(f"outbound_guard: log write failed: {exc}", file=sys.stderr)
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "ask",
        "permissionDecisionReason": f"[outbound guard] {reason}. Nichts geht ohne dein OK raus.",
    }}))
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception as exc:
        # Never fail silently: surface it, but do not block the tool.
        print(f"outbound_guard: unreadable hook input: {exc}", file=sys.stderr)
        sys.exit(0)
    if data.get("tool_name") != "Bash":
        sys.exit(0)
    cmd = (data.get("tool_input") or {}).get("command", "")
    cmd = cmd.replace("\\\n", " ")  # join line continuations
    for pat, why in RULES:
        if re.search(pat, cmd):
            ask(why)
    for m in GH_API.finditer(cmd):
        if GH_API_WRITE.search(m.group(0)):
            ask("gh api mit schreibender Methode/Body")
    sys.exit(0)


if __name__ == "__main__":
    main()
