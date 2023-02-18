# get all vocabularies from the files

# with open("temp2.txt", "r", encoding="utf8") as f:
#     lines = f.readlines()
# with open("temp2.txt", "w") as f:

#     for line in lines:
#         # split words by space
#         words = line.split()

#         f.write(words)

def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

a="calvin klein design dress calvin klein"
a=' '.join(unique_list(a.split()))
        
        
    




       
    





