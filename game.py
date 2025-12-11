import random
from update_stress_level import update_stress_level
from update_relationships import update_relationships
from generate_event import generate_event
from decision_impact import balance_decision_impact  # change file name if needed


# ----------------------------------------------------------
# INITIAL GAME STATE
# ----------------------------------------------------------

roommates = {
    "Jordan": {"relationship": 60, "mood": "neutral", "traits": ["sensitive"]},
    "Riley": {"relationship": 75, "mood": "happy", "traits": ["chill"]},
    "Casey": {"relationship": 50, "mood": "tense", "traits": ["messy"]}
}

stress_level = 30

apartment_status = {
    "broken_items": [],
    "upcoming_bills": ["electricity"],
    "roommate_moods": {name: rm["mood"] for name, rm in roommates.items()}
}

history = []   # keep track of actions over time


# ----------------------------------------------------------
# SIMPLE PLAYER ACTIONS
# ----------------------------------------------------------

def choose_action():
    print("\nChoose an action:")
    print("1. Help with chores")
    print("2. Listen to a roommate")
    print("3. Ignore everyone")
    print("4. Argue with someone")

    choice = input("> ").strip()

    if choice == "1":
        return {"type": "help_chores", "target": "all", "magnitude": 1.0}
    if choice == "2":
        return {
            "type": "listen",
            "target": random.choice(list(roommates.keys())),
            "magnitude": 1.0,
        }
    if choice == "3":
        return {"type": "ignore", "target": "all", "magnitude": 1.0}
    if choice == "4":
        return {
            "type": "argue",
            "target": random.choice(list(roommates.keys())),
            "magnitude": 1.0,
        }

    print("Invalid choice — you did nothing this turn.")
    return {"type": "ignore", "target": "all", "magnitude": 1.0}


# ----------------------------------------------------------
# DISPLAY GAME STATE
# ----------------------------------------------------------

def show_status(day, stress_level, roommates):
    print("\n--------------------------------")
    print(f"DAY {day} SUMMARY")
    print("--------------------------------")
    print(f"Your stress level: {stress_level}")

    print("\nRoommate relationships:")
    for name, data in roommates.items():
        print(f"  {name}: {data['relationship']} ({data['mood']})")


# ----------------------------------------------------------
# MAIN GAME LOOP
# ----------------------------------------------------------

def play_game(days=7):
    global stress_level, roommates

    print("Welcome to the Roommate Survival Game!")
    print("Survive the next 7 days without getting kicked out or burning out.\n")

    for day in range(1, days + 1):
        print(f"\n========== DAY {day} ==========")

        # 1. Player chooses an action
        action = choose_action()
        history.append(action)

        # 2. Balance decision impact based on history + current state
        balance = balance_decision_impact(action, history, stress_level, roommates)

        # 3. Update relationships (base algorithm)
        relationships_dict = {
            name: data["relationship"] for name, data in roommates.items()
        }
        updated_relationships = update_relationships(relationships_dict, action, history)

        # Apply updated relationships
        for name in roommates:
            roommates[name]["relationship"] = updated_relationships[name]

        # Apply extra relationship deltas from balancing
        for name, delta in balance["relationship_deltas"].items():
            if name in roommates:
                roommates[name]["relationship"] += delta
                roommates[name]["relationship"] = max(
                    0, min(100, roommates[name]["relationship"])
                )

        # 4. Update stress (base algorithm)
        sleep_hours = random.randint(4, 9)
        conflicts_today = [random.randint(1, 4)] if action["type"] == "argue" else []
        chores_done = (action["type"] == "help_chores")

        stress_level = update_stress_level(
            stress=stress_level,
            sleep_hours=sleep_hours,
            conflicts=conflicts_today,
            chores_done=chores_done,
        )

        # Apply additional stress delta from balancing
        stress_level += balance["stress_delta"]
        stress_level = max(0, min(100, stress_level))

        # 5. Random event based on current state
        relationships_dict = {
            name: data["relationship"] for name, data in roommates.items()
        }
        event = generate_event(day, stress_level, relationships_dict, apartment_status)

        print(f"\nRandom Event Today: {event['event']}")
        print(event["description"])

        # 6. Show daily summary
        show_status(day, stress_level, roommates)

        # 7. Lose conditions
        if stress_level >= 100:
            print("\nYour stress hit maximum. You were unable to continue the semester.")
            return
        if any(r["relationship"] <= 0 for r in roommates.values()):
            print("\nA roommate is done with you and asks you to leave the apartment.")
            return

    print("\nYou survived the week with your roommates. Well done.")


# ----------------------------------------------------------
# START GAME
# ----------------------------------------------------------

if __name__ == "__main__":
    play_game()
