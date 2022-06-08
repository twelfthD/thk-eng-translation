# # print the total number of words in a file
# with open("niv.txt", "r", encoding="utf8") as f:
#     print(len(f.read().split()))

with open("niv.txt","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        # if line word count is less than or equal to 1, join to previous line
        if len(line.split()) <= 1:
            # join to previous line
            f.seek(-len(line), 1)
            