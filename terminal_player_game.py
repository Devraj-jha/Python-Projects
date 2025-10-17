player = {
    'health' : 100,
    'max_health' : 100,
    'location' : 'home',
    'gold': 20,
    'inventory' : []

}

# Define the world map
world = {
    "Home": {
        "description": "You are at your home.",
        "directions": {
            "left": "Village",
            "right": "River",
            "down": "Dungeon",
            "up": "forest area"
        }
    },
    "Village": {
        "description": "You are in a small village with friendly locals.",
        "directions": {
            "right": "Home"
        }
    },
    "River": {
        "description": "You stand by a rushing river. It's too wide to cross.",
        "directions": {
            "left": "Home"
        }
    },
    "Dungeon": {
        "description": "You have entered a dark and scary dungeon.",
        "directions": {
            "up": "Home"
        }
    },
    "forest area": {
        "description": "You're in upper forest. .",
        "directions": {
            "down": "Home"
        }
    }
}

