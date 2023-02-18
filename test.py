# join two files line by line
combine =[]

with open("niv.txt", encoding="utf8") as xh:
  with open('bible_thk.txt', encoding="utf8") as yh:
    with open("eng_thk.txt","w" , encoding="utf8") as zh:
      #Read first file
      xlines = xh.readlines()
      #Read second file
      ylines = yh.readlines()
      #Combine content of both lists
      #combine = list(zip(ylines,xlines))
      #Write to third file
      for i in range(len(xlines)):
        line = xlines[i].strip() + '@1' + ylines[i]
        zh.write(line)


    







