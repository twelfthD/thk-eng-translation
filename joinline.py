with open("niv.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("niv.txt", "w") as f:
    for line in lines:
        #f.write(line.replace("\n", " "))
        #f.write(line.replace(" 9", "\n9"))

        # if line word count is less than 1, join to previous line
        if len(line.split()) <= 1:
            # join to previous line
            lines[lines.index(line) - 1] += line
        else:
            f.write(line)
            

           

        





        
        
