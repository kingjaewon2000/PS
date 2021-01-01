S = input()
result = int(S[0])

for i in range(1, len(S)):
    number = int(S[i])
    if (result + number) > (result * number):
        result += number
    else:
        result *= number

print(result)


