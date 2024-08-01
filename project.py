print("Let's create a knight!")
name = input("What is the knight's name: ")
print("Their name is: " + name)

print("--- What would you like to update? ---")
print("1: Knight's name: " + name )

selection = int(input("Select your option: "))

if selection  == 1:
    name = str(input("What is their new name: "))
    print("Your knight's new name is: " + name)
else:
    print("--- Please select a valid option ---")

print("Goodbye sir " + name)
