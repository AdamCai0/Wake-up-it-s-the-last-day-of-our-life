import json
import random
import time

def load_game_data():
    with open('Project 1/game_data.json', 'r') as file:
        return json.load(file)

def display_dialogue(dialogue):
    for line in dialogue:
        print(line)
        input()  # Wait for enter key
        
def play_scene(game_data, current_scene):
    scene = game_data['scenes'][current_scene]
    
    # Display the scene's dialogue
    if 'dialogue' in scene:
        display_dialogue(scene['dialogue'])
    
    # Handle the next step based on scene type
    if 'next_choice' in scene:
        # Scene requires player choice
        choice = None
        while choice not in scene['next_choice']['options']:
            print(scene['next_choice']['prompt'])
            choice = input().lower()
        return scene['next_choice']['options'][choice]
    
    elif 'outcomes' in scene:
        # Scene has random outcomes
        outcome = random.random()
        for outcome_name, outcome_data in scene['outcomes'].items():
            if outcome <= outcome_data['probability']:
                return outcome_data['next']
            outcome -= outcome_data['probability']
        # If we get here, return the last outcome as default
        return list(scene['outcomes'].values())[-1]['next']
    
    elif 'next' in scene:
        # Scene has a direct next scene
        return scene['next']
    
    return None  # End of game

def main():
    print("Loading game...")
    game_data = load_game_data()
    
    print(f"Welcome to {game_data['game_title']}!")
    time.sleep(1)
    
    current_scene = game_data['initial_state']['starting_scene']
    
    while current_scene:
        current_scene = play_scene(game_data, current_scene)
        
    print("Game Over")

if __name__ == "__main__":
    main() 