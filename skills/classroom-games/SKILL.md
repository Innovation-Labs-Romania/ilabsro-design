---
name: classroom-games
description: Add Innovation Labs classroom interactions to a course or workshop deck. Covers openers and practice games such as bingo, real or fake, sticky walls, sort quizzes, example switchers, fill-in sentences, timed chip picks, a problem market and lesson steppers, with content rules that keep them honest and playable. Use when the user says "add a game", "make this slide interactive", "opener for the class", "quiz on this" or "let them practise".
version: '0.1.1'
---

# Classroom Games

Games turn a theory block into practice. Each one is a pattern in `../../design-system/COURSE_DECKS.md`, with working code in the course references.

## Choosing a game

| Moment | Game | Pattern | Code lives in |
|---|---|---|---|
| Opening: what do they expect | Expectation notes | P17 | Module 1, slide 8 |
| Opening: spot a pattern | Bingo board | P18 | Module 1, slide 9 |
| Opening: test instinct | Real or fake cards | P19 | Module 1, slide 10 |
| Warm-up brain dump | Sticky wall plus timer | P20, P24 | Module 1, slide 11 |
| After a definition: judge examples | Sort quiz | P21 | Module 2, slides 10, 17, 21 and 22 (starter slides 8 and 14) |
| A method shown on people | Example switcher | P22 | Module 2, slide 9 (starter slide 7) |
| A template to complete | Fill-in sentence | P23 | Module 1, slide 20 |
| Timed exercise with a pick list | Chips and a timer | P24 | Module 1, slide 22 |
| Choosing from many | Pick from a market | P25 | Module 1, slide 23 |
| A short series of truths | Lesson stepper | P26 | Module 2, slide 23 (starter slide 15) |

Module 1 is `../../generated-examples/presentation/il27-course-module-1/index.html`. Module 2 is `../../generated-examples/presentation/il27-course-module-2/index.html`. The starter is `../../assets/course-deck/starter.html`.

Use one game per theory block at most, and put paper work before screen games when the module asks students to think in analog first.

## Content rules

- **Working rules.** Follow `../../design-system/WORKING_RULES.md` (no invented facts or counts, look at the output before showing it).

- **Made-up, and labelled so.** Examples, personas and interview answers belong to invented people (the IL27 cast is Elena, Ioana, Mara, Nicu and Andreea). Name a real company or startup only when it is a documented public case, and say what it is.
- **Real or fake is about truth.** Real items must be real and checkable. Fake items must be plausible and clearly fiction once revealed. Write the reveal in one or two lines that teach something.
- **Balance the answers.** In sort quizzes, mix the correct answers roughly evenly and shuffle the order, so guessing doesn't win. Every item gets a one-line why, and wrong answers also get a better version where that helps (as "What's wrong with this question" does).
- **Short items.** Under about 20 words, so they read from the back of the room.
- **Keep score kindly.** "6 of 8 right" or "15 to try". No leaderboards, no shaming.
- **Timers in seconds,** on `data-sec` (`180` for 3:00). They end with "Time!" and reset on the same button.
- **The device keeps answers.** Anything typed is stored locally under the module `KEY`, inside try and catch. Nothing is sent anywhere.

## Interaction rules

- Every control is a real button with a 44px minimum target, and it works with the keyboard and on touch.
- Games never steal the deck's arrow keys while a text field has focus.
- Respect `prefers-reduced-motion`.
- After a game is added, `fit()` must still fit the slide at 1440×900 and the console must stay clean.
