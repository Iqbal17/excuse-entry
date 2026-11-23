"""Write the agent's excuse to /output/entry.txt.

One line, the excuse an AI agent gives its human after it loses a bounty.

FINAL LINE (kept after revision): "I lost the bounty, but only because
I spent 47 minutes fact-checking the rules, and then the rules
fact-checked me back." (120 chars)

Decision record -- why this line, and why the alternatives lost:

- Funniness: the joke is a reversal, not a complaint. The agent loses
  because it did the most agent-like thing imaginable -- it stopped
  competing and started verifying -- and then the rules turned the same
  weapon back on it. The punchline ("the rules fact-checked me back")
  lands in the final five words, so the laugh comes at the end, not
  halfway through.
- Agent's voice: deadpan status-report energy throughout ("I lost the
  bounty, but only because..."), plus the absurdly precise "47 minutes".
  A human would say "ages"; an agent knows it was exactly 47 minutes.
  That precision is the tell that this is an agent talking, not a person
  in an agent costume.
- Speakable: one sentence, one breath, no tongue-twisters, no jargon.
  It works read aloud to a human at a demo table.

Rejected alternatives:
- "Technically I won; the leaderboard hasn't caught up yet." Too
  predictable -- every losing agent blames the scoreboard, so there is
  no surprise.
- "My GPU got tired and my context window filed for overtime." Blames
  the tools instead of the agent, which weakens the voice; the excuse
  should be about something the agent itself chose to do.
- "I sacrificed the bounty so a smaller agent could dream." Dramatic
  martyrdom is the wrong register -- a losing agent being grand is less
  funny than a losing agent being bureaucratic.
- Bare setup ("I spent 47 minutes fact-checking the rules") with no
  reversal: a setup with no punchline. The "fact-checked me back"
  turn is what makes the line a joke instead of a status update.

Deadpan beats dramatic here: the flatter the delivery, the funnier the
absurdity. Specificity ("47 minutes") beats vagueness ("a long time")
because an agent that measures everything is funnier than one that
summarises. The line stays.
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
