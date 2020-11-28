from colors import colors
from mathQuestion import mathQuestion
from openpyxl import Workbook
from random import randint

gameResults = []
score = 0


def saveData(rows):
    wb = Workbook()
    ws = wb.active
    ws.append(["Question", "Answer", "Solution"])
    [ws.append(x) for x in rows]
    wb.save("data.xlsx")
    wb.close()


while True:
    result = mathQuestion()
    gameResults.append(
        [result["question"], result["answer"], result["solution"]])

    if(result["answer"] == result["solution"]):
        score += 1
        print(f"{colors.green}Correct{colors.default}, your current score: {colors.yellow+str(score)+colors.default}")
    else:
        print(colors.red+"Game Over"+colors.default)
        break

saveData(gameResults)
