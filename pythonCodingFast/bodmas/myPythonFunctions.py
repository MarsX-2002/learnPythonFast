from random import randint
from os import remove, rename
def getUserScore(userName):
    try:
        f = open('bodmas\\userScores.txt', 'r')
        for line in f:
            content = line.split(', ')
            if content[0] == userName:
                f.close()
                return content[1]
        f.close()
        return '-1'   
    except IOError:
        print("File not found")
        print("New file will be created")
        f = open('bodmas\\userScores.txt', 'w')
        f.close()
        return '-1'


def updateUserPoints(newUser, userName, score):
    if newUser:
        f = open('bodmas\\userScores.txt', 'a')
        f.write(f"n\{userName}, {score}")
        f.close()
    else:
        f = open('bodmas\\userScores.txt', 'r')
        temp = open('bodmas\\userScores.tmp', 'w')
        for line in f:
            content = line.split(',')
            if content[0] == userName:
                content[1] = score
                line = f'{content[0]}, {content[1]}\n'
            
            temp.write(line)    
        f.close()
        temp.close()   
        
    remove('bodmas\\userScores.txt')
    rename('bodmas\\userScores.tmp', 'bodmas\\userScores.txt')     
            
def generateQuestions():
    operandList = [0, 0, 0, 0, 0,]
    operatorList = ['', '', '', '']
    operatorDict = {1:' + ', 2:' - ', 3:'', 4:'*'}
    
    for i in range(len(operandList)):
        operandList[i] = randint(1, 9)
    
    for i in range(len(operatorList)):
        if i > 0 and operatorList[i - 1] != '**':
            operator = operatorDict[randint(1, 4)] 
        else:
            operator = operatorDict[randint(1, 3)]
        operatorList[i] = operator    
            
    questionString = str(operandList[0])
    for i in range(4):
        questionString = questionString + operatorList[i] + str(operandList[i+1])
    result = eval(questionString)
    
    questionString = questionString.replace('**', '^')
    print(questionString)
    while True:
        try:
            answer = int(input("Answer: "))
            if answer == result:
                print("Correct!")
                return 1
            else: 
                print(f"Sorry... answer was: {result}")        
                return 0 
        except Exception as e:
            print("You did not enter a number... try again")
            answer = int("Answer: ")    
        
    