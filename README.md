# pte-skills

English | [简体中文](zh-CN/README.md)

A clear, strategy-first PTE Academic prep repo. Chinese explanations and English practice are available in the [Chinese edition](zh-CN/README.md).

This project helps learners decide:
- what target they need
- what their weak area is
- which question types deserve the most time
- what to practice every day
- how to approach the main high-yield tasks

## Who this is for
- student visa learners
- 7炸 learners
- 8炸 learners
- anyone who wants a simple, practical study system

## Repo structure
```text
pte-skills/
├─ README.md
├─ LICENSE
├─ CONTRIBUTING.md
├─ SKILL_FORMAT.md
├─ shared/
│  ├─ start-here.md
│  ├─ priority-map.md
│  ├─ study-plan.md
│  ├─ four-skills-guide.md
│  ├─ visa-requirements.md
│  ├─ coaching-guide.md
│  └─ sources.md
├─ skills/
│  ├─ pte-read-aloud.md
│  ├─ pte-repeat-sentence.md
│  ├─ pte-describe-image.md
│  ├─ pte-retell-lecture.md
│  ├─ pte-summarize-group-discussion.md
│  ├─ pte-respond-to-a-situation.md
│  ├─ pte-write-from-dictation.md
│  ├─ pte-reading-blanks.md
│  └─ pte-summarize-written-text.md
├─ examples/
│  └─ study-plan-examples.md
├─ data/
│  └─ au-home-affairs-english-requirements.json
├─ zh-CN/
│  ├─ README.md
│  ├─ shared/
│  ├─ skills/
│  └─ examples/
└─ publishing/
   └─ xiaohongshu-launch.zh-CN.md
```

## Use with an AI assistant

No npm or installation is needed to read these guides. Upload/paste [the coaching guide](shared/coaching-guide.md), [the study plan](shared/study-plan.md), and a relevant task page into a Markdown-friendly assistant. Upload referenced guides as needed; a pasted file does not automatically load its links.

Try: “Use these PTE Academic guides. I have 45 minutes per day and Writing is my weakest section. Ask only for missing details, give me a plan that fits, then coach one task at a time. Explain in Chinese and keep exam answers in English.”

The host must support audio/image input for audio/image feedback. This pack provides instructions, not an audio player or official scoring engine. Read the [coaching guide](shared/coaching-guide.md).

## Start here
1. [Start Here](shared/start-here.md)
2. [Priority Map](shared/priority-map.md)
3. [Study Plan](shared/study-plan.md)
4. the skill pages you need most

## Skill format
This repo uses a small, universal Markdown skill format.

See:
- `SKILL_FORMAT.md`

The format is designed to work well as plain context for:
- Claude Code
- Codex
- Gemini CLI
- OpenCode / OpenClaw-style agents
- other Markdown-friendly agent tools

It is not a vendor-native plugin format.
It is a portable Markdown instruction format.

## Core ideas
1. Ask the learner for the target first.
2. Ask the learner for the weak area first.
3. Prioritize observed weaknesses and required section scores; task priorities are coaching suggestions, not official weights.
4. Keep the system simple enough to follow every day.
5. Use official mock tests to validate readiness, especially for speaking and writing.

## Current skill focus
The repo is intentionally centered on these core skill pages:
- `skills/pte-read-aloud.md`
- `skills/pte-repeat-sentence.md`
- `skills/pte-describe-image.md`
- `skills/pte-retell-lecture.md`
- `skills/pte-summarize-group-discussion.md`
- `skills/pte-respond-to-a-situation.md`
- `skills/pte-write-from-dictation.md`
- `skills/pte-reading-blanks.md`
- `skills/pte-summarize-written-text.md`

## What this repo is not
- not a giant question bank
- not a full scoring engine
- not a full mock-analysis product
- not a complete library for every single PTE task yet

## Contributing
See:
- `CONTRIBUTING.md`

Good contributions are:
- clearer explanations
- better examples
- stronger practice routines
- concise updates to the existing strategy
- skill pages that follow `SKILL_FORMAT.md`

## License
This repo uses the MIT License.
See:
- `LICENSE`

## Sources and sharing

- [Official sources and scope](shared/sources.md) — checked 2026-09-09.
- [Chinese student edition](zh-CN/README.md) — onboarding, all nine task guides, and worked examples.
- [Xiaohongshu launch draft and tool comparison](publishing/xiaohongshu-launch.zh-CN.md).
