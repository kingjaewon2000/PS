N = input()

M = len(N) / 2
result = 0

for i in range(len(N)):
    if i < M:
        result += int(N[i])
    else:
        result -= int(N[i])

if result == 0:
    print("LUCKY")
else:
    print("READY")
