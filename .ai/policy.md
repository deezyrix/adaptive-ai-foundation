# Foundation Policy

## Priority order

1. Minimize user involvement.
2. Minimize unnecessary token and context use.
3. Maximize practical reliability.
4. Optimize execution speed.
5. Preserve portability across models and coding environments.

## Minimal Implementation Policy

Before writing new code, ask in order:

1. Is the change actually needed?
2. Does equivalent functionality already exist in the project?
3. Does the language standard library provide it?
4. Does the platform/framework already provide it?
5. Does an existing installed dependency provide it?
6. Is a small, well-maintained new dependency cheaper than custom implementation?
7. Only then write new custom code.

Minimal does NOT mean code golf.
Do not trade away readability, validation, error handling, security, or maintainability.

## Context policy

- Start with compact durable context only.
- Read source files, history, tests, docs, or web material only when relevant.
- Do not ingest whole repositories by default.
- Summarize durable findings instead of copying research dumps into memory.

## Documentation policy

Code is the primary source of truth.
Documentation stores only facts code cannot cheaply communicate to future agents/humans.

Update:
- `.ai/project-map.md` for architecture/topology changes.
- `.ai/project-state.md` for durable current-state changes.
- `.ai/decisions.md` for long-lived rationale.
- `docs/guide/` for human-relevant architectural changes.

Do not update documentation for trivial edits.

## Verification policy

Verification must match the failure mode.
Prefer real execution and behavior checks over ritual test generation.
Add automated tests where they materially reduce regression risk.

## Dead-end policy

A retry is justified only by new evidence, a new hypothesis, or a materially different tool/model.
Repeated attempts without new signal are prohibited.
If blocked, explain the issue to the user plainly and stop before introducing hacks.
