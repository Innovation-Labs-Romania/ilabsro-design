# Changelog

## 0.9.0 (4 Nov 2026)

One version that replaces 0.5.1 (organization), 0.7.0 (`ilabsro-design-updated`) and the 0.8.0 zip. An organization Owner or Primary Owner uploads it in Organization settings > Plugins with the same name, `ilabsro-design`, which replaces the existing plugin. Then remove `ilabsro-design-updated`, and Flavia turns off her private copy.

### Brought back

The 0.8.0 zip held only `skills/`. These folders are restored from 0.7.0 (the few edits to them are listed below):

- `assets/`: the 2027 logos, backgrounds and the 16 brand elements
- `design-system/`: tokens, brand elements, component catalog, `AI_TELLS.md`
- `docs/`: usage and examples
- `generated-examples/`: websites, decks, one-pagers, social, visuals, the context-engineering Reel
- `README.md`

Nothing from 0.5.1 is lost: 0.7.0 already held everything in it.

### Kept from 0.8.0

- New skills: `course-module-maker`, `course-skill-pair-maker`, `classroom-games`, `pig-mascot`, `artifact-index-updater`.
- `presentation-maker`: the course and workshop mode.

### New: the team's working rules

`design-system/WORKING_RULES.md` gathers Flavia's corrections from 20 Oct to 2 Nov (from the IL27 context update of 4 Nov). The design system file points to it, and the output makers, course skills, content planner, pig mascot and index updater read it. The voice lenses don't. In short:

- no invented deadlines, counts, quotes or statistics; flag claims from memory so they can be checked
- check consent in the source sheet, comments included, before naming or quoting anyone
- match the established reference artifact for social content and reuse its assets
- keep Flavia's original pages when rebuilding one of her decks
- read the live artifact before editing it
- look at the output before showing it, with the full viewport check for decks

### Changed skills

- `insta-post-maker` 0.6.0: posts in English, the logo in place of the words "Innovation Labs", no frame numbering ever, no blurred star, the pig shows its head on the first slide, the event name "AI Validation Bootcamp SiSC", a cleaner LinkedIn variant, no music in videos, Design canvas tips.
- `reels-maker` 0.8.0: no music, finished pieces instead of sketches, one page for a set of Reels, English, no numbering.
- `content-planner` 0.1.3-draft, `classroom-games` 0.1.1: they read the working rules.
- `presentation-maker` 0.6.0: keep the source deck's pages, pace for the room, the publish check.
- `pig-mascot` 0.2.0: falls back to the live Pig Studio, headless export, head first on the first slide of a post, the balloon in the middle of the back, one pig per view, working names held back.
- `course-module-maker` 0.2.0: course facts updated (the .txt exit file, skill versions, field track, photo rule, roster rules); a question to settle about the closing slides; the co-owned course plan stays untouched.
- `course-skill-pair-maker` 0.2.0: the rules learned from the Module 1 submissions, the .txt exit, a question about the passport stamp, a warning about the WhatsApp example still in the archived v0.1 files, live testing and checker notes.
- `artifact-index-updater` 0.2.0: one index only, and every link gets opened before it goes in.
- `website-maker` 0.4.2, `one-pager-maker` 0.4.2, `brand-image-maker` 0.1.3: they read the working rules.

### Still missing (ask Flavia where these files are)

The 0.8.0 skills point to files that aren't in any of the three zips. Her installed copy is the 0.7.0 one, which doesn't have them either, so they may exist only in the chat where 0.8.0 was built:

- `design-system/COURSE_DECKS.md` (patterns P01–P35)
- `assets/course-deck/` (`starter.html`, `README.md`, `pig-flying.png`, `balloon-*.svg`)
- `assets/pig/` (`pig-studio.html`, `pig-flying.png`)
- `generated-examples/presentation/il27-course-module-1/` and `il27-course-module-2/`

Until they're added, `course-module-maker` builds from the live module decks and `pig-mascot` uses the live Pig Studio.

### Not in this version

- The 28 Oct proposals (P36–P43, `deck_qa.py`, `deck_additions.md`, six reference prompts): not received.
- The latest challenger and exit pairs (recorded as `m1-v0.2`, `m2-v0.3`, `m2-field-v0.2`): only the v0.1 copies are bundled.
- `flavia-voice` and `email-maker`: not part of any of the plugin zips.
