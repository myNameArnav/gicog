from datetime import timedelta, date
from alphabetMatrix import getAlphabetMatrix


def getDaysToCommit(todayDate: str) -> dict:
    matrix = getAlphabetMatrix()
    dateGrid = []
    commitGrid = []
    noOfWeeks = 0
    addDays = 0
    sentence = "Hello World"

    # if week day is anything else than sunday then go to next sunday
    delta = 6 - todayDate.weekday()
    startDate = todayDate + timedelta(days=delta)

    # Adding empty week when space is present
    for alphabet in sentence.upper():
        if alphabet != " ":
            noOfWeeks += 5
            commitGrid.append(matrix[alphabet])
        else:
            noOfWeeks += 1
            alphabet = "SPACE"
            commitGrid.append(matrix[alphabet])

    # flattening the list
    commitGrid = [item for sublist in commitGrid for item in sublist]

    for week in range(noOfWeeks):
        subGrid = []
        for day in range(7):
            temp = []
            temp.append((startDate + timedelta(days=addDays)).strftime("%Y-%m-%d"))
            subGrid.append(temp)
            addDays += 1
        dateGrid.append(subGrid)

    mergedGrid = {}
    for count, dates in enumerate(dateGrid):
        for count2, date in enumerate(dates):
            dictDate = date[0]
            dictIsCommit = commitGrid[count][count2]

            mergedGrid[dictDate] = dictIsCommit

    return mergedGrid
