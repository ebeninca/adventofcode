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
print("Result Part 1 >>>", len(bagsList), bagsList)


bagsList = set()


def recursiveBagsPart2(currentBag, countBags):
    for idx, line in enumerate(fileLines):
        rootBags, childBags = line.strip().split("contain")
        if rootBags.strip().startswith(currentBag):
            childBags = childBags.strip().split(", ")
            for bag in childBags:
                #re1 = re.compile("([\d]) ([a-z]+\W[a-z]+)").split(bag.strip())
                bagAmountList = re.findall("\d*", bag.strip())[0]
                if len(bagAmountList) > 0:
                    bagAmount = int(bagAmountList[0])
                    bagName = bag.strip().split(str(bagAmount))[1]
                    bagName = bagName.strip().split("bag")[0]
                    for count in range(bagAmount):
                        countBags += 1
                        print(countBags, idx, " | currentBagx > ", currentBag, "| bagName > ",
                              bagName.strip(), " | line > ", line.strip())
                        countBags = recursiveBagsPart2(
                            bagName.strip(), countBags)
    return countBags


print("Result Part 2 >>>", recursiveBagsPart2("shiny gold", 0))
