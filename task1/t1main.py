import random

randomList = []


# Generation of a list
def randomListGeneration():
    for i in range(50):
        randomList.append(random.randint(-100, 100))
    return checkingValues(randomList)


# Looping through list
def checkingValues(random_list):
    for i in randomList:
        if i < 0:
            print(i, "is negative.")
        elif i == 0:
            print(i, "is zero.")
        elif i > 0:
            print(i, "is positive.")


randomListGeneration()
