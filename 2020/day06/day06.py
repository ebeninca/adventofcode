import os
from ast import literal_eval

with open(os.path.dirname(__file__) + '/day06input.txt') as f:
    fileLines = [line for line in f]

groupAns = set()
ansSum = 0
for idx, ans in enumerate(fileLines):

    groupAns.update([char for char in ans.strip()])
    if ans in ('\n', '\r\n') or idx == len(fileLines)-1:
        ansSum += len(groupAns)
        print(idx, ansSum, groupAns)
        groupAns = set()


print('answers sum part 1>>> ' + str(ansSum))


with open(os.path.dirname(__file__) + '/day06input.txt') as f:
    fileLines = [line.split() for line in f.read().strip().split("\n\n")]

ansSum = 0
for idxg, group in enumerate(fileLines):
    groupAns = set()
    for idx, answer in enumerate(group):
        if idx == 0:
            groupAns.update([char for char in answer.strip()])
        groupAns &= set([char for char in answer.strip()])

    print(idxg, ansSum, groupAns)
    ansSum += len(groupAns)

# 3243
print('answers sum part 2 >>> ' + str(ansSum))
