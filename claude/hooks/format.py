#!/usr/bin/env python3
"""PostToolUse formatter: formats the edited file, but only if the project opted in
(ruff config / prettier config + local prettier). Go files always via gofmt. Never fails."""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

PRETTIER_EXT = {".js", ".jsx", ".ts", ".tsx", ".mjs", ".cjs", ".svelte", ".astro", ".vue",
                ".css", ".scss", ".html", ".json", ".md", ".yaml", ".yml"}
PRETTIER_CFG = [".prettierrc", ".prettierrc.json", ".prettierrc.js", ".prettierrc.cjs", ".prettierrc.mjs",
                ".prettierrc.yaml", ".prettierrc.yml", ".prettierrc.toml", "prettier.config.js",
                "prettier.config.cjs", "prettier.config.mjs", "prettier.config.ts"]


def find_up(start: Path, names: list[str]) -> Path | None:
    for d in [start, *start.parents]:
        for n in names:
            if (d / n).exists():
                return d / n
        if (d / ".git").exists():
            break
    return None


def run(cmd: list[str], cwd: Path) -> None:
    try:
        subprocess.run(cmd, cwd=cwd, timeout=20, capture_output=True)
    except Exception:
        pass


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return
    f = (data.get("tool_input") or {}).get("file_path")
    if not f or not os.path.isfile(f):
        return
    p = Path(f).resolve()
    ext = p.suffix.lower()

    if ext in {".py", ".pyi"}:
        cfg = find_up(p.parent, ["ruff.toml", ".ruff.toml", "pyproject.toml"])
        if not cfg or (cfg.name == "pyproject.toml" and "[tool.ruff" not in cfg.read_text(errors="ignore")):
            return
        ruff = shutil.which("ruff")
        cmd = [ruff] if ruff else (["uvx", "ruff"] if shutil.which("uvx") else None)
        if cmd:
            run([*cmd, "format", "--quiet", str(p)], cfg.parent)
    elif ext in PRETTIER_EXT:
        cfg = find_up(p.parent, PRETTIER_CFG)
        if not cfg:
            return
        bin_ = cfg.parent / "node_modules" / ".bin" / "prettier"
        if bin_.exists():
            run([str(bin_), "--write", "--log-level", "silent", str(p)], cfg.parent)
    elif ext == ".go":
        gofmt = shutil.which("gofmt") or os.path.expanduser("~/.local/go/bin/gofmt")
        if os.path.exists(gofmt):
            run([gofmt, "-w", str(p)], p.parent)


if __name__ == "__main__":
    main()
    sys.exit(0)
