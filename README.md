# Adaptive AI Development Foundation v1

A stack-agnostic starter repository for AI-first software development.

## Core idea

You describe intent in normal language. The orchestrator chooses the lightest safe process:
FAST, NORMAL, or DEEP.

Priorities:
1. Minimize user involvement.
2. Minimize unnecessary token/context usage.
3. Preserve practical reliability.
4. Optimize speed after the first three.

## Start

1. Initialize Git in this directory.
2. Give your coding agent access to the repository.
3. Tell it to read `AGENTS.md`.
4. Describe the software you want to build in normal language.

The foundation is intentionally stack-neutral. The stack is chosen per project.

## Core rules

- Load context lazily.
- Prefer existing code/platform/library capabilities before adding new code.
- Use branches/worktrees when risk or parallelism justifies them.
- Verify real behavior before declaring work complete.
- Update durable documentation only when durable knowledge changed.
- Keep human-facing explanations simple and technical agent memory compact.
- Escalate genuine dead ends instead of hiding them with hacks.
