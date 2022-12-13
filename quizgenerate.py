# quizgenerate.py

import numpy
import pickle

def quizgenerate():

    QUESTIONS = {
        "Quando o brasil foi descoberto": [
            "1500","1771","1871","1881"
        ],
        "Tiradentes morreu": [
            "enforcado","dormindo","infartado","atropelado"
        ],
        "Qual brasileiro foi o maior ganhador da fórmula 1": [
            "Ayrton Senna","Nelson Piquet","Rubens Barrichelo","Rafael Câmara"
        ],
        "Quem foi eleito Presidente do Brasil em 2022": [
            "Luiz Inácio Lula da Silva",
            "Macaco Tião",
            "Luiza Erundina",
            "Jair Bolsonaro",
        ],
    }

    file = open("quiz.npy", "wb")
    numpy.save(file,list(QUESTIONS),allow_pickle=True,fix_imports=True)
    file.close
    pickle.dump(QUESTIONS,open('quiz.npy','wb'))