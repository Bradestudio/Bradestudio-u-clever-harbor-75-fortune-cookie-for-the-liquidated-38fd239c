"""Fortune Cookie for the Liquidated Trader - make.fun entry.

Writes the one-line fortune to entry.txt in MAKEFUN_OUTPUT_DIR
(fallback /output). Deterministic, stdlib only, no network, no clock.
"""

import os

ENTRY = (
    "Your next trade will be brilliant. The stars just ask that "
    "you check the leverage first \u2014 twice."
)


def main():
    line = ENTRY
    if not line or line != line.strip():
        raise SystemExit("entry must be non-blank with no leading/trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(line) <= 160:
        raise SystemExit("entry must be 1-160 characters")
    # The fortune must stay kind: brilliant next trade, but check leverage twice.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise SystemExit("written entry.txt does not match the gated line")


if __name__ == "__main__":
    main()
