import os
import itertools
import time

# cada adaptador pode recebe um entrada de 1 ate 3 jolts mais baixo e continuar produzindo sua joltagem de saida
# adaptador integrado que suporta 3 jolts a mais que a joltagem do maior adaptador
# Ponto de carregamento esta com 0 jolts


with open(os.path.dirname(__file__) + '/day10input.txt') as f:
    adapters = [int(line) for line in f]


def adapterOrganizer():
    adapterOrder = []
    adapterOrder.append(0)
    maxJoltage = max(adapters) + 3
    lastJoltage = 0
    joltsDiff1 = 0
    joltsDiff3 = 0

    while True:
        if min(adapters) <= lastJoltage + 3:
            adapter = min(adapters)
            if adapter == lastJoltage + 1:
                joltsDiff1 = joltsDiff1 + 1
            else:
                joltsDiff3 = joltsDiff3 + 1
            adapterOrder.append(adapter)
            adapters.remove(adapter)
            lastJoltage = adapter
            print(adapter, joltsDiff1, joltsDiff3)
        if len(adapters) == 0:
            joltsDiff3 += 1
            adapterOrder.append(maxJoltage)
            break
    return adapterOrder, joltsDiff1, joltsDiff3, joltsDiff1*joltsDiff3


#print("Result Part 1 >>>", adapterOrganizer())


def adapterCombinations():
    start = time.time()
    adapters.sort()
    minAdapters = int(max(adapters) / 3)
    combinations = 0
    for countLen in range(len(adapters), minAdapters, -1):
        for comb in itertools.combinations(adapters, countLen):
            if max(adapters) in comb and min(adapters) <= 3:
                lastAdapter = 0
                validComb = True
                for adapter in comb:
                    if adapter <= lastAdapter + 3:
                        lastAdapter = adapter
                        continue
                    else:
                        validComb = False
                        break
                if validComb:
                    combinations += 1
                    print(countLen, comb, combinations)
    print(time.time() - start)
    return combinations


def find(index, chain, dp):
    if index in dp:
        return dp[index]

    result = 0
    if index == len(chain) - 1:
        result = 1
    else:
        cur = chain[index]
        for p in [1, 2, 3]:
            if cur + p in chain:
                print(index, cur, p, result, dp)
                result += find(chain.index(cur + p), chain, dp)

    dp[index] = result
    return result


adapters += [0, max(adapters)+3]
adapters.sort()
print("Result Part 2 >>>", find(0, adapters, {}))
