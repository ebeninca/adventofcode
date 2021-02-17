import os
import copy

with open(os.path.dirname(__file__) + '/day11input.txt') as f:
    seats = [[c for c in line.strip()] for line in f]


def countOccupiedSeatsAround(currentSeat, idxL, idxC, seats):
    countOccupied = 0
    for idx1 in range(idxL-1, idxL+2):
        for idx2 in range(idxC-1, idxC+2):
            if idx1 < 0 or idx1 >= len(seats) or idx2 < 0 or idx2 >= len(seats[0]):
                continue
            if idx1 == idxL and idx2 == idxC:
                continue
            if seats[idx1][idx2] == '#':
                countOccupied += 1
    return countOccupied


def occupySeats(occupied):
    seatChange = False
    print(seats)
    originalSeats = copy.deepcopy(seats)
    for idxL, line in enumerate(seats):
        for idxC, seat in enumerate(line):
            if seat == '#' and countOccupiedSeatsAround(seat, idxL, idxC, originalSeats) >= 4:
                seats[idxL][idxC] = 'L'
                seatChange = True
            if seat == 'L' and countOccupiedSeatsAround(seat, idxL, idxC, originalSeats) == 0:
                seats[idxL][idxC] = '#'
                seatChange = True
    if seatChange:
        occupySeats(occupied)
    else:
        for idxL, line in enumerate(seats):
            for idxC, seat in enumerate(line):
                if seat == '#':
                    occupied += 1
        print(occupied)
        return occupied


print("Result Part 1 >>>", occupySeats(0))


def countOccupiedSeatsAround2(currentSeat, idxL, idxC, seats):
    countOccupied = 0
    while idxL < len(seats) and idxC < len(seats[0]):
        

    for idx1 in range(idxL-1, idxL+2):
        for idx2 in range(idxC-1, idxC+2):
            if idx1 < 0 or idx1 >= len(seats) or idx2 < 0 or idx2 >= len(seats[0]):
                continue
            if idx1 == idxL and idx2 == idxC:
                continue
            if seats[idx1][idx2] == '#':
                countOccupied += 1
    return countOccupied


def occupySeats2(occupied):
    seatChange = False
    print(seats)
    originalSeats = copy.deepcopy(seats)
    for idxL, line in enumerate(seats):
        for idxC, seat in enumerate(line):
            if seat == '#' and countOccupiedSeatsAround2(seat, idxL, idxC, originalSeats) >= 5:
                seats[idxL][idxC] = 'L'
                seatChange = True
            if seat == 'L' and countOccupiedSeatsAround2(seat, idxL, idxC, originalSeats) == 0:
                seats[idxL][idxC] = '#'
                seatChange = True
    if seatChange:
        occupySeats2(occupied)
    else:
        for idxL, line in enumerate(seats):
            for idxC, seat in enumerate(line):
                if seat == '#':
                    occupied += 1
        print(occupied)
        return occupied


print("Result Part 2 >>>", occupySeats(0))
