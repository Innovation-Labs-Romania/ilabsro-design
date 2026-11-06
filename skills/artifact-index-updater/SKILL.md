---
name: artifact-index-updater
description: Keep the Innovation Labs Artifact Index current. Adds new artifacts with real previews, places Reels on the shelf, updates links and descriptions, and republishes the index to the same URL. Use when the user says "add this to the artifact index", "update the index", "I made a new deck, put it in the list" or shares new artifact links for the index.
version: '0.2.0'
---

# Artifact Index Updater

The index is one published artifact: https://claude.ai/artifact/R1EyEBqW2DUjAmsrGgor95. Its page holds every entry as a JSON array (`ENTRIES`) inside the main script. The page is the source of truth: always start from the live version and never from an old local copy.

## Steps

1. **Read the live index** with the Artifact tool (`read`). From the saved file, pull the `ENTRIES` array into `data.json`. Then list the published files (`scope: files`) so you can reuse the previews and media already there.
2. **Collect the new items.** For each one you need:
   - title;
   - link;
   - what it is (one or two sentences, from the artifact itself or from the user);
   - category: `strategy`, `content`, `visual` or `systems`;
   - format: `website`, `deck`, `one-pager`, `carousel`, `visual`, `workflow`, `system` or `documentation`;
   - tags;
   - an access note (`Private` or `Organization only`) when it isn't open to anyone.

   Read each artifact to write its description. If it can't be read, ask the user for a line about it. Never guess what an artifact contains.
3. **Get a real preview.** Load the artifact's HTML (from the read) in Playwright at 1440×900, screenshot the first screen and save it as a 960×600 JPG in `previews/<id>.jpg`. For decks, use the cover slide. When the artifact can't be loaded, ask the user for a screenshot. Without one, leave `preview` out, and the card falls back to a branded ground.
4. **Reels go on the shelf.** An entry with a `reel` object (`letter`, `poster`, `title`, `chips: [style, duration]`) appears on the Reels shelf instead of the library. A poster is a 9:16 screenshot of the Reel's first frame. Reels without a poster sit in the second row.
5. **Add the entries** to `data.json`. Keep the existing entries unchanged unless the user asked for a change. Use stable kebab-case ids.
6. **Rebuild and check.**
   - Run `python3 assets/build.py assets/template.html data.json index.html`. If the live page has drifted from `assets/template.html`, replace the `ENTRIES` array inside the live page instead.
   - Load the page in Playwright at 1440×900 and 390×844: the console must be clean, there must be no sideways scroll, every card must have an image or cover, and the filters must work.
   - Run `../human-pass/scripts/design_tells.py`.
7. **Republish to the same URL** (`url` set to the index) with the new preview files in `files`. Earlier files stay. Say in one line what was added.

## One index only

Follow `../../design-system/WORKING_RULES.md` as well, especially reading the live artifact before editing it.


- There is exactly one index, at the URL above. Older copies of the index have existed and caused mix-ups. If you find another copy, don't update it: tell the user and keep working on the URL above.
- Open every link before adding or keeping it, and check that it shows the artifact the entry describes. One entry once pointed to the wrong artifact, and a rebuilt artifact may have a new URL, so check it.

## Data rules

- **Never invent provenance.** Prompts, dates, statuses and previews come from the source or stay out. Prompts appear only where an archived prompt exists (`prompt: {kind: 'original' | 'similar', text}`).
- **Private links stay visible.** Every entry shows its link with the access note, and only people with access can open it.
- **Media entries** (carousels, illustrations and asset sets) open in the viewer: `media: {type: 'carousel', frames: [{src, w, h, alt}]}` or `{type: 'image', src, w, h, alt}`.
- **Alt text and descriptions describe.** Every image has alt text that says what it shows, and descriptions say what the artifact is and who it is for, without marketing language.
