import os
import re
import copy

with open(os.path.dirname(__file__) + '/day08input.txt') as f:
    insts = [line for line in f]


def processor():
    acc = 0
    idx = 0
    pastIdx = []

    while True:
        op, arg = insts[idx].strip().split("\x20")
        arg = int(arg)
        pastIdx.append(idx)

        if op == "acc":
            acc += arg
            idx += 1
        elif op == "jmp":
            idx += arg
        else:
            idx += 1
        print(op, arg, "|", idx, acc)

        # end execution on repeated index
        if idx in pastIdx:
            break
    return acc


print("Result Part 1 >>>", processor())


def process(op, arg, idx, acc):
    if op == "acc":
        acc += arg
        idx += 1
    elif op == "jmp":
        idx += arg
    else:
        idx += 1
    print(op, arg, "|", idx, acc)
    return idx, acc


def processor2():
    for instCount, line in enumerate(insts):
        opPert, argPert = line.strip().split("\x20")
        argPert = int(argPert)

        # correction for infinite loop
        if opPert == "nop":
            opPert = "jmp"
            print("CORRIGINDO ???", opPert, argPert, "|", instCount)
        elif opPert == "jmp":
            opPert = "nop"
            print("CORRIGINDO ???", opPert, argPert, "|", instCount)
        else:
            continue

        # realizando modificação na lista
        perturbed = copy.deepcopy(insts)
        perturbed[instCount] = opPert + " " + str(argPert)
        acc = 0
        idx = 0
        pastIdx = set()

        # looping de processamento na lista modificada
        while True:
            op, arg = perturbed[idx].strip().split("\x20")
            pastIdx.add(idx)
            idx, acc = process(op, int(arg), idx, acc)

            # if index is the last line, end execution
            if idx in pastIdx:
                looped = True
                break
            if idx == len(insts):
                looped = False
                break

        if not looped:
            break

    return acc


print("Result Part 2 >>>", processor2())
