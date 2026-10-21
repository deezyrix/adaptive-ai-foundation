# Skill: Verify

Match verification to the failure mode.

Examples:
- parser: representative valid/invalid files
- web app: launch, browser flow, console/network errors
- bot/API: command/request flow, logs, sandbox/mocks when appropriate
- binary reader: known samples, offsets, corrupt input

Add automated tests only when they materially reduce regression risk.
Never declare done without evidence.
