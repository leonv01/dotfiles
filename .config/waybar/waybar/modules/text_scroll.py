#!/usr/bin/env python3
import os
import sys
import json
import tempfile

BUFFER_WIDTH = 30
SCROLL_FILE = os.path.join(tempfile.gettempdir(), "waybar_scroll_index")

def main():
    if len(sys.argv) < 2:
        print("Usage: scroll_output.py '<your scrolling text>'")
        sys.exit(1)

    full_text = sys.argv[1]
    padded_text = full_text + "   "  # Padding between loops

    # Load current scroll index
    try:
        with open(SCROLL_FILE, "r") as f:
            index = int(f.read().strip())
    except (FileNotFoundError, ValueError):
        index = 0

    # Get visible part
    start = index % len(padded_text)
    display_text = (padded_text + padded_text)[start:start + BUFFER_WIDTH]

    # Save next index
    with open(SCROLL_FILE, "w") as f:
        f.write(str((index + 1) % len(padded_text)))

    output = {
        "text": display_text,
        "tooltip": full_text
    }
    print(json.dumps(output))


if __name__ == "__main__":
    main()

