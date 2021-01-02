S = input()
S = sorted(S)
number = 0
_sum = 0

for i in S:
    try:
        _sum += int(i)
        number += 1
    except:
        break

_sum = list(str(_sum))
S = ''.join(S[number:] + _sum)

print(S)
