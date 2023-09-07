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
        "word": "adventurous",
        "activity": "What kind of activity would an adventurous person enjoy?",
        "person": "Who is an adventurous person? Why do you think that?"
    },
    {
        "word": "athletic",
        "activity": "What kind of activity would an athletic person enjoy?",
        "person": "Who is an athletic person? Why do you think that?"
    },
    {
        "word": "musical",
        "activity": "What kind of activity would a musical person enjoy?",
        "person": "Who is a musical person? Why do you think that?"
    },
    {
        "word": "social",
        "activity": "What kind of activity would a social person enjoy?",
        "person": "Who is a social person? Why do you think that?"
    }, 
    {
        "word": "artistic",
        "activity": "What kind of activity would an artistic person enjoy?",
        "person": "Who is an artistic person? Why do you think that?"
    },
    {
        "word": "mathematical",
        "activity": "What kind of activity would a mathematical person enjoy?",
        "person": "Who is a mathematical person? Why do you think that?"
    },
    {
        "word": "quiet",
        "activity": "What kind of activity would a quiet person enjoy?",
        "person": "Who is a quiet person? Why do you think that?"
    },
    {
        "word": "verbal",
        "activity": "What kind of activity would a verbal person enjoy?",
        "person": "Who is a verbal person? Why do you think that?"
    },                   
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
    print_center(question['activity'], [termMods.BOLD])

    # command
    print('\n')
    command = input("")
    if command == 'x':
        break

    # front matter
    os.system('clear')
    print('\n')

    # screen    
    print_center(question['word'].upper(), [termMods.BOLD, termMods.INFO])    
    print_center(question['person'], [termMods.BOLD])

    # command
    print('\n')
    command = input("")
    if command == 'x':
        break        

os.system('clear')