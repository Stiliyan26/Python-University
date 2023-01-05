import functools
import math

def inputValidator(inpMsg, errMsg, isPositive):
    while True:
        try:
            number = int(input(inpMsg))
            if isPositive:
                if number <= 0:
                    raise Exception(errMsg)
                return number
            return number
        except ValueError:
            print("Invalid type try again!")
        except Exception as e:
            print(e)

n = inputValidator("Enter number n: ", "Invalid number n!", True)
k = inputValidator("Enter number k: ", "Invalid number k!", True)

numbers = [inputValidator("Enter number: ", "Invalid number!", False)  for _ in range(n)]

firstList = [num for num in numbers if num > k]
multiply = functools.reduce(lambda a, y: a * y,
        [firstList[i] for i in range(len(firstList)) if i % 2 == 1])

print(f'Multiplication is {multiply}')

if len(firstList) > 0:
    print(firstList.index(min(firstList)))
else:
    print('No such data!')

secondList = [num for num in numbers if k >= num > 0]

if len(secondList) > 0:
    print(max(secondList) - min(secondList))
else:
    print('No such data!')