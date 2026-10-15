#!/usr/bin/env python3
"""UserPromptSubmit: if the user pastes a secret into the chat, tell the agent how to handle it.
Never blocks (user would have to retype); only injects instructions. Never prints the secret."""
import json
import re
import sys

PATTERNS = {
    "API-Key (sk-…)": r"\bsk-(ant-)?[A-Za-z0-9_-]{20,}",
    "GitHub-Token": r"\b(ghp|gho|ghs|ghu|ghr)_[A-Za-z0-9]{30,}|\bgithub_pat_[A-Za-z0-9_]{40,}",
    "Slack-Token": r"\bxox[abposr]-[A-Za-z0-9-]{10,}",
    "AWS-Key": r"\bAKIA[0-9A-Z]{16}\b",
    "Private Key (PEM)": r"-----BEGIN [A-Z ]*PRIVATE KEY-----",
    "Telegram-Bot-Token": r"\b\d{8,10}:[A-Za-z0-9_-]{35}\b",
    "Solana-Private-Key": r"\b[1-9A-HJ-NP-Za-km-z]{86,88}\b|\[\s*(\d{1,3}\s*,\s*){63}\d{1,3}\s*\]",
    "Private Key (hex)": r"(?i)priv(ate)?[\s_-]*key\W{0,5}(0x)?[a-f0-9]{64}\b",
    "Credential-Zuweisung": r"(?i)\b(api[_-]?key|secret|token|passw(or)?d|pwd)\b\s*[:=]\s*['\"]?[^\s'\"]{8,}",
}


def main() -> None:
    try:
        prompt = json.load(sys.stdin).get("prompt", "")
    except Exception:
        return
    hits = [name for name, pat in PATTERNS.items() if re.search(pat, prompt)]
    if not hits:
        return
    ctx = (
        f"[t3setup secret-guard] Der Prompt enthält vermutlich Secrets ({', '.join(hits)}). "
        "Regeln: Secret NIE wiederholen/zitieren/loggen, nicht in Code, Commits, Docs oder Tests schreiben. "
        "Nur in die passende gitignorte .env bzw. den Secret-Store eintragen (vorher prüfen, dass sie gitignored ist), im Code per Env-Var lesen. "
        "Am Ende 1 Zeile: der User soll das Secret rotieren, weil es im Chat-Verlauf liegt."
    )
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": ctx}}))


if __name__ == "__main__":
    main()
    sys.exit(0)
