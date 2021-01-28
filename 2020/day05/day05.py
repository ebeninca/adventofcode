import os

with open(os.path.dirname(__file__) + '/day05input.txt') as f:
    seats = [line for line in f]

highest = 0
seatsList = []

# FBFBFFBRRR: 40-47, 40-43, 40-41, 41

for idxs, seat in enumerate(seats):
    minfb, maxfb, minlr, maxlr = 0, 127, 0, 7
    halffb, halflr = 0, 0

    for idx, char in enumerate(seat.strip()):

        if idx < 7:
            halffb = minfb + int((maxfb - minfb) / 2)
            if char == 'F':
                maxfb = halffb
            elif char == 'B':
                minfb = halffb = halffb + 1

        if idx >= 7:
            halflr = minlr + int((maxlr - minlr) / 2)
            if char == 'L':
                maxlr = halflr
            elif char == 'R':
                minlr = halflr = halflr + 1

    if (halffb * 8 + halflr) > highest:
        highest = (halffb * 8 + halflr)

    seatsList.append(int(halffb * 8 + halflr))
    print(idxs, seat.strip(), halffb, halflr, halffb * 8 + halflr)

print('maior valor >>> ' + str(highest))

seatsList.sort()
print(seatsList)

lastSeat = 0
for seat in seatsList:
    currentSeat = int(seat)
    if (currentSeat - 1) == lastSeat or lastSeat == 0:
        lastSeat = currentSeat
    else:
        print('meu acento >>> ' + str(currentSeat - 1))
        break