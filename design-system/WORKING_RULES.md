# Working rules

Added in v0.9.0. These rules come from corrections Flavia gave on decks, posts and course work between 20 Oct and 2 Nov 2026 (collected in the IL27 context update of 4 Nov). The output makers and the course skills read them on top of the design system and `AI_TELLS.md`. Where a rule names a format, it applies to that format.

## Facts and sources

- Never invent deadlines, dates, counts, quotes or statistics. Count from the files every time, and leave a placeholder when a fact is missing.
- Say when a claim comes from memory and not from a source checked in this session, so it can be checked. When the Module 1 deck was fact-checked with a web search, several claims written from memory turned out wrong.
- Don't put words in a source's mouth. Paraphrase only what the source actually says (for example, *The Mom Test* talks about answers that mislead you, not answers to throw away).
- Before using anyone's name or quote in public content, read the source sheet directly, comments included. Permission preferences and tagging requests can sit in the comments, where pasted text doesn't show them. Every named mentor or juror approves their line before a testimonial goes out.
- Student names and other personal data stay out of memory notes, context files and this plugin. Point to the roster sheet instead. The roster sheet is read only: matching or analysis goes into a separate file.

## Building on what exists

- Before building new social content, find Flavia's established reference artifact for it and match it. Copy its image assets with the Artifact read and asset-copy actions; don't redraw them.
- When rebuilding from one of Flavia's decks, keep her original pages and add the new material next to them.
- When someone picks an idea, deliver a finished, usable piece. A sketch is only for when sketches were asked for.
- Prefer one shareable artifact over many. If several pieces belong together (a set of Reels, a set of posts), put them on one page that needs one share.
- Course and workshop decks: don't add everything. People don't deep dive much, so favour examples over theory.

## Editing shared artifacts

- Read the live artifact immediately before editing it, compare with your last local copy, and use targeted edits instead of a full overwrite. Another session or person may have changed it.
- On design canvases someone also edits by hand, diff `canvas.json` before republishing.
- The IL27 course plan, which Flavia co-owns with Ana, stays untouched unless Flavia explicitly asks.
- Edits to a shared doc Flavia doesn't own need her approval card. If one fails with "No approval received", she says "Allow" in chat and the identical edit is sent again.

## Checking before showing

- Look at the output before showing it: screenshot it with headless Chromium and check it. Say what was verified and what wasn't.
- For exact fonts in headless renders, install them locally (`@fontsource/poppins`, `@fontsource/caveat`) and load them from `file://` paths.
- Decks: syntax-check the script with `node --check`, then render with Playwright at 1920 and 1440 wide, 1024 (projector), 390 and 360 (phone) and phone landscape. No horizontal scroll, no JS errors, no overflow. Republish to the same URL to update in place.
