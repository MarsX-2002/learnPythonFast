# 'r' - read only
# 'w' - write only (nofile -> creates new, oldfile -> erase)
# 'a' - append (nofile -> creates new, oldfile -> add to the end)
# 'r+' - read and write
# ----------------
f = open('myFile.txt', 'r') 

firstLine = f.readline()
secondLine = f.readline()
print(f"{firstLine}{secondLine}")

allLines = f.readlines() # list of lines
print(allLines, end='') # no \n added

f.close() # always close file
#-----------------

# use for loop for reading file
f = open('myFile.txt', 'r')
for line in f:
    print(line, end='')
f.close()

# write to file
f = open('myFile.txt', 'a')
f.write("/nThis line added bro :)")
f.close()