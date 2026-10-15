# agent-config

Private. Global rules, skills, hooks and settings for Claude Code and Codex.

## Install / update

```bash
git clone https://github.com/nxtsuj2005/agent-config.git ~/agent-config
~/agent-config/install.sh
```

Update later: `git -C ~/agent-config pull`. Everything is symlinked, so no re-run is needed unless files were added.

## Layout

| Path | Target |
|---|---|
| `agents/AGENTS.md` | `~/.agents/AGENTS.md` (+ `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`) |
| `agents/skills/*` | `~/.agents/skills`, `~/.claude/skills`, `~/.codex/skills` |
| `claude/hooks/*` | `~/.claude/hooks` (guard, outbound_guard, context_watch, format, secret_paste, notify) |
| `claude/agents/*` | `~/.claude/agents` (explorer, reviewer) |
| `claude/settings.json` | `~/.claude/settings.json` |
| `codex/rules/guard.rules` | `~/.codex/rules/guard.rules` |

## Not in here (by design)

Tokens, SSH keys, `~/.proxmox_*`, `~/.fritz_creds`, `~/.poker_gh_token`, Codex `config.toml` and `auth.json`. `AGENTS.md` only references these paths.

## On servers

The `Homelab` block in `agents/AGENTS.md` points to files that only exist on the main machine. Remove or adapt it on other hosts.
