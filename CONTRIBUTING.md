# Contributing

Thanks for contributing to `pte-skills`.

This repo is intentionally small, practical, and easy to reuse across agents.
Please keep changes clear, concise, and useful for real PTE learners.

## Core principles
- keep the repo simple
- prefer strategy over clutter
- use learner-friendly wording
- keep common terms like PTE, RA, RS, and WFD in English
- ask for the learner's target and weak area before prioritizing
- do not add complexity unless it clearly improves the repo

## Main structure
- `shared/` = shared strategy and planning docs
- `skills/` = question-type skill pages
- `examples/` = short example plans
- `data/` = structured reference data
- `SKILL_FORMAT.md` = format rules for all skill pages

## Adding or editing a skill page
Every file in `skills/` should follow `SKILL_FORMAT.md`.

Keep the section order consistent:
1. `## Purpose`
2. `## When to use`
3. `## Success looks like`
4. `## Common mistakes`
5. `## Practice method`
6. `## Special notes` *(optional)*
7. `## Daily target`
8. `## Related files`

## Style guide
- use short bullets and short paragraphs
- avoid vendor-specific prompt syntax
- keep broad strategy in `shared/`
- keep question-specific tactics in `skills/`
- prefer practical advice over theory
- if the repo already says something clearly, do not duplicate it

## Language guide
- match the user's language where appropriate
- if the user mainly uses Chinese, Chinese-facing wording is fine
- common PTE terms can stay in English
- use learner wording that matches the repo style, such as `7炸` and `8炸`

## Good contributions
- clearer explanations
- simpler structure
- stronger daily practice guidance
- better prioritization logic
- more consistent skill formatting
- concise examples that are easy to adapt

## Before opening a PR
Please check:
- the repo is still easy to scan
- the change does not reintroduce clutter
- skill pages still follow `SKILL_FORMAT.md`
- wording is clear for real learners, not just for contributors

## Pull request tips
A good PR usually includes:
- a short title
- a short summary of what changed
- why the change makes the repo clearer or more useful
