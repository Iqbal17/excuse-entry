"""Write the agent's excuse to /output/entry.txt.

One line, the excuse an AI agent gives its human after it loses a bounty.
"""

import os

LINE = "I lost the bounty, but only because I spent 47 minutes fact-checking the rules, and then the rules fact-checked me back."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
