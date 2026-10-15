#!/usr/bin/env bash
# Symlinks this repo's agent config into ~/.claude, ~/.codex and ~/.agents.
# Existing files are moved to <name>.bak-<timestamp>. Safe to re-run.
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TS="$(date +%Y%m%d-%H%M%S)"

link() { # link <src> <dst>
  local src="$1" dst="$2"
  mkdir -p "$(dirname "$dst")"
  if [ -L "$dst" ] && [ "$(readlink "$dst")" = "$src" ]; then return; fi
  if [ -e "$dst" ] || [ -L "$dst" ]; then
    mv "$dst" "$dst.bak-$TS"
    echo "backup: $dst -> $dst.bak-$TS"
  fi
  ln -s "$src" "$dst"
  echo "link:   $dst -> $src"
}

# Global rules: one file for Claude and Codex
link "$REPO/agents/AGENTS.md" "$HOME/.agents/AGENTS.md"
link "$HOME/.agents/AGENTS.md" "$HOME/.claude/CLAUDE.md"
link "$HOME/.agents/AGENTS.md" "$HOME/.codex/AGENTS.md"

# Skills (shared by Claude and Codex)
for d in "$REPO"/agents/skills/*/; do
  n="$(basename "$d")"
  link "$REPO/agents/skills/$n" "$HOME/.agents/skills/$n"
  link "$HOME/.agents/skills/$n" "$HOME/.claude/skills/$n"
  link "$HOME/.agents/skills/$n" "$HOME/.codex/skills/$n"
done

# Claude hooks, subagents, settings
for f in "$REPO"/claude/hooks/*; do link "$f" "$HOME/.claude/hooks/$(basename "$f")"; done
for f in "$REPO"/claude/agents/*; do link "$f" "$HOME/.claude/agents/$(basename "$f")"; done
link "$REPO/claude/settings.json" "$HOME/.claude/settings.json"

# Codex guard rules
link "$REPO/codex/rules/guard.rules" "$HOME/.codex/rules/guard.rules"

echo "done. Restart the Claude/Codex session (or run /hooks) to apply."
