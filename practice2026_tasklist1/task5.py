print("enter how many numbers")
a = int(input())

b = []

for i in range(n):
    print("Enter number")
    c = int(input))
    i += 1
    b.append(c)
for i in range(a - 1):
    for j in range(n - 1 - i):
        if b[j] > b[j + 1]:
            b[j], b[j + 1] = b[j + 1], b[j]
print(b)
