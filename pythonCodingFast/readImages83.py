# binary files - non-text files -> 'rb', 'wb' modes
inputFile = open('myImage.png', 'rb')
outputFile = open('myOutputImage.png', 'wb') # creates new image file
msg = inputFile.read(10) # read 10 bytes only, to save resources
while len(msg):
    outputFile.write(msg)
    msg = inputFile.read(10) # next 10 bytes
inputFile.close()
outputFile.close()    
