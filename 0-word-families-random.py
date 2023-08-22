import os
import random

families = [
    {
        "verb": "act",
        "noun": "action",
        "adjective": "active",
        "adverb": "actively" 
    },
    {
        "verb": "apologize",
        "noun": "apology",
        "adjective": "apologetic",
        "adverb": "apologetically" 
    },
    {
        "verb": "beautify",
        "noun": "beauty",
        "adjective": "beautiful",
        "adverb": "beautifully" 
    },
    {
        "verb": "believe",
        "noun": "belief",
        "adjective": "believable",
        "adverb": "believably" 
    }, 
    {
        "verb": "benefit",
        "noun": "benefit",
        "adjective": "beneficial",
        "adverb": "beneficially"
    },
    {
        "verb": "care",
        "noun": "care",
        "adjective": "careful",
        "adverb": "carefully"
    }, 
    {
        "verb": "create",
        "noun": "creation",
        "adjective": "creative",
        "adverb": "creatively"
    },
    {
        "verb": "decide",
        "noun": "decision",
        "adjective": "decisive",
        "adverb": "decisively"
    }, 
    {
        "verb": "differ",
        "noun": "difference",
        "adjective": "different",
        "adverb": "differently"
    }, 
    {
        "verb": "divide",
        "noun": "division",
        "adjective": "divisive",
        "adverb": "divisively"
    },
    {
        "verb": "exclude",
        "noun": "exclusion",
        "adjective": "exclusive",
        "adverb": "exclusively"
    }, 
    {
        "verb": "identify",
        "noun": "identification",
        "adjective": "identifiable",
        "adverb": "identifiably"
    },
    {
        "verb": "justify",
        "noun": "justification or justice",
        "adjective": "justifiable",
        "adverb": "justifiably"
    }, 
    {
        "verb": "protect",
        "noun": "protection",
        "adjective": "protective",
        "adverb": "protectively"
    }, 
    {
        "verb": "rely",
        "noun": "reliability",
        "adjective": "reliable",
        "adverb": "reliably"
    },
    {
        "verb": "signify",
        "noun": "significance",
        "adjective": "significant",
        "adverb": "significantly"
    },
    {
        "verb": "succeed",
        "noun": "success",
        "adjective": "successful",
        "adverb": "successfully"
    },
    {
        "verb": "tolerate",
        "noun": "tolerance",
        "adjective": "tolerable",
        "adverb": "tolerably"
    },
    {
        "verb": "understand",
        "noun": "understanding",
        "adjective": "understandable",
        "adverb": "understandably"
    },
]

members = [
    'verb',
    'noun',
    'adjective',
    'adverb',
]

while(True):
    os.system('clear')
    family = random.choice(families)
    member = random.choice(members)
    print(f'PROMPT: Your word family is \"{family["verb"]}\":\n')
    print(f'verb\t\t=>\t\t{family["verb"]}')
    print(f'noun\t\t=>\t\t{family["noun"]}')
    print(f'adjective\t=>\t\t{family["adjective"]}')
    print(f'adverb\t\t=>\t\t{family["adverb"]}\n')
    print(f'EXERCISE: Please use the {member}-form to create a sentence.\n')
    input('')