import os

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
                joltsDiff1 += 1
            else:
                joltsDiff3 += 1
            adapterOrder.append(adapter)
            adapters.remove(adapter)
            lastJoltage = adapter
            print(adapter, joltsDiff1, joltsDiff3)
        if len(adapters) == 0:
            joltsDiff3 += 1
            adapterOrder.append(maxJoltage)
            break
    return adapterOrder, joltsDiff1, joltsDiff3, joltsDiff1*joltsDiff3


print("Result Part 1 >>>", adapterOrganizer())
