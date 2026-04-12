# pte-skills

Open-source agent skills to help people practice and prepare for PTE question types.

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
│  └─ question-type-mapping.md
├─ skills/
│  └─ pte-question-skill-template.md
└─ examples/
   └─ sample-session-outline.md
```

## Draft scope

### Foundation layer
- Shared guidance for the 4 core PTE skill areas:
  - Reading
  - Speaking
  - Listening
  - Writing
- Mapping between PTE question types and the core skill areas they train

### Question-type skills
Initial high-value targets:
- Read Aloud
- Repeat Sentence
- Describe Image
- Retell Lecture
- Write From Dictation

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

## Proposed first milestone

Ship a polished draft with:
- shared study tips for reading, speaking, listening, and writing
- a question-type mapping document
- one reusable question skill template
- one example learner session outline

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
