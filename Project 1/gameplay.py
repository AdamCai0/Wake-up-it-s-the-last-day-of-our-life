import copy

# NPCs and their attributes
npcs = {
    "ZTR": {"familiarity": 0, "trust": 0, "impression": 0},
    "Emma": {"familiarity": 0, "trust": 0, "impression": 0},
    "Mr. K": {"familiarity": 0, "trust": 0, "impression": 0},
    "YL": {"familiarity": 0, "trust": 0, "impression": 0},
    "Ms. H": {"familiarity": 0, "trust": 0, "impression": 0},
}

# Log for time slices
time_log = [{} for _ in range(30)]  # 30 time slices, each storing actions and their effects

# Major decisions and their impacts
def major_decision_1(npcs):
    npcs["ZTR"]["familiarity"] += 5
    npcs["ZTR"]["trust"] += 3
    return "You confessed your love to ZTR."

def major_decision_2(npcs):
    npcs["Emma"]["trust"] -= 5
    npcs["YL"]["impression"] += 2
    return "You spread a rumor about Emma."

def major_decision_3(npcs):
    npcs["Mr. K"]["familiarity"] += 4
    npcs["Ms. H"]["trust"] += 2
    return "You helped Mr. K and Ms. H."

def major_decision_4(npcs):
    npcs["YL"]["familiarity"] += 6
    return "You went on a date with YL."

def major_decision_5(npcs):
    npcs["Ms. H"]["trust"] += 3
    npcs["Ms. H"]["familiarity"] += 2
    return "You moved to Canada to meet Ms. H."

# Map decisions to functions
decisions = {
    5: major_decision_1,
    10: major_decision_2,
    15: major_decision_3,
    20: major_decision_4,
    25: major_decision_5,
}

# Replay function
def replay(start_time):
    # Reset NPC attributes
    for npc in npcs.values():
        npc["familiarity"] = npc["trust"] = npc["impression"] = 0

    # Reapply decisions from the log
    for t in range(start_time):
        if time_log[t]:
            decision_func = time_log[t]["decision"]
            decision_func(npcs)

# Main game loop
for current_time in range(30):
    print(f"\nTime Slice {current_time + 1}")

    # Check if this time slice has a decision
    if current_time + 1 in decisions:
        print("A major decision is available!")
        print(f"Current stats: {npcs}")
        choice = input("Do you want to make this decision? (yes/no): ").strip().lower()
        if choice == "yes":
            result = decisions[current_time + 1](npcs)
            time_log[current_time] = {"decision": decisions[current_time + 1]}
            print(result)
        else:
            print("You skipped this decision.")

    # Ask if the player wants to change the past
    change = input("Do you want to change a past decision? (yes/no): ").strip().lower()
    if change == "yes":
        past_time = int(input("Enter the time slice (1-30) you want to revisit: ")) - 1
        if 0 <= past_time < 30 and time_log[past_time]:
            print(f"Revisiting Time Slice {past_time + 1}.")
            print(f"Current stats: {npcs}")
            replay(past_time)  # Replay decisions from the start to the present
        else:
            print("Invalid time slice or no decision made at that time.")

    # Display updated stats
    print(f"NPC stats after Time Slice {current_time + 1}: {npcs}")

# Final Results
print("\nGame Over! Final NPC stats:")
for npc, attributes in npcs.items():
    print(f"{npc}: {attributes}")

print("\nDecision Log:")
for t, entry in enumerate(time_log):
    if entry:
        print(f"Time Slice {t + 1}: {entry['decision'].__name__}")
