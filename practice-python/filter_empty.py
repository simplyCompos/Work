with open("somefile.txt", "r") as file:
    content = file.readlines()
    filtered = list(filter(lambda ch: ch != "\n", content))
    print(filtered)
