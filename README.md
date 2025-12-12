# Roommate Survival Game (The game players based on the project)

## Overview
This project is a command-line demo game where the player lives with quirky roommates and makes daily decisions to keep the peace. Choices affect roommate relationships, stress level, and random events that change the “vibe” of the apartment. The goal is to survive the week/semester without getting kicked out or burning out.

---

## Repository Files (Purpose of Each File)

- **game.py**  
  Main playable demo. Connects relationship updates, stress updates, decision balancing, and random events into a single daily game loop.

- **update_stress_level.py**  
  Contains `update_stress_level(...)`, the stress management algorithm that updates player stress based on sleep, conflicts, and chores.

- **update_relationships.py**  
  Contains `update_relationships(...)`, the relationship dynamics algorithm that updates each roommate’s relationship score using moods, traits, the player’s action, and recent history.

- **generate_event.py**  
  Contains `generate_event(...)`, the random event generator that selects context-aware events (e.g., guests, bills, arguments, inspections).

- **decision_impact.py** (or your actual filename)  
  Contains `balance_decision_impact(...)`, the decision impact balancing algorithm that prevents “spamming” one strategy and introduces fair trade-offs.

- **group_members.txt**  
  List of group members and (optionally) roles.

---

## How to Run (Command Line)

1. Open a terminal and go into the repository folder:
   ```bash
   cd path/to/INST326_2025_FALL_group218
