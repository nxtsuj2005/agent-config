#!/usr/bin/env python3
"""PreToolUse guard: hard-deny catastrophic commands, ask before risky ones or secret access.

Works in bypassPermissions mode too (hooks run before the permission check).
"""
import json
import os
import re
import sys

SECRET_NAME = re.compile(
    r"(^|/)("
    r"\.env(\.(?!example$|sample$|template$|dist$)[\w.-]+)?"
    r"|[\w.-]+\.(pem|key|p12|pfx)"
    r"|id_(rsa|ed25519|ecdsa)(?!\.pub)"
    r"|key\.txt|\.netrc|\.credentials\.json|credentials\.json|clerk-tokens\.json"
    r")$"
)
SECRET_IN_CMD = re.compile(
    r"(?<![\w.-])("
    r"\.env(\.(?!example\b|sample\b|template\b|dist\b)[\w-]+)?"
    r"|[\w.-]+\.(pem|key|p12|pfx)|id_(rsa|ed25519|ecdsa)(?!\.pub)|key\.txt|\.credentials\.json"
    r")(?![\w.-])"
)
READ_VERBS = re.compile(r"\b(cat|less|more|head|tail|grep|rg|awk|sed|bat|xxd|strings|base64|nl|od|jq|yq)\b")

DENY_CMD = [
    (r"\brm\s+(-\w*\s+)*-\w*[rR]\w*\s+(-\w+\s+)*(/|/\*|~|~/|~/\*|\$HOME/?\*?|\.\.?/?|\*)(\s|$|;|&|\|)", "rm -rf auf / ~ . .. oder *"),
    (r"\brm\s+(-\w*\s+)*-\w*f\w*\s+(-\w+\s+)*-\w*[rR]\w*\s+(/|~|\$HOME|\.\.?)(\s|$)", "rm -rf auf / ~ . oder .."),
    (r"\bmkfs(\.\w+)?\b", "mkfs"),
    (r"\bdd\b.*\bof=/dev/(sd|nvme|vd|hd|mmcblk)", "dd auf ein Block-Device"),
    (r">\s*/dev/(sd|nvme|vd|hd|mmcblk)", "Write auf ein Block-Device"),
    (r"\b(pkill\s+(-\w+\s+)*-f|killall)\b", "pkill -f/killall killt oft die eigene Shell (Exit 144). Nimm `kill $(lsof -ti :PORT)` oder ein Pidfile"),
    (r"\bgit\s+push\b(?=.*(\s--force(?!-with-lease)\b|\s-f\b|\s\+))(?=.*\b(main|master)\b)", "Force-Push auf main/master"),
]
ASK_CMD = [
    (r"\bgit\s+push\b.*(\s--force|\s-f\b|\s\+\w)", "Force-Push"),
    (r"\bgit\s+reset\s+--hard\b", "git reset --hard verwirft Änderungen"),
    (r"\bgit\s+clean\s+-\w*f", "git clean löscht untracked Files"),
    (r"\b(drop\s+(table|database|schema)|truncate\s+table)\b", "DROP/TRUNCATE"),
    (r"\bdocker(\s+compose|-compose)\b.*\bdown\b.*\s-v\b", "compose down -v löscht Volumes"),
    (r"\bdocker\s+(volume\s+(rm|prune)|system\s+prune)\b", "Docker Volumes/Prune"),
    (r"\b(reboot|shutdown|poweroff)\b", "Reboot/Shutdown"),
    (r"\b(pct|qm)\s+(destroy|stop|rollback)\b", "Proxmox destroy/stop/rollback"),
]


def out(decision: str, reason: str) -> None:
    print(json.dumps({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": decision,
        "permissionDecisionReason": f"[t3setup guard] {reason}",
    }}))
    sys.exit(0)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    tool = data.get("tool_name", "")
    inp = data.get("tool_input") or {}

    if tool == "Bash":
        cmd = inp.get("command", "")
        for pat, why in DENY_CMD:
            if re.search(pat, cmd, re.I):
                out("deny", f"Geblockt: {why}. Wenn das wirklich gewollt ist, führ es selbst aus.")
        for pat, why in ASK_CMD:
            if re.search(pat, cmd, re.I):
                out("ask", why)
        if SECRET_IN_CMD.search(cmd) and READ_VERBS.search(cmd):
            out("ask", "Command liest evtl. Secrets (.env/Key-Datei)")
        sys.exit(0)

    path = inp.get("file_path") or inp.get("notebook_path") or inp.get("path") or ""
    if tool in {"Read", "Edit", "Write", "MultiEdit", "NotebookEdit", "Grep"} and path:
        if SECRET_NAME.search(os.path.normpath(path)):
            out("ask", f"Zugriff auf Secret-Datei: {os.path.basename(path)}")
    sys.exit(0)


if __name__ == "__main__":
    main()
