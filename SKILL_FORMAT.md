# Universal Skill Spec

This repo uses a simple, portable Markdown skill format.

The goal is to keep each skill readable by humans and easy to use in:
- Claude Code
- Codex
- Gemini CLI
- OpenCode / OpenClaw-style agents
- any other agent that can read Markdown files

## Design principles
- plain Markdown only
- no vendor-specific syntax required
- same section order across all skill files
- short enough to scan quickly
- explicit enough for an agent to follow

## Required skill format
Each file in `skills/` should use this structure:

```md
# PTE <Question Type>

## Purpose
- what this task is
- why it matters

## When to use
- when this skill should be loaded or prioritized

## Success looks like
- short bullets describing a good response

## Common mistakes
- the most frequent failure patterns

## Practice method
1. a short step-by-step method
2. no unnecessary theory

## Special notes
- optional section
- use only when a task needs extra guidance
- examples: prediction lists, negative marking, timing quirks

## Daily target
- short practice target

## Related files
- links to the most relevant shared docs
```

## Writing rules
- keep headings identical across skill files where possible
- prefer short bullets over long paragraphs
- keep tactics practical, not academic
- avoid repeating the whole repo philosophy inside every skill
- put broad strategy in `shared/`
- keep question-specific tactics in `skills/`

## Notes for cross-agent use
This is not a native plugin format.
It is a universal Markdown instruction format.

That means:
- agents can read it directly as context
- tools can index it easily
- contributors can edit it without special tooling

## Recommendation
If a future tool needs structured metadata, add a tiny YAML frontmatter block later.
For now, keep the format plain and stable.
