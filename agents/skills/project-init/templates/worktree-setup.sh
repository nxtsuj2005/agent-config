#!/usr/bin/env bash
# Runs in a fresh T3 worktree: copy untracked local config from the main checkout, install deps.
set -euo pipefail
main=$(git worktree list --porcelain | awk '/^worktree /{print $2; exit}')
here=$(git rev-parse --show-toplevel)

if [ "$main" != "$here" ]; then
  # gitignored files worth copying (adjust per project)
  for f in .env .env.local .env.development; do
    [ -f "$main/$f" ] && [ ! -e "$here/$f" ] && cp "$main/$f" "$here/$f" && echo "copied $f"
  done
fi

[ -f uv.lock ] && uv sync
[ -f package-lock.json ] && npm ci --prefer-offline --no-audit --no-fund
[ -f go.mod ] && go mod download
exit 0
