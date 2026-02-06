print("Enter num")
n = int(input())

def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n - 1)
if n < 0:
    print("factorial of negative number is not defined")
else:
    print("factorial", n, " = ", fact(n))
