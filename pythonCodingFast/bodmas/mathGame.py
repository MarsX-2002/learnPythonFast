try:
    import myPythonFunctions as mpf
    userName = input("Your userName: ")
    userScore = int(mpf.getUserScore(userName))
    newUser = False
    if userScore == -1:
        newUser = True
        userScore = 0
        
    userChoice = 0
    while userChoice != '-1':
        userScore += mpf.generateQuestions() 
        print(f"Current score = {userScore}")
        userChoice = input("Exit: [-1]\tContinue: [Enter]\n")
     
    mpf.updateUserPoints(newUser, userName, str(userScore)) 
    print(f"{userName}: {userScore}")   
except Exception as e:
    print("Error occured... program will exit!")
        