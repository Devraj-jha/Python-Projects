#!/usr/bin/env python3
"""
Text-Based Adventure Game - "The Mysterious Castle"
Demonstrates core Python concepts including:
- Variables and data types
- Control structures (if/else, loops)
- Functions
- Classes and OOP
- Error handling
- File I/O
- List/dictionary comprehensions
- Decorators
- Generators
- Context managers
"""

import random
import time
import json
from datetime import datetime
from typing import Dict, List, Optional

# =============================================================================
# DECORATORS - For adding functionality to methods
# =============================================================================

def game_logger(func):
    """Decorator to log game events"""
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} executed at {datetime.now().strftime('%H:%M:%S')}")
        return result
    return wrapper

def require_item(item_name: str):
    """Decorator to check if player has required item"""
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            if item_name in self.inventory:
                return func(self, *args, **kwargs)
            else:
                print(f"You need {item_name} to do that!")
                return False
        return wrapper
    return decorator

# =============================================================================
# CLASSES - Object Oriented Programming
# =============================================================================

class Player:
    """Player class to manage player state"""
    
    def __init__(self, name: str):
        self.name = name
        self.health = 100
        self.inventory = ["torch", "map"]
        self.location = "entrance"
        self.score = 0
        self._secret_code = random.randint(1000, 9999)  # Private attribute
        
    def __str__(self) -> str:
        return f"Player {self.name} (Health: {self.health}, Score: {self.score})"
    
    def __repr__(self) -> str:
        return f"Player(name='{self.name}', health={self.health})"
    
    @property
    def is_alive(self) -> bool:
        """Property to check if player is alive"""
        return self.health > 0
    
    @game_logger
    def take_damage(self, damage: int) -> bool:
        """Method to handle player taking damage"""
        self.health = max(0, self.health - damage)
        print(f"Ouch! You took {damage} damage. Health: {self.health}")
        return self.is_alive
    
    def heal(self, amount: int) -> None:
        """Method to heal player"""
        self.health = min(100, self.health + amount)
        print(f"Restored {amount} health. Current health: {self.health}")
    
    def add_item(self, item: str) -> None:
        """Add item to inventory"""
        if item not in self.inventory:
            self.inventory.append(item)
            print(f"Added {item} to inventory!")
    
    def remove_item(self, item: str) -> bool:
        """Remove item from inventory"""
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        return False

class Room:
    """Room class to represent different locations"""
    
    def __init__(self, name: str, description: str, items: List[str] = None, 
                 connections: Dict[str, str] = None, puzzle: str = None):
        self.name = name
        self.description = description
        self.items = items if items else []
        self.connections = connections if connections else {}
        self.puzzle = puzzle
        self.visited = False
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}"
    
    def describe(self) -> str:
        """Generate room description"""
        base_desc = f"\n=== {self.name.upper()} ===\n{self.description}"
        
        if self.items:
            base_desc += f"\nYou see: {', '.join(self.items)}"
        
        if self.connections:
            base_desc += f"\nExits: {', '.join(self.connections.keys())}"
        
        if not self.visited:
            base_desc += "\n* This place feels unfamiliar *"
            self.visited = True
            
        return base_desc

