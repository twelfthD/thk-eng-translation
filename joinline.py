with open("niv.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("niv.txt", "w") as f:
    for line in lines:
        # # except for the first line, remove the newline character
        # if line != lines[0]:
        #     line = line.rstrip()
        # f.write(line)

        for i in range(10): # add newline characters before the verse number
            # find "."+str(i) in the line and replace it with ".\n"+ str(i)
            line = line.replace('"{}'.format(i), '"\n{}'.format(i))
        f.write(line)





            

           

        





        
        
