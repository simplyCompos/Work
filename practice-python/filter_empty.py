import sys
content = sys.stdin.read()
filtered = "".join(filter(lambda ch: ch != "\n", content))
print(filtered)
