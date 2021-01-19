import os

with open(os.path.dirname(__file__) + '/day01input.txt') as f:
    numbers = [int(line) for line in f]

# part one
for n1 in numbers:
    for n2 in numbers:
        if n1 == n2:
            continue
        if n1 + n2 == 2020:
            print(n1, n2, n1 + n2, n1 * n2)

# part two
for n1 in numbers:
    for n2 in numbers:
        if n1 == n2:
            continue
        for n3 in numbers:
            if n1 == n3 or n2 == n3:
                continue
            if n1 + n2 + n3 == 2020:
                print(n1, n2, n3, n1 + n2 + n3, n1 * n2 * n3)
