knights_number = 0
knights = []

print("Let's create a knight!")
name = input("What is the knight's name: ")
knights.append(name)

while knights_number < 1:

    print("Their name is: " + knights[0])
    knights_number += 1

print("--- What would you like to update? ---")
print("1: Knight's name: " + knights[0] )

try:


    selection = int(input("Select your option: "))

    if selection  == 1:
        if knights_number >= 0:
            print("You have a new knight!")

        knights[0] = str(input("What is their new name: "))
        print("Your knight's new name is: " + knights[0])
    else:
        print("--- Please select a valid option ---")

except:
    print("--- Try Again! ---")

print("Goodbye sir " + knights[0])
