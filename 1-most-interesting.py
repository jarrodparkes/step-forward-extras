import os
import random
import textwrap

# =============================================================================
# [HELPERS]
# =============================================================================
TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_PADDING = 8
LINE_WIDTH = TERMINAL_WIDTH - (TERMINAL_PADDING * 2)

wrapper = textwrap.TextWrapper(width=LINE_WIDTH)

class termMods:    
    INFO = '\033[94m'      
    SUCCESS = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def print_center(text, mods = []):
    chunks = wrapper.wrap(text)    
    for chunk in chunks:
        centered_chunk = f'{chunk}'.center(LINE_WIDTH)
        print("".join(mods) + (' ' * TERMINAL_PADDING) + centered_chunk + termMods.RESET)
    print('\n')

# =============================================================================
# [PROGRAM SPECIFIC]
# =============================================================================
questions = [
    {
        "word": "interesting", 
        "question": "In your opinion, who is the most interesting person in the world? Why?",
        "instructions": "Write a short paragraph explaining your answer.",
        "sample": "I think my wife is the most interesting person in the world. Since the day we met, I've always wanted to know more about her. Often, she makes me laugh with her amazing whit and bubbly personality.  Even though we have been together for almost 10 years, I'm still always learning new things about her.",
    }                 
]

# =============================================================================
# [MAIN]
# =============================================================================
for question in questions:
    # front matter
    os.system('clear')
    print('\n')

    # screen    
    print_center(question['word'].upper(), [termMods.BOLD, termMods.INFO])    
    print_center(question['question'], [termMods.BOLD])

    # command    
    command = input("")
    if command == 'x':
        break

    # screen    
    print_center(question['instructions'], [termMods.BOLD])    

    # command    
    command = input("")    
    if command == 'x':
        break

    # screen    
    print_center(question['sample'], [termMods.BOLD, termMods.INFO])    
    
    # command    
    command = input("")
    if command == 'x':
        break        

os.system('clear')