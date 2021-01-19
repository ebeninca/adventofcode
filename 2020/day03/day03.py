import os

with open(os.path.dirname(__file__) + '/day03input.txt') as f:
    trees = [[column for column in list(line.strip())] for line in f]


# part one
def countTrees(columnMove, lineMove):
    numTrees = 0
    columnMoveInc = columnMove
    lineMoveInc = lineMove
    while lineMoveInc < len(trees):
        numColumns = len(trees[lineMoveInc])
        if columnMoveInc > numColumns - 1:
            columnMoveInc -= numColumns
        #print(lineMoveInc, columnMoveInc, trees[lineMoveInc][columnMoveInc])
        if trees[lineMoveInc][columnMoveInc] == '#':
            numTrees += 1
        columnMoveInc += columnMove
        lineMoveInc += lineMove
    return numTrees


print(countTrees(3, 1))

# part two
print(countTrees(1, 1))
print(countTrees(3, 1))
print(countTrees(5, 1))
print(countTrees(7, 1))
print(countTrees(1, 2))

print(countTrees(1, 1) * countTrees(3, 1)
      * countTrees(5, 1) * countTrees(7, 1) * countTrees(1, 2))
