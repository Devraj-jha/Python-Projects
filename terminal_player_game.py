
# SIMPLE TEXT ADVENTURE GAME
# A beginner-friendly Python program that teaches programming basics

# Line 1-3: Import statements - bringing in pre-made code we need
import random
import time

# Line 5-10: Game setup - variables that store our game state
player_health = 100
player_gold = 50
inventory = ["sword", "health potion"]
current_room = "forest"

# Line 12-20: Game locations - a dictionary that maps places to descriptions
locations = {
    "forest": "You are in a dark forest. Paths lead north and east.",
    "cave": "You are in a damp cave. It's dark and mysterious.",
    "village": "You are in a peaceful village. People are going about their day.",
    "river": "You are by a flowing river. The water looks clean and fresh."
}

# Line 22-30: Room connections - which rooms connect to which others
connections = {
    "forest": {"north": "cave", "east": "village"},
    "cave": {"south": "forest", "east": "river"},
    "village": {"west": "forest", "north": "river"},
    "river": {"west": "cave", "south": "village"}
}

# Line 32-40: Function to display game status
def show_status():
    """Shows the player's current stats and location"""
    print(f"\n--- Your Status ---")
    print(f"Health: {player_health}")
    print(f"Gold: {player_gold}")
    print(f"Location: {current_room}")
    print(f"Inventory: {', '.join(inventory)}")
    print("-" * 20)

# Line 42-55: Function to handle moving between rooms
def move(direction):
    """Moves the player in the specified direction if possible"""
    global current_room  # This lets us change the variable outside the function
    
    if direction in connections[current_room]:
        current_room = connections[current_room][direction]
        print(f"\nYou move {direction} to the {current_room}.")
        print(locations[current_room])
        return True
    else:
        print(f"\nYou can't go {direction} from here!")
        return False

# Line 57-75: Function to handle random encounters
def random_encounter():
    """Random events that can happen when moving"""
    global player_health, player_gold, inventory
    
    # 30% chance of an encounter
    if random.random() < 0.3:
        encounter_type = random.choice(["treasure", "monster", "nothing"])
        
        if encounter_type == "treasure":
            gold_found = random.randint(5, 20)
            player_gold += gold_found
            print(f"\n*** You found {gold_found} gold coins! ***")
            
        elif encounter_type == "monster":
            damage = random.randint(10, 25)
            player_health -= damage
            print(f"\n*** A monster attacks you for {damage} damage! ***")
            
        else:
            print(f"\nYou travel safely. Nothing happens.")

# Line 77-95: Function to handle shopping
def visit_shop():
    """Lets the player buy items if they're in the village"""
    global player_gold, inventory
    
    if current_room == "village":
        print("\n=== VILLAGE SHOP ===")
        print("1. Health Potion - 20 gold")
        print("2. Better Sword - 50 gold")
        print("3. Leave shop")
        
        choice = input("What would you like to buy? (1-3): ")
        
        if choice == "1" and player_gold >= 20:
            player_gold -= 20
            inventory.append("health potion")
            print("You bought a health potion!")
            
        elif choice == "2" and player_gold >= 50:
            player_gold -= 50
            # Replace the old sword with a better one
            if "sword" in inventory:
                inventory.remove("sword")
            inventory.append("magic sword")
            print("You bought a magic sword!")
            
        elif choice == "3":
            print("You leave the shop.")
        else:
            print("You can't afford that or invalid choice!")

# Line 97-100: Function to use items from inventory
def use_item():
    """Lets the player use items from their inventory"""
    global player_health
    
    if not inventory:
        print("Your inventory is empty!")
        return
        
    print(f"\nYour inventory: {', '.join(inventory)}")
    item = input("Which item would you like to use? ").lower()
    
    if item in inventory:
        if item == "health potion":
            player_health += 30
            if player_health > 100:
                player_health = 100
            inventory.remove("health potion")
            print("You used a health potion and gained 30 health!")
        else:
            print(f"You can't use the {item} right now.")
    else:
        print("You don't have that item!")

# Line 125-150: Main game loop
def main():
    """The main function that runs the game"""
    print("=== WELCOME TO THE TEXT ADVENTURE GAME ===")
    print("You wake up in a forest with no memory...")
    print("Type 'help' for commands")
    
    # Game continues until player health reaches 0
    while player_health > 0:
        show_status()
        
        # Get player input
        command = input("\nWhat would you like to do? ").lower()
        
        # Process commands
        if command in ["north", "south", "east", "west"]:
            if move(command):
                random_encounter()
                
        elif command == "look":
            print(f"\n{locations[current_room]}")
            
        elif command == "shop":
            visit_shop()
            
        elif command == "use":
            use_item()
            
        elif command == "help":
            print("\n=== COMMANDS ===")
            print("north/south/east/west - Move in that direction")
            print("look - Look around your current location")
            print("shop - Visit the village shop (only in village)")
            print("use - Use an item from your inventory")
            print("help - Show this help message")
            print("quit - Exit the game")
            
        elif command == "quit":
            print("Thanks for playing!")
            break
            
        else:
            print("I don't understand that command. Type 'help' for options.")
        
        # Small delay to make the game feel better
        time.sleep(1)
    
    # Game over message
    if player_health <= 0:
        print("\n*** GAME OVER ***")
        print("You have been defeated...")

# Line 175: This starts the game when the file is run
if __name__ == "__main__":
    main()