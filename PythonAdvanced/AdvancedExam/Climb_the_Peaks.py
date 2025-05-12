from collections import deque

food = [int(x) for x in input().split(", ")]
stamina = deque([int(y) for y in input().split(", ")])

peaks = deque([80, 90, 100, 60, 70])
peaks_names = deque(['Vihren', 'Kutelo', 'Banski Suhodol', 'Polezhan', 'Kamenitza'])
conquered_peaks = []

if len(food) > len(stamina):
    range_1 = len(stamina)
else:
    range_1 = len(food)

for x in range(range_1):
    if peaks:
        if food[len(food) - 1] + stamina[0] >= peaks[0]:
            food.pop()
            stamina.popleft()
            peaks.popleft()
            conquered_peaks.append(peaks_names.popleft())
        else:
            food.pop()
            stamina.popleft()

if not peaks_names:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print("Conquered peaks:")
    for x in conquered_peaks:
        print(x)
