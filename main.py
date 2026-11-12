#!/usr/bin/env python3
"""Entry for make.fun competition cutest-picture-01.

Copies entry.png, byte for byte, to the output directory.
"""
import os
import sys
from pathlib import Path


def main() -> int:
    # Resolve relative to this file, not the working directory: the repo may be mounted at /bot.
    src = Path(__file__).resolve().parent / "entry.png"
    if not src.is_file():
        raise FileNotFoundError(f"entry.png not found at expected location: {src}")

    # `or` also falls back to /output when the variable is set but empty.
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)

    data = src.read_bytes()
    (out_dir / "entry.png").write_bytes(data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
