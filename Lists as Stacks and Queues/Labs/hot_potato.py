from _collections import deque

kids = input().split()
players = deque(kids)
toss = int(input())
counter = 0
while len(players) > 1:
    counter += 1
    current_player = players.popleft()
    if counter == toss:
        counter = 0
        print(f"Removed {current_player}")
    else:
        players.append(current_player)
print(f"Last is {players[0]}")