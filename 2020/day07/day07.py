import os
import re

with open(os.path.dirname(__file__) + '/day07input.txt') as f:
    fileLines = [line for line in f]

bagsList = set()


def recursiveBags(currentBag, countBags):
    for idx, line in enumerate(fileLines):
        if len(re.findall("\d* " + currentBag, line.strip())) > 0:
            bagName = line.strip().split("bags contain")[0]
            if bagName not in bagsList:
                bagsList.add(bagName.strip())
                countBags += 1
                print(countBags, idx, " | bagName > ",
                      bagName, " | currentBag > ", currentBag, " | line > ", line.strip())
                countBags = recursiveBags(bagName, countBags)
    return countBags


recursiveBags("shiny gold", 0)
print(len(bagsList), bagsList)
