import sys
lines = sys.stdin.readlines()
filtered = [line for line in lines if line.strip() != ""]

for line in filtered:
    print(line, end="")
