import random

# Define the NPC class
class NPC:
    def __init__(self, name):
        self.name = name
        self.happiness = 5
        self.trust = 5
        self.curiosity = 5
        self.action_history = []  # List to store past actions

    def apply_action(self, effects):
        """Applies the effects of an action to the NPC"""
        self.happiness += effects["happiness"]
        self.trust += effects["trust"]
        self.curiosity += effects["curiosity"]
        
    def revert_action(self, effects):
        """Reverts the effects of an action from the NPC"""
        self.happiness -= effects["happiness"]
        self.trust -= effects["trust"]
        self.curiosity -= effects["curiosity"]

    def get_status(self):
        """Returns the current status of the NPC"""
        return {"happiness": self.happiness, "trust": self.trust, "curiosity": self.curiosity}
    
    def add_action_to_history(self, action_key, time_point):
        """Adds an action to history"""
        # If we're adding an action at a time that already exists in history,
        # it means we're manipulating history - remove all actions at or after this time
        self.action_history = [a for a in self.action_history if a["time"] < time_point]
        # Add the new action
        self.action_history.append({"action": action_key, "time": time_point})
        # Sort history by time
        self.action_history.sort(key=lambda x: x["time"])
    
    def revert_to_time(self, target_time):
        """Reverts all actions after the specified time"""
        # Find actions after the target time
        actions_to_revert = [a for a in self.action_history if a["time"] > target_time]
        
        # Revert effects in reverse order
        for action_info in reversed(actions_to_revert):
            self.revert_action(Action.ACTIONS[action_info["action"]])
        
        # We don't remove actions from history here - that will be handled by add_action_to_history
        # when the new action is added at the target time
        
        return target_time

# Define actions and their effects
class Action:
    ACTIONS = {
        "Give a gift": {"happiness": 2, "trust": 1, "curiosity": 0},
        "Lie to them": {"happiness": -2, "trust": -3, "curiosity": 1},
        "Tell a secret": {"happiness": 0, "trust": 2, "curiosity": 3},
    }

    
adam = NPC("Adam")
input_map = {"G": "Give a gift", "L": "Lie to them", "T": "Tell a secret"}

time_slice = 10
current_time = 0

for time in range(1, time_slice + 1):
    current_time = time
    print(f"\nTime: {time}")
    user_input = input(f"Your action (G/L/T): ")
    
    if user_input in input_map:
        action_key = input_map[user_input]
        adam.apply_action(Action.ACTIONS[action_key])
        adam.add_action_to_history(action_key, time)
        
        print(f"{adam.name}'s status: happiness={adam.happiness}, trust={adam.trust}, curiosity={adam.curiosity}")
        print(f"Action history: {[(a['time'], a['action']) for a in adam.action_history]}")
        
        choice = input("Do you want to manipulate past? (y/n): ")
        if choice.lower() == "y":
            while True:
                try:
                    target_time = int(input(f"What time do you want to go back to? (1-{time}): "))
                    if 1 <= target_time <= time:
                        # Find the specific action at the target time
                        target_action = next((a for a in adam.action_history if a["time"] == target_time), None)
                        
                        if target_action:
                            # Revert only the specific action at target time
                            print(f"Reverting action '{target_action['action']}' at time {target_time}")
                            adam.revert_action(Action.ACTIONS[target_action['action']])
                            
                            # Apply new action at the target time
                            new_action = input("Your new action (G/L/T): ")
                            if new_action in input_map:
                                action_key = input_map[new_action]
                                # Apply the new action
                                adam.apply_action(Action.ACTIONS[action_key])
                                
                                # Update the history - replace the old action with the new one
                                for action in adam.action_history:
                                    if action["time"] == target_time:
                                        action["action"] = action_key
                                        break
                                
                                print(f"Action at time {target_time} updated to '{action_key}'")
                                print(f"New status: happiness={adam.happiness}, trust={adam.trust}, curiosity={adam.curiosity}")
                                print(f"Updated action history: {[(a['time'], a['action']) for a in adam.action_history]}")
                                print(f"Continuing to time {time+1}...")
                            break
                        else:
                            print(f"No action found at time {target_time}")
                            break
                    else:
                        print(f"Please enter a time between 1 and {time}")
                except ValueError:
                    print("Please enter a valid number")
    else:
        print("Invalid input! Please use G, L, or T.")