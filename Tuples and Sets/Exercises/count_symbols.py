from collections import OrderedDict

text = tuple(i for i in input())
char = {ch: text.count(ch) for ch in text}
sorted_char = OrderedDict(sorted(char.items()))
for k, v in sorted_char.items():
    print(f'{k}: {v} time/s')

