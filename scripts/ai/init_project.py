from pathlib import Path
from datetime import date

root = Path(__file__).resolve().parents[2]

project_map = root / ".ai" / "project-map.md"
project_state = root / ".ai" / "project-state.md"

print("Adaptive AI Development Foundation")
print("----------------------------------")
print("Repository:", root)
print()
print("Next step:")
print("1. Initialize Git if needed.")
print("2. Give your coding agent access to this repository.")
print("3. Tell the agent to read AGENTS.md.")
print("4. Describe the product you want to build.")
print()
print("The agent should initialize project-map/state as the architecture becomes real.")
