
with open("niv.txt", "r", encoding="utf8") as f:
    lines = f.readlines()
with open("niv.txt", "w") as f:
    # #for i in range(len(a) - 1):
    # for line in lines:
    #     f.write(line.replace('; 9', ';\n9'))

    # # remove newline at the end of each line except the first one
    # for i in range(len(lines) - 1):
    #     f.write(lines[i].replace("\n", " "))

    # range search between 1 - 177, and replace if found
    for line in lines:
        
        for i in range(177):
            if line.find(", " + str(i)) != -1:
                line = line.replace(", " + str(i), ',\n' + str(i))
        f.write(line)



            

        



           

                
                
               
            

        
          
        
            




    



            

        
        
        
            
            
        

        




        
        


        


        









        
            


            
            
        

        

        
        
        
    

        



      



        



           

        





        
        
