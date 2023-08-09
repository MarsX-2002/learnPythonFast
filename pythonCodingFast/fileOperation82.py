# open and read txt by Buffer size (byte size)
inputFile = open('myFile.txt', 'r')
outputFile = open('myOutputFile.txt', 'w') # creates new one
msg = inputFile.read(10) # read 10 bytes only, to save resources
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10) # next 10 bytes
inputFile.close()
outputFile.close()    


