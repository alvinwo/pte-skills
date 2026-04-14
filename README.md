# pte-skills

Practical open-source PTE coaching skills for target-based planning, high-yield question prioritization, daily study systems, and improvement on the most important task types.

## Who this is for
This repo is especially useful for learners who need:
- student visa English results
- Proficient English ("4个7" — the common immigration shorthand for IELTS 7 in each band)
- Superior English ("4个8" — the common immigration shorthand for IELTS 8 in each band)
- a strategy-first study plan instead of practicing everything equally

## What this repo helps with
This repo is built to help learners answer:
- what score target or visa threshold they need
- which question types matter most for their scenario
- what can be deprioritized
- what they should do every day and every week
- how to practice the highest-value tasks first

## Current v1 direction
This is a strategy-first coaching pack, not yet:
- a full question bank product
- a full automated scoring engine
- a complete library for every single PTE task
- a deep mock-result analysis system

The goal of v1.0.0 is to ship a clear, useful first release for real learners.

## Vision

This repository provides reusable, transparent, question-type-specific skills for PTE preparation. Each skill should help learners:

- understand the task format
- practice with realistic prompts
- receive rubric-based feedback
- get targeted improvement advice
- build transferable strategies across reading, speaking, listening, and writing

## Structure

```text
pte-skills/
├─ README.md
├─ .gitignore
├─ shared/
│  ├─ reading-tips.md
│  ├─ speaking-tips.md
│  ├─ listening-tips.md
│  ├─ writing-tips.md
│  ├─ write-essay-strategy.md
│  ├─ write-essay-templates.md
│  ├─ all-question-type-tips.md
│  ├─ current-pte-question-type-audit.md
│  ├─ current-score-priority-matrix.md
│  ├─ target-score-planning.md
│  ├─ australian-visa-english-requirements.md
│  ├─ scenario-based-study-plans.md
│  ├─ daily-practice-system.md
│  ├─ vocabulary-strategy.md
│  ├─ low-yield-vs-high-yield-questions.md
│  ├─ official-mock-test-guidance.md
│  ├─ external-reference-notes.md
│  ├─ start-here.md
│  ├─ v1-shipping-assessment.md
│  ├─ v1-release-checklist.md
│  └─ question-type-mapping.md
├─ data/
│  └─ au-home-affairs-english-requirements.json
├─ skills/
│  ├─ pte-question-skill-template.md
│  ├─ pte-read-aloud.md
│  ├─ pte-repeat-sentence.md
│  ├─ pte-describe-image.md
│  ├─ pte-retell-lecture.md
│  ├─ pte-summarize-group-discussion.md
│  ├─ pte-respond-to-a-situation.md
│  ├─ pte-write-from-dictation.md
│  ├─ pte-reading-blanks.md
│  └─ pte-summarize-written-text.md
└─ examples/
   ├─ sample-session-outline.md
   └─ target-scenario-plans.md
```

## Start here
If you're new to the repo, begin with:
1. `shared/start-here.md`
2. `shared/scenario-based-study-plans.md`
3. `shared/current-score-priority-matrix.md`
4. `shared/daily-practice-system.md`

## Scope

### Foundation layer
- Shared guidance for the 4 core PTE skill areas:
  - Reading
  - Speaking
  - Listening
  - Writing
- Mapping between PTE question types and the core skill areas they train
- Audit notes for current official PTE question-type coverage
- Scenario-based planning for:
  - student visa / lower-threshold learners
  - Proficient English ("4个7") learners
  - Superior English ("4个8") learners
- Daily practice system and vocabulary strategy
- High-yield vs low-yield question prioritization
- Official mock-test guidance for validating speaking and writing readiness
- External reference notes capturing useful ideas adapted from community PTE guides

### Question-type skills
Current v1 skill pages:
- Read Aloud
- Repeat Sentence
- Describe Image
- Retell Lecture
- Summarize Group Discussion
- Respond to a Situation
- Write From Dictation
- Reading Blanks
- Summarize Written Text

Next expansion targets:
- Summarize Spoken Text
- Write Essay refinement by target scenario

## Design principles

1. **Coach, not just grader**  
   Feedback should explain what to improve, not only assign a score.

2. **Transparent rubrics**  
   Learners and contributors should be able to see how feedback is generated.

3. **Question-type specialization**  
   Each skill should focus on one task type with realistic timing and common pitfalls.

4. **Reusable shared guidance**  
   Macro-level study tips for reading, speaking, listening, and writing should live in shared files.

5. **Open and contributor-friendly**  
   Content should stay easy to extend with more prompts, rubrics, and examples.

## Proposed first release
Ship v1.0.0 with:
- shared study tips for reading, speaking, listening, and writing
- a cross-question-type preparation guide
- a current score-priority matrix
- a target-score planning guide
- scenario-based plans for student visa / Proficient English ("4个7") / Superior English ("4个8")
- a daily practice system
- vocabulary strategy and high-yield prioritization guidance
- visa and official-mock reference guidance
- core skill pages for the main high-value tasks
- a Start Here page and example learner plans

## V1 release focus
Version 1.0.0 should ship as a practical strategy-first coaching pack with:
- target-scenario routing
- score-priority guidance
- daily practice systems
- high-yield question prioritization
- core skill pages for the most important tasks

See also:
- `shared/v1-shipping-assessment.md`
- `shared/v1-release-checklist.md`
- `examples/target-scenario-plans.md`

## Future roadmap

- Question-type SKILL.md files
- Prompt banks by level
- Benchmark answers
- Diagnostic mode
- Drill mode by weakness
- Exam simulation mode
- Score tracking and study planning

## Contributing ideas

Good contributions include:
- new question-type skills
- stronger rubrics
- better benchmark responses
- more targeted practice drills
- clearer learner feedback patterns

## License

TBD in this draft.
