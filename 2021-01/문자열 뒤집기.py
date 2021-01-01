S = input()
value = -1
result = [0, 0]

for i in S:
    if value != i:
        value = i
        
        if value == '0':
            result[0] += 1
        else:
            result[1] += 1

print(min(result))