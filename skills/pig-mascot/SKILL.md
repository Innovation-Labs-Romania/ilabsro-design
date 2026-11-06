---
name: pig-mascot
description: Keep the Innovation Labs flying pig consistent across decks, Reels, posts and pages. Picks the right pig, outfit, held item and move for the moment, and exports it from the pig studio as PNG, animated SVG or MP4. Use when the user mentions the pig, "we make pigs fly", the mascot, a pig animation or a pig for a slide, Reel or post.
version: '0.2.0'
---

# Pig Mascot

"We make pigs fly" is Innovation Labs' line, and the flying pig is its mascot. There is one pig system: `../../assets/pig/pig-studio.html` ("The flying pigs, redrawn"). Use it as the source. Never redraw the pig from scratch or swap in a stock pig.

If that file isn't in the installed plugin, use the live Pig Studio artifact instead: https://claude.ai/artifact/Nvzc7JBuDsgUygivBXNtZw. Read it with the Artifact tool and say which source you used.

## The cast

- **Pigs:** Boy, Girl, Mentor (grey hair, moustache, bushy brows), Mangalița (woolly curls) and Spotty. Mentor, Mangalița and Spotty are working names: don't put them in labels or export filenames until the team confirms them.
- **Glasses:** the Boy and the Mentor wear glasses by default; the others don't.
- **Outfits:**
  - superhero cape (the default);
  - pilot;
  - lab coat;
  - graduate;
  - Demo Day party;
  - winter (beanie and striped scarf);
  - hackathon (headphones and a grey hoodie cape);
  - investor day (dark suit cape and a red tie).
- **Held items:**
  - nothing;
  - a balloon on the back or on the head;
  - paper and pencil;
  - a magnifier;
  - a laptop;
  - a trophy;
  - a briefcase.

## Matching the pig to the moment

| Moment | Pig choice |
|---|---|
| Course deck, every slide | The deck pig (`assets/course-deck/pig-flying.png`) on the rope, holding a balloon. It is the progress bar (P34). |
| Paper and analog steps | Paper and pencil |
| Research and discovery | Magnifier |
| Building and prototyping | Laptop, or the hackathon outfit |
| Demo Day and celebrations | The Demo Day party outfit, or a trophy |
| Partners and investors | The investor day outfit, or a briefcase |
| Graduation and final review | The graduate outfit |
| Winter events | The winter outfit |

## Moves (from the studio)

- **Loop-the-loop:** for stamping the passport. Balloons burst out at the end.
- **Happy hop:** for a right answer in a game. Quick and small.
- **Wobble:** for a wrong answer. The brow drops, then the pig shakes it off.
- **Fly the route:** for a cover. The pig follows the dotted path past the stops.
- **Let go and fly off:** for "Get out of the building". The balloon floats away.

The pig is calm by default: the bigger moves only happen when something triggers them. With reduced motion turned on, the pig stays still.

## Exporting

Open the studio and pick the pig, outfit, held item and glasses. Then export:

- **PNG** at 800, 1600 or 3200px, on a transparent, night teal or white background;
- **animated SVG**;
- **MP4**, a seamless 5-second loop at 1080 square, 1080×1920 vertical or 1920×1080 wide, for Reels and slides.

For a headless build, drive the studio from Playwright: it exposes `setPig`, `bakePig` and `frameSVG`, which export transparent PNG pigs for posts. Only when the studio can't run at all, use `assets/pig/pig-flying.png` and say so.

## Rules

- **Working rules.** Follow `../../design-system/WORKING_RULES.md`.

- **One pig per view.** When a big pig flies on a slide, hide the small rope pig there.
- **Head first.** On the first slide of a post, the pig shows its head, not its rear.
- **The balloon is tied near the centre of gravity,** in the middle of the back, as in the deck.
- **The pig supports the content.** Keep it off text and away from the nav.
- **Balloons are the pig's balloons.** Use the official balloon set (`assets/course-deck/balloon-*.svg`); purple belongs to AI steps only.
- **Keep it kind.** The pig is never mocked or used as a joke at a student's expense.
