import os
import random

exercises = [
    {
        "word": "succeed",
        "question": "Practice and patience are the keys to ______.",
        "answer": "success (noun)",
        "final": "Practice and patience are the keys to success."
    },
    {
        "word": "rely",
        "question": "My best friend never lets me down. I ______ on her all the time.",
        "answer": "rely (verb)",
        "final": "My best friend never lets me down. I rely on her all the time."
    },
    {
        "word": "differ",
        "question": "I can't see what's ______ in the second version of this document.",
        "answer": "different (adjective)",
        "final": "I can't see what's different in the second version of this document."
    },
    {
        "word": "act",
        "question": "______ speak louder than words.",
        "answer": "actions (noun)",
        "final": "Actions speak louder than words."
    },
    {
        "word": "apologize",
        "question": "After tripping me on my way to my desk yesterday, my coworker ______ profusely.",
        "answer": "apologized (verb)",
        "final": "After tripping me on my way to my desk yesterday, my coworker apologized profusely."
    },
    {
        "word": "identify",
        "question": "Please show me your ______ and your insurance papers.",
        "answer": "identification (noun)",
        "final": "Please show me your identification and your insurance papers."
    },
    {
        "word": "understand",
        "question": "He was ______ upset when he heard about the accident.",
        "answer": "understandably (adverb)",
        "final": "He was understandably upset when he heard about the accident."
    },
    {
        "word": "divide",
        "question": "There were so many ______ issues that they called a mediator in.",
        "answer": "divisive (adjective)",
        "final": "There were so many divisive issues that they called a mediator in."
    },
    {
        "word": "decide",
        "question": "Because the manager reacted ______, the problem didn't spiral out of control.",
        "answer": "decisively (adverb)",
        "final": "Because the manager reacted decisively , the problem didn't spiral out of control."
    },
    {
        "word": "benefit",
        "question": "This document was a ______ resource for the project.",
        "answer": "beneficial (adjective)",
        "final": "This document was a beneficial resource for the project."
    }
]

for exercise in exercises:      
    os.system('clear')
    print(f'PROMPT: {exercise["question"]}')
    print(f'EXERCISE: Complete the sentence using a word in the \"{exercise["word"]}\" word family.')
    input('')
    print(f'ANSWER: {exercise["answer"]}')
    print(f'FINAL: {exercise["final"]}\n')
    input('')