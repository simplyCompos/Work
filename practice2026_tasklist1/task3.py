print("please enter a, b and c")
a = float(input())
b = float(input())
c = float(input())

if a == 0;
    print("a cant be 0")
else:
    D = b**2 - 4*a*c
    print("D = ", D)
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print("roots")
        print("x1: ", x1)
        print("x2: ", x2)
    elif D == 0:
        x = -b / (2*a)
        print("root: ", x)
    else:
        print("no roots")
