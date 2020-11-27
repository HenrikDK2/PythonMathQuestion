from colors import colors
from mathQuestion import mathQuestion
from openpyxl import Workbook
from math import floor
from random import randint

score = 0
wb = Workbook()
ws = wb.active
ws.append(["Question", "Answer", "Solution"])


def gameLoop():
    global score, wb
    result = mathQuestion()
    resultArr = [result["question"], result["answer"], result["solution"]]

    if(result["answer"] == result["solution"]):
        score += 1
        ws.append(resultArr)
        print(f"{colors.green}Correct{colors.default}, your current score: {colors.yellow+str(score)+colors.default}")
        gameLoop()
    else:
        print(colors.red+"Game Over"+colors.default)
        ws.append(resultArr)
        wb.save("data.xlsx")
        wb.close()


gameLoop()
