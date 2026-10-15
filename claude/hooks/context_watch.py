#!/usr/bin/env python3
"""UserPromptSubmit + PostToolUse: watches the main thread's context size (from the transcript)
and nudges the agent to suggest a safe compact point before quality drops / auto-compact loses stuff.
Fires once per 50k bucket above the hint threshold. Never blocks."""
import json
import os
import sys

HINT = int(os.environ.get("T3SETUP_CTX_HINT", "120000"))
WARN = int(os.environ.get("T3SETUP_CTX_WARN", "160000"))
BUCKET = 50000


def last_context_tokens(path: str) -> int | None:
    try:
        with open(path, "rb") as f:
            f.seek(0, 2)
            f.seek(max(0, f.tell() - 512 * 1024))
            lines = f.read().decode("utf-8", "ignore").splitlines()
    except OSError:
        return None
    for line in reversed(lines):
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get("isSidechain") or e.get("type") != "assistant":
            continue
        u = (e.get("message") or {}).get("usage") or {}
        if u:
            return (u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0)
                    + u.get("cache_creation_input_tokens", 0))
    return None


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    if data.get("agent_id"):  # subagent context: not our business
        return
    n = last_context_tokens(data.get("transcript_path", ""))
    if not n or n < HINT:
        return
    bucket = n // BUCKET
    state = f"/tmp/t3setup-ctx-{os.getuid()}-{data.get('session_id', 'x')}"
    try:
        prev = int(open(state).read())
    except Exception:
        prev = -1
    if bucket <= prev:
        return
    open(state, "w").write(str(bucket))

    k = n // 1000
    if n >= WARN:
        msg = (f"[context-watcher] Kontext ~{k}k Tokens – teuer und Qualität sinkt. Keine neue große Teilaufgabe mehr anfangen. "
               "Aktuellen Schritt abschließen, committen, `handoff` nach .handoff/ schreiben, dann dem User in 1 Zeile: "
               "\"yo, jetzt compacten (oder neuer Thread mit Handoff) – nix geht verloren\".")
    else:
        msg = (f"[context-watcher] Kontext ~{k}k Tokens. Am nächsten sicheren Punkt (Teilaufgabe fertig + committet, "
               "keine laufenden Subagents/Jobs, Entscheidungen notiert) dem User in 1 Zeile sagen: \"guter Moment zum Compacten\". "
               "Nicht mitten in einer Änderung.")
    event = data.get("hook_event_name", "UserPromptSubmit")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": event, "additionalContext": msg}}))


if __name__ == "__main__":
    main()
    sys.exit(0)
