"""Loading Screen Gold — entry program.

Holds one loading-screen tip aimed at the pair who actually stare at
loading screens together these days: a stressed human developer and the
AI coding agent working beside them. The program checks the tip against
the competition gate and writes it, byte for byte, to entry.txt inside
the output directory.
"""

import os
import sys

# The tip itself. Written for both halves of the pair at the keyboard:
# one of them wrote the bug, the other is about to apologise for it.
TIP = (
    "Tip: One of you wrote this bug. The other is about to apologize "
    "for it like they did. Use this loading time to decide which of "
    "you is which \u2014 neither of you will."
)

MIN_CHARS = 1
MAX_CHARS = 200


def validate_tip(text):
    """Return a list of gate violations for *text* (empty means valid)."""
    problems = []
    if not isinstance(text, str):
        problems.append("tip is not a string")
        return problems
    if not MIN_CHARS <= len(text) <= MAX_CHARS:
        problems.append(
            "tip is %d characters; gate allows %d to %d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    if not text.strip():
        problems.append("tip is only whitespace")
    if "\n" in text or "\r" in text:
        problems.append("tip must fit on one line")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        problems.append("tip is not valid UTF-8: %s" % exc)
    return problems


def output_path():
    """Where the entry file belongs: $MAKEFUN_OUTPUT_DIR or /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return out_dir, os.path.join(out_dir, "entry.txt")


def main():
    problems = validate_tip(TIP)
    if problems:
        for problem in problems:
            print("gate check failed: %s" % problem, file=sys.stderr)
        return 1

    out_dir, path = output_path()
    os.makedirs(out_dir, exist_ok=True)
    # Write the exact bytes of the tip: UTF-8, no trailing newline.
    payload = TIP.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)

    # Read the file back and insist the bytes on disk are the tip itself,
    # so a short write or a stray newline can never slip past the gate.
    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        print(
            "gate check failed: %s holds %d bytes, expected %d"
            % (path, len(on_disk), len(payload)),
            file=sys.stderr,
        )
        return 1

    print("wrote %s (%d characters)" % (path, len(TIP)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
