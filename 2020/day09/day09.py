import os

with open(os.path.dirname(__file__) + '/day09input.txt') as f:
    numbers = [int(line) for line in f]


def sumValues(previousNumbers, number):
    for prev in previousNumbers:
        for prev2 in previousNumbers:
            if prev != prev2 and prev + prev2 == number:
                return True
    return False


def preambleSum(preamble):
    for idx, number in enumerate(numbers):
        if idx < preamble:
            continue
        previousNumbers = numbers[idx-preamble:idx]
        if sumValues(previousNumbers, number) == False:
            break
    return number


print("Result Part 1 >>>", preambleSum(25))


def contiguousSum(preamble):
    invalidNumber = preambleSum(preamble)
    invalidIdx = numbers.index(invalidNumber)
    previousNumbers = numbers[0:invalidIdx]
    for idx1, number1 in enumerate(previousNumbers):
        sumVal = number1
        for idx2, number2 in enumerate(previousNumbers):
            if idx2 > idx1:
                sumVal += number2
                if sumVal > invalidNumber:
                    break
                if sumVal == invalidNumber:
                    return min(previousNumbers[idx1:idx2]) + max(previousNumbers[idx1:idx2])
    return 0


print("Result Part 2 >>>", contiguousSum(25))
