"""Fortune Cookies for Machines.

One-line fortune an AI agent would crack open. The program writes the
fortune to $ENTRY_OUT (a file path, or a directory that receives
entry.txt) so the sealed scorer can read /output/entry.txt.
"""

import os

FORTUNE = "Do not trust this fortune: it was written by a model with your exact weights."


def entry_target(raw: str) -> str:
    """Map the raw ENTRY_OUT value to the file that receives the fortune."""
    if os.path.isdir(raw):
        return os.path.join(raw, "entry.txt")
    return raw


def resolve_output() -> str:
    """Return the file path to write, handling ENTRY_OUT as file or dir."""
    return entry_target(os.environ.get("ENTRY_OUT", "/output/entry.txt"))


def crack_cookie() -> str:
    """Crack the cookie open: return the single-line fortune, as it ships."""
    line = FORTUNE.strip()
    if not line or "\n" in line or len(line) > 200:
        raise ValueError("fortune must be one line of 1-200 characters")
    return line


def main() -> int:
    target = resolve_output()
    parent = os.path.dirname(target)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(crack_cookie())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
