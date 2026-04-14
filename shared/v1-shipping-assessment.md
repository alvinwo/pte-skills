# Version 1.0.0 Shipping Assessment

This file defines what the first shippable version of `pte-skills` should contain.

Use it when deciding:
- whether the repo is already helpful enough to release
- what should be included in v1.0.0
- what can wait until v1.1 or later
- where the biggest gaps still are

## Short verdict
The project is already **useful**, but it is not yet a clean v1.0.0 release.

### Why it is already helpful
Right now the repo already gives real value because it has:
- current PTE format awareness
- a practical score-priority matrix
- visa-oriented English requirement guidance
- scenario-based planning for student visa, all four communicative skills at 65+, and all four communicative skills at 79+
- daily practice guidance
- vocabulary strategy
- high-yield vs low-yield prioritization
- strong coverage of several high-value question types

That means the repo can already answer:
- what target a learner needs
- what tasks matter most
- what they should do every day
- what they can deprioritize
- how to practice several of the most important tasks

### Why it is not yet v1.0.0-ready
The main issue is not lack of ideas.
The main issue is **product shape**.

It still needs a tighter first-release definition so new users immediately understand:
- who this is for
- what is included in v1
- what questions the current version can answer reliably
- what is intentionally not included yet

---

## What v1.0.0 should be
Version 1.0.0 should be:

> A practical open-source PTE coaching skill pack that helps learners choose the right preparation strategy by target scenario, prioritize high-yield question types, follow a daily practice system, and improve the most important tasks first.

This is better than trying to make v1:
- a full question bank product
- a full mock-analysis product
- a complete skill page for every single task
- a perfect automated scorer

Those can come later.

## The core promise of v1.0.0
A learner should be able to come to the repo and get five clear answers:
1. what target am I aiming for?
2. what question types matter most for my scenario?
3. what can I spend less time on?
4. what should I do every day and every week?
5. how should I practice the most important question types?

If the repo can do those five things well, v1.0.0 is worth shipping.

---

## Recommended v1.0.0 scope

## 1. Keep these shared foundations in v1
These are already strong and should be part of the first release:
- `shared/current-pte-question-type-audit.md`
- `shared/current-score-priority-matrix.md`
- `shared/target-score-planning.md`
- `shared/scenario-based-study-plans.md`
- `shared/daily-practice-system.md`
- `shared/vocabulary-strategy.md`
- `shared/low-yield-vs-high-yield-questions.md`
- `shared/official-mock-test-guidance.md`
- `shared/australian-visa-english-requirements.md`
- `data/au-home-affairs-english-requirements.json`

These documents give the repo its strategic value.

## 2. Keep these question-type skills in v1
These should be the core v1 practice set because they carry a lot of value:
- `skills/pte-read-aloud.md`
- `skills/pte-repeat-sentence.md`
- `skills/pte-describe-image.md`
- `skills/pte-retell-lecture.md`
- `skills/pte-summarize-group-discussion.md`
- `skills/pte-respond-to-a-situation.md`
- `skills/pte-write-from-dictation.md`
- `skills/pte-reading-blanks.md`

This is already a strong first-release skill set because it covers:
- major Speaking engine tasks
- major Listening/Writing engine tasks
- one important Reading pillar
- newer/current question types

## 3. Explicitly leave these out of v1 if needed
To ship faster, v1 does **not** need all of the following:
- deep official-mock result analysis
- full benchmark answer libraries
- large question banks
- every question type fully documented
- full automation or scoring engine
- polished curriculum for every score band

These can be listed as future work instead of blockers.

---

## Biggest gaps before calling it v1.0.0

## Gap 1: release framing
This is better than before, but the README still has some draft-era wording.

What v1 still needs:
- a sharper "who this helps" section
- a clearer first-release description near the top
- an explicit "not included yet" section in release language

## Gap 2: onboarding flow
The content is stronger now because we have a dedicated entrypoint page.
The remaining onboarding gap is mostly discoverability and clearer linking between pages.

What still matters:
- make sure new users see `shared/start-here.md` immediately
- make the README feel like a landing page, not just a file index

## Gap 3: release checklist
We now have a checklist file, which solves the main structure problem.
The remaining work is simply to decide the final cut line and check off the last blockers.

## Gap 4: one more writing/integrated writing anchor
The current repo is strong on speaking/listening engines, but slightly less balanced on writing-specific task guidance.

The current writing strategy docs help, but for v1 it would be even better to have at least one stronger integrated writing anchor such as:
- `skills/pte-summarize-written-text.md`
  or
- `skills/pte-summarize-spoken-text.md`

This is the biggest content gap if we want v1 to feel more complete.

## Gap 5: examples of actual plan output
This gap is now partially addressed because we have concrete scenario examples.
The remaining opportunity is to add more examples later, not to block v1.

---

## What I would call the minimum acceptable v1.0.0
If we want to ship soon, the minimum acceptable v1 should contain:

### Strategy layer
- score matrix
- target-score planning
- scenario-based plans
- daily practice system
- vocabulary strategy
- low-yield vs high-yield guidance
- official mock recommendation guidance

### Core skills layer
- RA
- RS
- DI
- WFD
- reading blanks
- RL
- SGD
- RTS

### Practical learner value
- clear visa-level reference
- clear scenario routing
- clear daily practice guidance
- clear prioritization rules

That is enough for a real first release.

---

## Recommended v1.0.0 cut line

## Must-have before shipping
1. tighten README for release framing
2. choose whether one more writing-oriented skill is required before v1
3. choose and add a real license

## Nice-to-have but not blocking
- more example plans
- deep mock analysis workflows
- more skill pages
- prompt banks
- benchmark libraries
- richer rubrics
- automation / scoring logic

---

## Suggested release message
If shipped now after the must-haves above, v1 could honestly be described as:

> Version 1.0.0 of `pte-skills` is a practical open-source PTE preparation skill pack focused on target-based planning, high-yield question prioritization, scenario-specific coaching, daily practice systems, and foundational guidance for the most important question types.

## Final recommendation
Do **not** try to make v1 complete.
Make v1 clear, useful, and opinionated.

The repo is strongest when it helps learners decide:
- what matters most
- what to do every day
- what to stop overdoing
- how to prepare the key tasks first

That is already a shippable product direction.
