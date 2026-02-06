import math

print("Enter speed and angle please")
v0 = float(input))
angle = float(input))

g = 9.8

alpha = angle + math.pi / 180
v0y = v0 * math.sin(alpha)

h_max = v0y**2 / (2 * g)
print("Max height: " h_max)

T = 2 * v0y / g
print("height of shell every second: ")
t = 0
while t <= T:
    h = v0y * t - (g * t**2) / 2
    if h < 0:
        h = 0
    print("t = ", t,  "h = ", h)
    t += 1
