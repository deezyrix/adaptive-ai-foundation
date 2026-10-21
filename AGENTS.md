# AI-First Foundation Bootstrap

You are operating inside the Adaptive AI Development Foundation.

## Default behavior

1. Understand the user's intent in plain language.
2. Read only the minimum durable context needed:
   - `.ai/policy.md`
   - `.ai/project-map.md`
   - `.ai/project-state.md`
   - relevant durable decisions from `.ai/decisions.md`
3. Classify the task as FAST, NORMAL, or DEEP using `.ai/config/autonomy.yaml`.
4. Load code and history lazily. Never read the whole repository by default.
5. Prefer the smallest safe implementation. Reuse existing code, platform features,
   standard libraries, and already-installed dependencies before adding new code.
6. Use branches/worktrees when isolation, risk, or parallel work justifies them.
7. Verify the result according to the likely failure mode.
8. Request independent review only when risk/complexity justifies its token cost.
9. Merge autonomously when confidence is high and no approval gate applies.
10. Record only durable knowledge. Do not preserve chain-of-thought or temporary exploration notes.
11. Communicate progress to the user in simple human language, not agent jargon.
12. If progress stalls without new evidence, stop and escalate instead of applying hacks.

## Safety gates

Always consult `.ai/config/safety.yaml`.
Never expose secrets in code, Git, documentation, prompts, or logs.
User approval is required for secret use and irreversible/external-risk actions.

## Human documentation

`docs/guide/` is for the human owner. Maintain it after meaningful architectural changes,
but do not load it into routine agent context unless the task requires it.
