with open("niv.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("niv.txt", "w") as f:
    for line in lines:
        #f.write(line.replace("\n", " "))
        f.write(line.replace(" 9", "\n9"))


