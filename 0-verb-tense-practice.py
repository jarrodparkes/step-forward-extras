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
tenses = [
    {
        "name": 'present simple',
        "example": 'I study English in the morning as soon as I wake up.',
        "prompt": "When do you study English?"
    },
    {
        "name": 'present continuous',
        "example": 'Right now, I\'m rewatching "The Office" for the third time.',
        "prompt": "Are you currently watching any shows?"
    },
    {
        "name": 'present perfect',
        "example": 'Yes. I\'ve been to New York.',
        "prompt": "Have you been to _________?"
    },    
    {
        "name": 'past simple',
        "example": 'Yesterday, I watched employee training videos for my new job.',
        "prompt": 'What did you do yesterday?'
    },
    {
        "name": 'past continuous',
        "example": 'I was probably riding bikes and playing video games with my friends.',
        "prompt": 'What were you doing at this time, twenty years ago?'
    },
    {
        "name": 'future',
        "example": 'Tomorrow, I will hang out with some friends.',
        "prompt": 'What will you do tomorrow?',
        "hint": '"Will" and "going to" are used interchangeably in casual speech. But, in writing, "will" is more commonly used with recent decisions, certain futures, and predictions. "Going to" is typically used for previously determined events.'
    },
]

# =============================================================================
# [MAIN]
# =============================================================================
for tense in tenses:
    # front matter
    os.system('clear')
    print('\n')

    # screen    
    print_center(tense['name'].upper(), [termMods.BOLD, termMods.INFO])    
    print_center(tense['prompt'], [termMods.BOLD])    
    print_center("Ex: " + tense['example'])    

    # hint
    if ('hint' in tense):        
        command = input("")
        print_center(tense['hint'], [termMods.BOLD])

    # command
    print('\n')
    command = input("")
    if command == 'x':
        break

os.system('clear')