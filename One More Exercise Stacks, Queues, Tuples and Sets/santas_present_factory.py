from collections import deque

boxes = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())
crafted_toys = []

toys = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while boxes and magic_level:
    current_box = boxes.pop()
    current_magic = magic_level.popleft()
    if current_box == 0 and current_magic == 0:
        continue
    elif current_box == 0:
        magic_level.appendleft(current_magic)
        continue
    elif current_magic == 0:
        boxes.append(current_box)
        continue

    if toys.get(current_box * current_magic):
        crafted_toys.append(toys[current_box * current_magic])
    elif current_box * current_magic < 0:
        boxes.append(current_box + current_magic)
    elif current_box * current_magic > 0:
        boxes.append(current_box + 15)

if {'Doll', 'Wooden train'}.issubset(crafted_toys) or {'Teddy bear', 'Bicycle'}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if boxes:
    print(f"Materials left: {', '.join([str(el) for el in boxes][::-1])}")
if magic_level:
    print(f"Magic left: {', '.join(str(el) for el in magic_level)}")
[print(f"{toy}: {crafted_toys.count(toy)}") for toy in sorted(set(crafted_toys))]
