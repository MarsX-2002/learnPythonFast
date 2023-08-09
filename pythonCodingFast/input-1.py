# get user name, age
# store in dict

name = input("Your name? ")
age = input("Your age? ")
userData = {"name":name, "age":age}

print(f"You are {userData['name']} and you are {userData['age']} years old.")

# format methods
print("Hi there %s\n" %(userData["name"]))
print("You are {} years old".format(userData["age"]))

# row string
print("row string 'r'")
print(r"\n is not new line, same with \t")