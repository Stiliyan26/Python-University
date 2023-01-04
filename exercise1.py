import functools
from operator import index

def inputValidator(inputMsg, errMsg, isPositive):
    while True:
        try:
            number = int(input(inputMsg))
            if isPositive:
                if number <= 0:
                    raise Exception(errMsg)
                return number
            return number
        except ValueError:
            print("Value type is incorrect")
        except Exception as e:
            print(e)

n = inputValidator('Enter number n: ', 'Invalid number n!', True)
k = inputValidator('Enter number k: ', 'Invalid number k!', True)

firstList = []
secondList = []

for i in range(n):
    currentNum = inputValidator('Enter number: ', 'Invalid number!', False)
    if currentNum > k:
        firstList.append(currentNum)
    elif currentNum <= k:
        secondList.append(currentNum)

multiply = functools.reduce(lambda a, y: a * y,
    [firstList[x] for x in range(len(firstList)) if index(x) % 2 == 1])

print(multiply)
if len(firstList) > 0:
    indexWithMinValue = firstList.index(min(firstList))
    print(indexWithMinValue)

if len(secondList) > 0:
    maxAndMinDiff = max(secondList) - min(secondList)
    print(maxAndMinDiff)









