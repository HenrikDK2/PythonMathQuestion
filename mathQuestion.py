from random import randint
from colors import colors


def oddOrEven():
    number = randint(1, 1000)
    numberIsOdd = number % 2 != 0
    question = f"Is {number} odd or even: "

    if(numberIsOdd):
        solution = "odd"
    else:
        solution = "even"

    while True:
        userInput = input(question)
        if(userInput == "odd" or userInput == "even"):
            return {
                "answer": userInput,
                "question": question,
                "solution": solution
            }
        else:
            print("Only odd or even")


def muliply():
    a = randint(0, 10)
    b = randint(0, 10)
    question = f"What is {a} * {b}:  "
    solution = a*b

    while True:
        userInput = input(question)
        try:
            return {
                "answer": int(userInput),
                "question": question,
                "solution": solution
            }
        except:
            print("Only numbers are allowed")


mathFunctions = [
    oddOrEven,
    muliply
]


def mathQuestion():
    return mathFunctions[randint(0, len(mathFunctions)-1)]()
