import re
with open("niv2.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("niv2.txt", "w") as f:


    
        # # except for the first line, remove the newline character
        # if line != lines[0]:
        #     line = line.rstrip()
        # f.write(line)
    for line in lines:
        for i in range(100, 177): # add newline characters before the verse number
            # find "."+str(i) in the line and replace it with ".\n"+ str(i)
            #line = line.replace(',{}'.format(i), ',\n{}'.format(i))
            # line = line.replace("'{}".format(i), "'\n{}".format(i))
            # line = line.replace("-{}".format(i), "-\n{}".format(i))
            # line = line.replace("?{}".format(i), "?\n{}".format(i))
            # line = line.replace("!{}".format(i), "!\n{}".format(i))
            # line = line.replace(":{}".format(i), ":\n{}".format(i))
            line = line.replace("{} ".format(i), "")

            



        # for i in range(1):       
        #     for letter in range(65):
        #         for line in lines:
        #             toletter = str(chr(letter))
        #             num = str(i)
        #             line = line.replace("\n"+ num + toletter, "\n"+ num + " " + toletter)
        #             f.write(line)

        # # add space between words using regex "(?i)(?:(?<=\d)(?=[a-z])|(?<=[a-z])(?=\d))"g
        # for line in lines:
        #     line = re.sub(r'(?i)(?:(?<=\d)(?=[a-z])|(?<=[a-z])(?=\d))', ' ', line)
        #     f.write(line)


        

    
    
            



        





            

           

        





        
        
