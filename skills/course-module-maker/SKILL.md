---
name: course-module-maker
description: Build one module of an Innovation Labs course, such as the IL27 master's pilot, as a set. Makes the night student deck, the prep guide for the course team and the session plan, all from a module brief and the course design system. Use when the user says "make module 3", "build next week's class", "deck for the journey mapping session" or "prep the workshop".
version: '0.2.0'
---

# Course Module Maker

One module is three artifacts that must agree with each other:

1. **The student deck.** A present-only night deck, shared with students and followed on their phones.
2. **The prep guide.** A Light website for the course team: timings, what to print or check, the running order and links.
3. **The session plan.** A doc the team edits together: the running order with minutes, who runs what, and open decisions.

## Before building

1. Read `references/course.md` for the course facts (modules, dates, loop, skills, exit ritual). For a course other than IL27, ask for the equivalent facts. Don't reuse IL27's.
2. Read `../../design-system/COURSE_DECKS.md`, `../../assets/course-deck/README.md`, `../../design-system/AI_TELLS.md` and `../../design-system/WORKING_RULES.md`. If `COURSE_DECKS.md` or the starter is missing from the installed plugin, say so and build from the latest live module deck (links in `references/course.md`) instead of guessing the patterns.
3. Collect the module brief: number, title, date, the promise in one line, theory blocks, activities, what students make on paper, and what the challenger and exit skills do. If the user gives a source deck (as Module 2 was built on the 11 Sept customer discovery deck), build on it and keep its examples and wording where they hold up.
4. Ask only for what is missing and can't be inferred. Never invent statistics, quotes, studies, people, deadlines or counts. If a number needs a source, show it in a dig-deeper drawer (P13) with the source named. Say which claims come from memory, so they can be checked. When the Module 1 deck was fact-checked, the attribution of the "quarter-inch drill" quote, the origin of "schlep" and the milkshake details were wrong.

## The student deck

- Start from `../../assets/course-deck/starter.html`, set `KEY` to the module prefix (`il27-m3-`), and replace every slide and data constant.
- Fixed opening: route cover (P01) with the module promise as the title, one circled word and a reframe line (P05); then the passport (P27) with earlier modules stamped; then the loop (P16).
- Fixed closing: you decide (P30), what did we just do (P31), log it, stamp it (P32) and the next-week closer with what to bring (P33). Note: on 28 Oct Flavia removed "What did we just do?" and the passport stamp from the Module 2 exit slide, and added a "What you send, in one place" slide after it. Ask whether the next module keeps P31 and the stamp before building the closing.
- Between them, the stops follow the brief. Each theory block gets at least one interaction (`classroom-games`). Examples run on made-up people with a shuffle (P22).
- AI stops are purple and come after paper work. The challenger card (P29) carries the prompt and the Drive download link from `course-skill-pair-maker`.
- The pig flies on the rope on every slide, and balloons are the bullets (`pig-mascot`).
- No physical handouts: everything students need is in the slides.

## The prep guide

Use `website-maker` in Light mode. Include:

- the timeline with minutes;
- the three-step loop;
- the running order with who leads each part;
- what to check before the room opens (projector, QR codes, Drive links, the skill zip);
- the student deck link;
- what students hand in.

Keep it to what the team needs on the day.

## The session plan

Make it as a Claude Docs doc (or the format the team already uses). It holds the running order in a table (time, block, what happens, who, materials), open questions for the team, and the links. If a shared course doc already exists, ask before editing it. The IL27 course plan is co-owned by Flavia and Ana and stays untouched unless Flavia explicitly asks.

## Checks before delivering

- Every slide passes `human-pass`, and `design_tells.py` is clean on the deck and the guide.
- The deck runs with a clean console, and every step reveals, at 1920, 1440×900, 1024 (projector), 844×390 and 390×844 and 360 wide, with no horizontal scroll or overflow (`node --check` on the script first).
- The deck link in student messages is the student deck, never the private course plan.
- Dates, module numbers, stop names and timings match across all three artifacts.
- The skill prompts in the deck match the skill files the students download.
