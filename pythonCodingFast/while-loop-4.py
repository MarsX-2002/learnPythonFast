# A while loop repeteadly executes instructions inside the loop while a certain condition remains valid.
# while condition is true:
#   do A

counter = 5
while counter > 0:
    print(f"counter = {counter}")
    counter -= 1
    if counter == 1:
        print("go")
        break

# continue - skip 1 iteration
for i in range(5):
    if i == 3:
        print("skip 3")
        continue
    print(i)



