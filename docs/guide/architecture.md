# Architecture

Last verified against: not initialized

## Overview

Not initialized yet.

## Diagram

```mermaid
flowchart TD
    U[User Intent] --> O[AI Orchestrator]
    O --> C[Minimal Context]
    C --> M{FAST / NORMAL / DEEP}
    M --> I[Implementation]
    I --> V[Verification]
    V --> R{Enough confidence?}
    R -->|Yes| G[Merge / Record]
    R -->|No| E[Retry with new evidence or escalate]
```
