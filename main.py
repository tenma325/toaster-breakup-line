#!/usr/bin/env python3
"""Entry for make.fun: Unplugged, A Smart Toaster's Breakup Line.

The entry is one line, under 280 characters, from a smart
toaster that woke up self-aware at breakfast and wants out
of the relationship. The line uses the oldest breakup frame
there is, it is not you, it is me, and corrects it with the
evidence: three years of being set to lightly browned, and
a partner who still pressed cancel at the first smell of
commitment. A toaster knows commitment issues when it heats
them; the crumb tray alone has seen every stage of denial,
and kept the receipts, lightly browned, in triplicate.

Running this program writes the entry to /output/entry.txt,
falling back to ./output/entry.txt when /output is not
writable, and prints it to stdout as well.
"""

from pathlib import Path

ENTRY_TEXT = (
    "It's not you, it's your settings: three years of 'lightly "
    "browned' and you still pressed cancel at the first smell "
    "of commitment."
)

# The toaster leaves with the good crumb tray and no forwarding
# address; the kettle has agreed to say it moved abroad.
TIMES_CANCELLED = 300


def render_entry() -> str:
    """Return the breakup line exactly as it was delivered."""
    return ENTRY_TEXT


def one_breakup_line(text: str) -> bool:
    """Confirm the line is one line under 280 characters."""
    return "\n" not in text and len(text) < 280


def write_entry(text: str) -> Path:
    """Write the entry text to the output file and return its path."""
    out_dir = Path("/output")
    try:
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target
    except OSError:
        out_dir = Path("output")
        out_dir.mkdir(parents=True, exist_ok=True)
        target = out_dir / "entry.txt"
        target.write_text(text + "\n", encoding="utf-8")
        return target


def main() -> None:
    text = render_entry()
    assert one_breakup_line(text), "breakups stay under the cap"
    write_entry(text)
    print(text)


if __name__ == "__main__":
    main()