class Game:
    """Main game class"""
    
    def __init__(self):
        self.player = None
        self.rooms = self._create_rooms()
        self.game_active = False
        self.actions_taken = 0
        
    def _create_rooms(self) -> Dict[str, Room]:
        """Create game rooms using dictionary comprehension"""
        room_data = {
            "entrance": {
                "description": "You stand before a massive castle gate. Cold wind howls through the ancient stones.",
                "items": ["key"],
                "connections": {"north": "great_hall", "east": "garden"}
            },
            "great_hall": {
                "description": "A vast hall with towering ceilings. Tattered banners hang from the walls.",
                "items": ["sword", "potion"],
                "connections": {"south": "entrance", "west": "library", "east": "dungeon"},
                "puzzle": "riddle"
            },
            "library": {
                "description": "Dusty books line the walls from floor to ceiling. A single candle flickers on a desk.",
                "items": ["ancient book", "candle"],
                "connections": {"east": "great_hall"},
                "puzzle": "books"
            },
            "dungeon": {
                "description": "Dark, damp cells line the corridor. The air smells of decay and rust.",
                "items": ["bone key"],
                "connections": {"west": "great_hall", "north": "treasure_room"}
            },
            "garden": {
                "description": "An overgrown courtyard with a mysterious fountain in the center.",
                "items": ["herbs", "gold coin"],
                "connections": {"west": "entrance"}
            },
            "treasure_room": {
                "description": "A glittering room filled with gold, jewels, and ancient artifacts!",
                "items": ["crown", "treasure chest"],
                "connections": {"south": "dungeon"}
            }
        }
        
        # Dictionary comprehension to create Room objects
        return {name: Room(name, **data) for name, data in room_data.items()}
    
    # =============================================================================
    # GENERATOR - For creating sequences
    # =============================================================================
    
    def item_generator(self, room_name: str):
        """Generator that yields items from a room one by one"""
        room = self.rooms[room_name]
        for item in room.items:
            yield item
            time.sleep(0.5)  # Small delay for dramatic effect
    
    # =============================================================================
    # CONTEXT MANAGER - For resource management
    # =============================================================================
    
    class GameSaver:
        """Context manager for saving game state"""
        
        def __init__(self, filename: str, game_data: dict):
            self.filename = filename
            self.game_data = game_data
        
        def __enter__(self):
            return self
        
        def __exit__(self, exc_type, exc_val, exc_tb):
            if exc_type is None:
                with open(self.filename, 'w') as f:
                    json.dump(self.game_data, f)
                print(f"Game saved to {self.filename}")
            return False
    
    # =============================================================================
    # GAME METHODS
    # =============================================================================
    
    def start_game(self) -> None:
        """Initialize and start the game"""
        print("Welcome to THE MYSTERIOUS CASTLE!")
        name = input("Enter your name, brave adventurer: ").strip()
        
        # Input validation
        while not name:
            name = input("Please enter a valid name: ").strip()
        
        self.player = Player(name)
        self.game_active = True
        
        print(f"\nGreetings, {self.player.name}! Your adventure begins...")
        print("Type 'help' for commands\n")
        
        self._show_location()
    
    @game_logger
    def _show_location(self) -> None:
        """Display current location description"""
        current_room = self.rooms[self.player.location]
        print(current_room.describe())
    
    def _handle_puzzle(self, room: Room) -> bool:
        """Handle room puzzles"""
        if room.puzzle == "riddle":
            print("\nA ghostly figure appears and asks: 'I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?'")
            answer = input("Your answer: ").lower().strip()
            
            if answer == "echo":
                print("Correct! The ghost vanishes, leaving behind a glowing orb.")
                room.items.append("glowing orb")
                self.player.score += 50
                return True
            else:
                print("Wrong! The ghost wails and disappears.")
                return False
                
        elif room.puzzle == "books":
            print("\nThe books are arranged in a strange order. Can you find the pattern?")
            # List comprehension to create book titles
            books = [f"Book {chr(65 + i)}" for i in range(5)]
            print("Books:", ", ".join(books))
            return True
            
        return True
    
    @require_item("key")
    def _unlock_door(self) -> bool:
        """Example of using decorator to require items"""
        print("You use the key to unlock a mysterious door!")
        self.player.score += 20
        return True
    
    def process_command(self, command: str) -> bool:
        """Process player commands"""
        self.actions_taken += 1
        cmd_parts = command.lower().split()
        
        if not cmd_parts:
            return True
        
        action = cmd_parts[0]
        
        try:
            if action in ["quit", "exit"]:
                self.game_active = False
                print("Thanks for playing!")
                return False
                
            elif action == "help":
                self._show_help()
                
            elif action == "look":
                self._show_location()
                
            elif action == "inventory":
                self._show_inventory()
                
            elif action == "health":
                print(f"Your health: {self.player.health}")
                
            elif action == "score":
                print(f"Your score: {self.player.score}")
                
            elif action == "move" and len(cmd_parts) > 1:
                self._move_player(cmd_parts[1])
                
            elif action == "take" and len(cmd_parts) > 1:
                self._take_item(' '.join(cmd_parts[1:]))
                
            elif action == "use" and len(cmd_parts) > 1:
                self._use_item(' '.join(cmd_parts[1:]))
                
            elif action == "save":
                self._save_game()
                
            elif action == "explore":
                self._explore_room()
                
            else:
                print("Unknown command. Type 'help' for available commands.")
                
        except Exception as e:
            print(f"Something went wrong: {e}")
            
        return True
    
    def _show_help(self) -> None:
        """Display help information"""
        help_text = """
Available Commands:
- look: Describe current location
- move [direction]: Move in specified direction (north, south, east, west)
- take [item]: Pick up an item
- use [item]: Use an item from inventory
- inventory: Show your inventory
- health: Check your health
- score: Check your score
- explore: Examine room carefully
- save: Save game progress
- quit: Exit game
"""
        print(help_text)
    
    def _move_player(self, direction: str) -> None:
        """Move player to different room"""
        current_room = self.rooms[self.player.location]
        
        if direction in current_room.connections:
            new_location = current_room.connections[direction]
            self.player.location = new_location
            
            # Random encounter - 30% chance
            if random.random() < 0.3:
                self._random_encounter()
                
            self._show_location()
            
            # Handle room puzzle if exists
            new_room = self.rooms[new_location]
            if new_room.puzzle and not new_room.visited:
                self._handle_puzzle(new_room)
        else:
            print(f"You cannot go {direction} from here!")
    
    def _take_item(self, item: str) -> None:
        """Take item from current room"""
        current_room = self.rooms[self.player.location]
        
        if item in current_room.items:
            current_room.items.remove(item)
            self.player.add_item(item)
            self.player.score += 10
        else:
            print(f"{item} is not here!")
    
    def _use_item(self, item: str) -> None:
        """Use item from inventory"""
        if item == "potion" and item in self.player.inventory:
            self.player.heal(30)
            self.player.remove_item("potion")
        elif item == "key" and item in self.player.inventory:
            self._unlock_door()
        else:
            print(f"You cannot use {item} right now.")
    
    def _show_inventory(self) -> None:
        """Display player inventory"""
        if self.player.inventory:
            print("Inventory:", ", ".join(self.player.inventory))
        else:
            print("Your inventory is empty.")
    
    def _random_encounter(self) -> None:
        """Handle random encounters"""
        encounters = [
            ("A bat flies into your face!", 5),
            ("You trip on a loose stone!", 10),
            ("A ghostly chill runs through you!", 15),
            ("You find a healing herb!", -20),  # Negative damage = healing
        ]
        
        encounter, damage = random.choice(encounters)
        print(f"\n*** RANDOM ENCOUNTER ***")
        print(encounter)
        
        if damage > 0:
            self.player.take_damage(damage)
        else:
            self.player.heal(abs(damage))
    
    def _explore_room(self) -> None:
        """Thoroughly explore current room using generator"""
        current_room = self.rooms[self.player.location]
        print(f"Carefully exploring {current_room.name}...")
        
        item_gen = self.item_generator(self.player.location)
        
        for i, item in enumerate(item_gen, 1):
            print(f"Found: {item}")
            
        if not current_room.items:
            print("Nothing else of interest here.")
    
    def _save_game(self) -> None:
        """Save game state using context manager"""
        game_data = {
            'player_name': self.player.name,
            'health': self.player.health,
            'inventory': self.player.inventory,
            'location': self.player.location,
            'score': self.player.score,
            'actions_taken': self.actions_taken
        }
        
        filename = f"castle_adventure_{self.player.name.lower()}.json"
        
        try:
            with self.GameSaver(filename, game_data) as saver:
                print("Saving game data...")
        except Exception as e:
            print(f"Failed to save game: {e}")

# =============================================================================
# MAIN GAME LOOP
# =============================================================================

def main():
    """Main function to run the game"""
    game = Game()
    game.start_game()
    
    # Main game loop
    while game.game_active and game.player.is_alive:
        try:
            command = input("\nWhat would you like to do? ").strip()
            game.process_command(command)
            
            # Check for win condition
            if (game.player.location == "treasure_room" and 
                "treasure chest" in game.player.inventory):
                print("\n🎉 CONGRATULATIONS! You found the treasure and won the game! 🎉")
                print(f"Final Score: {game.player.score}")
                break
                
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            break
        except EOFError:
            print("\n\nUnexpected end of input. Game over!")
            break
    
    if not game.player.is_alive:
        print("\n💀 You have died! Game Over!")
    
    print(f"\nGame Statistics:")
    print(f"Final Score: {game.player.score}")
    print(f"Actions Taken: {game.actions_taken}")
    print(f"Items Collected: {len(game.player.inventory)}")

if __name__ == "__main__":
    main()