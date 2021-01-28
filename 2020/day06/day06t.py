import os
from ast import literal_eval

with open(os.path.dirname(__file__) + '/day06input.txt') as f:
    fileLines = [line.split() for line in f.read().strip().split("\n\n")]

def count(groups: list, everyone: bool) -> int:
    result = 0
    for idx, group in enumerate(groups):
        letras = []
        answers = {chr(c):0 for c in range(97, 123)}

        for answer in group:
            for letter in answer:
                letras.append(letter)
                answers[letter] += 1

        if everyone:
            result += sum([1 for letter in answers if answers[letter] == len(group)])
            print(idx, result, letras)
        else:
            result += sum([1 for letter in answers if answers[letter]])

    return result

def part1(groups: list) -> int:
    return count(groups, False)

def part2(seat_ids: list) -> int:
    return count(groups, True)

if __name__ == "__main__":
    groups = fileLines
    #print(f"Part 1: {part1(groups)}")
    print(f"Part 2: {part2(groups)}")
