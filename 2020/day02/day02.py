import os

with open(os.path.dirname(__file__) + '/day02input.txt') as f:
    policies = [line for line in f]

# part one
validpasswds = 0
for policy in policies:
    letterCounter = 0
    times, letter, passwd = policy.split('\x20')
    mintimes, maxtimes = [int(i) for i in times.split('-')]
    for char in passwd:
        if char == letter[0]:
            letterCounter += 1
    if letterCounter >= mintimes and letterCounter <= maxtimes:
        print(policy.replace('\n', ''), letterCounter)
        validpasswds += 1

print(validpasswds)

# part two
validpasswds = 0
for policy in policies:
    positions, letter, passwd = policy.split('\x20')
    posOne, posTwo = [int(i) for i in positions.split('-')]
    if bool(letter[0] == passwd[posOne - 1]) ^ bool(letter[0] == passwd[posTwo - 1]):
        print(policy.replace('\n', ''), posOne,
              letter[0] == passwd[posOne - 1], posTwo, letter[0] == passwd[posTwo - 1])
        validpasswds += 1

print(validpasswds)
