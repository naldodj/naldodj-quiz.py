# quiz.py

import numpy
import array
import random
import pickle

from quizgenerate import *
from os.path import exists as file_exists

if (not file_exists("quiz.npy")):
    quizgenerate()

QUESTIONS = numpy.load("quiz.npy",allow_pickle=True,fix_imports=True)

for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    random.shuffle(alternatives)
    print(f"question: {question}?")
    nIndex=64
    for alternative in alternatives:
        nIndex = nIndex + 1
        cStr=chr(nIndex)
        if (correct_answer == alternative):
            correct_answer = cStr
        print(f" {cStr}) {alternative}")

    answer = input(f"answer: ").upper()
    if answer == correct_answer:
        print("Correct!","\n")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}","\n")