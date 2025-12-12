# Roommate Survival Game (The game players based on the project)

## Overview
This project is a command-line demo game where the player lives with quirky roommates and makes daily decisions to keep the peace. Choices affect roommate relationships, stress level, and random events that change the “vibe” of the apartment. The goal is to survive the week/semester without getting kicked out or burning out.

---

## Repository Files (Purpose of Each File)
- **game.py**  
  Main playable demo. Connects relationship updates, stress updates, decision balancing, and
  random events into a single daily game loop.

- **update_stress_level.py**  
  Contains `update_stress_level(...)`, the stress management algorithm that updates player stress
  based on sleep, conflicts, and chores.

- **update_relationships.py**  
  Contains `update_relationships(...)`, the relationship dynamics algorithm that updates each
  roommate’s relationship score using moods, traits, the player’s action, and recent history.

- **generate_event.py**  
  Contains `generate_event(...)`, the random event generator that selects context-aware events
  (e.g., guests, bills, arguments).

- **decision_impact.py**  
  Contains `balance_decision_impact(...)`, the decision impact balancing algorithm that prevents
  repeatedly using the same strategy and introduces fair trade-offs.

- **group_members.txt**  
  List of group members.


## How to Run (Command Line)

1. Open a terminal and go into the repository folder:
   ```bash
   cd path/to/INST326_2025_FALL_group218

### Game Setup
When the game starts, you will be prompted to enter:
- Your **player name**
- Names for **each roommate**

These names will be used throughout the game for relationship tracking and events.

---

### Daily Actions
Each in-game day, choose **one action** by entering the corresponding number:

1. Help with chores  
2. Listen to a roommate  
3. Ignore everyone  
4. Argue with someone  

Your choice affects stress, roommate relationships, and future events.

---

### What Happens Each Day
After each action:

- Your **stress level** is updated (range: 0–100)
- Each roommate’s **relationship score** is updated (range: 0–100)
- Each roommate’s **mood** is displayed as:
  - **tense** (low relationship)
  - **neutral** (medium relationship)
  - **happy** (high relationship)
- A **random event** may occur and influence the day

A daily summary is printed showing the current game state.

---

### Win and Lose Conditions
The game ends if:
- Your stress level reaches **100** (burnout), or
- Any roommate’s relationship reaches **0** (you are kicked out)

You **win** if you survive all days without losing.
## Interpreting the Output

- **Stress Level**  
  Represents the player’s mental and emotional state. Higher stress limits success and can end the game if it reaches 100.

- **Relationship Score**  
  Indicates how each roommate feels about the player. Low relationship scores increase tension and may result in being kicked out.

- **Mood**  
  A readable summary of each roommate’s emotional state:
  - **tense** indicates a poor relationship
  - **neutral** indicates a stable relationship
  - **happy** indicates a strong relationship

- **Random Events**  
  Narrative events that add unpredictability and consequences. Events may affect stress levels, relationships, or future gameplay.

  ## Annotated Bibliography

1. Maxis. *The Sims* (Video Game Series). Electronic Arts.  
   The Sims series served as conceptual inspiration for this project, particularly in modeling
   relationship dynamics, mood states, stress management, and everyday decision-making within a
   shared living environment. The idea of balancing social interactions, personal well-being, and
   household harmony over time influenced the design of the roommate relationship system, mood
   thresholds, and random life events in the Roommate Survival Game. No code, assets, or proprietary
   mechanics from The Sims were used; it was referenced only as a high-level design and gameplay
   inspiration.  
   Official website: https://www.ea.com/games/the-sims
## Attribution Table

| Method/function | Primary author | Techniques demonstrated |
|-----------------|----------------|--------------------------|
| update_stress_level | Nathaniel Mekonnen | clamping; iteration over list |
| update_relationships | Sean Nehrebecky | dictionary iteration; trait-based modifiers |
| generate_event | Miguel Saagong | lambda triggers; filtering list |
| balance_decision_impact | Yawo Tchatchou | pattern detection over a sliding window |

