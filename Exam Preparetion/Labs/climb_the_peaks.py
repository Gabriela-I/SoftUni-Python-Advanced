from collections import deque

food = deque(int(el) for el in input().split(', '))
stamina = deque(int(el) for el in input().split(', '))
peaks = deque((['Vihren', 80], ['Kutelo', 90], ['Banski Suhodol', 100], ['Polezhan', 60], ['Kamenitza', 70]))
conquered_peaks = []
while food:# moje da ne e prawilno, moje bi days == 7
    if not peaks:
        break
    portion = food.pop()
    current_stamina = stamina.popleft()
    peak = peaks.popleft()
    if portion + current_stamina >= peak[1]:
        conquered_peaks.append(peak[0])
        continue
    elif portion + current_stamina < peak[1]:
        peaks.appendleft(peak)
        continue

if peaks:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
else:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
if conquered_peaks:
    print(f"Conquered peaks: ", *conquered_peaks, sep='\n')



