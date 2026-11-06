---
name: course-skill-pair-maker
description: Write the challenger and exit skill pair for one course module (il27-challenger-mN and il27-exit-mN), package each as a downloadable skill zip plus a copy-paste prompt, and wire them into the module deck. Use when the user says "make the skills for module 3", "challenger for next class", "exit skill" or "update the challenger".
version: '0.2.0'
---

# Course Skill Pair Maker

Every class in the loop (**think in analog, challenge with AI, human synthesis**) has two skills:

- **Challenger.** It runs after the paper work. It pushes back on what the student made, never makes it for them, and ends with a `CHALLENGE LOG`.
- **Exit.** It runs in the same chat. It records what happened without improving it, and writes a student summary plus an IL log for the team.

## Before writing

1. Read both archived pairs in `references/` (Module 1 and Module 2, version v0.1). They are the house structure. They predate the rules learned from the Module 1 submissions, so the hard rules below win where they differ. If the user can share the latest versions (recorded on 28 Oct as `m1-v0.2`, `m2-v0.3` and `m2-field-v0.2`), read those instead. Match their structure, and write the content fresh for the new module.
   Also read `../course-module-maker/references/course.md` for the exit file format and `../../design-system/WORKING_RULES.md`.
2. Get from the module brief:
   - what students make on paper (the artifacts the challenger reads);
   - the three to five challenge modes;
   - the default order and minutes;
   - the date;
   - what the exit hands in.
3. Never copy a previous module's modes unless the brief asks for it.

## Challenger structure (keep the headings)

1. **Title line:** `# IL27 challenger skill · Module N · version mN-v0.1`. The intro names the loop and says the student owns step 3.
2. **Hard rules.** Keep the house rules every module shares:
   - never produce the work, not even as a suggested question;
   - never rewrite the student's work;
   - quote the student's exact words, then ask one question per issue;
   - stay short;
   - reply in the student's language, with labels in English;
   - no real people's personal data;
   - when a photo is unreadable, ask instead of guessing;
   - nothing the AI says is evidence about real users;
   - photos of the paper work are required, and the challenger does not start without them;
   - one question per point, with unique point numbers;
   - one reason per point, in the student's own words, or `skipped by student` when they give none;
   - stay inside the student's paper: no tools, channels or numbers they did not write;
   - no answer options or sample prompts inside questions;
   - lines marked "as read" are copied exactly;
   - no confidence labels, and the student keeps every choice;
   - the skill never grades.
   Don't reuse the WhatsApp example from the archived Module 1 v0.1 files (`challenger-m1-v0.1.md` and `exit-m1-v0.1.md` still contain it): it likely primed the challenger and was removed from the later prompt.
3. **What the student brings**, listing the paper artifacts and what to do if one is missing.
4. **The modes.** List them, ask which to run, recommend the default order with minutes, and give each mode its own "look for" list.
5. **Closing the session: the challenge log.** It is a fixed block starting `CHALLENGE LOG` / `skill: il27-challenger` / `version: mN-v0.1` that the exit skill can find.
6. **Examples.** Three short exchanges: two modes in action, and the student asking the AI to do the work, answered with a refusal and a question.

## Exit structure (keep the headings)

1. **Title line and role:** a careful recorder, not a coach.
2. **Hard rules:**
   - record, never improve;
   - add no new ideas;
   - quote wherever the format says so;
   - write `not given` instead of inventing;
   - use the student's language for the summary and English labels for the log;
   - no personal data.
3. **Steps:**
   - find the challenge log;
   - ask once for what's missing;
   - write two code blocks;
   - close by telling the team to save the output as one plain .txt, one file per team, and have one member email it as `course.md` describes (file name, subject, empty body, every teammate's name inside, sent to contact@tech-lounge.ro for IL27). No zip, Word or RTF. On 28 Oct Flavia removed the passport stamp from the Module 2 exit prompts: ask whether a new module brings it back.
4. **Block 1: the student summary,** and **Block 2: the IL log.** The IL log records how the skill behaved and how the student moved through the loop, so the team can compare work before and after the AI step.
5. **Example of the summary tone.**

## Packaging

For each skill, make:

- **A skill folder** named `il27-challenger-mN` or `il27-exit-mN`. Its `SKILL.md` has frontmatter (`name`, a description that says when to use it and names the module, `version: mN-v0.1`). The body is the prompt without the first "Paste everything below…" line.
- **A zip of that folder,** for students who can install skills.
- **A prompt file** (`il27-challenger-mN-prompt.md`) holding the full copy-paste text, starting with the "Paste everything below…" line. This is for students using any AI chat.

Students are outside the organization, so artifact downloads don't reach them. Put the zips and prompt files in the module's public Drive folder (one per module) and put that link on the deck's challenger card (P29). Put the same prompt text in the deck's `TEXTS` so the copy buttons match the files.

## Versioning

Bump the version (`m3-v0.2`) when the prompt changes after a class, and keep the earlier version so logs stay readable. The exit skill and the deck must name the same challenger version.

## Checks

- Read the challenger as a student trying to get answers out of it. Every route to "just tell me" should end in a question.
- Check that the exit skill can find the exact `CHALLENGE LOG` header the challenger writes.
- Run `human-pass` on the student-facing lines.
- Recommended: test the pair in a live chat before class, with photos. The 28 Oct versions were never tested live; a tick-box test list is in the skills review doc.
- When checking submissions: the header counts are written by the AI, so recount from the points table. Keep "no" apart from "not visible", because the logs start at the challenger's first reply.
- Upload the zips to Drive with a size check after upload, and the prompts as markdown.
