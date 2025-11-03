import keyboard
import time
import random

text_to_type = "write something here"

def realistic_fast_typing(text, wpm=300):
    base_delay = 60 / (wpm * 5)
    
    for char in text:
        keyboard.write(char)
        # Very small random delay for natural rhythm
        if char != ' ':  # Spacebar is instant in real typing
            time.sleep(base_delay * random.uniform(0.7, 1.3))

time.sleep(3)
realistic_fast_typing(text_to_type, wpm=700)