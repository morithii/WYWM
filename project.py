knights = []

# call for this when you want to create a new knight
def create_knight():
    knights_data = []

    print("Let's create a knight!")

    # Set the information up for the knight
    knights_data = (str(input("What is the knight's name: ")))

    # Adds the information to the knight
    knights.append(knights_data)

# Show the current knights and select one
def select_knight(knights):
    while knights_number < 1:

        print("Their name is: " + knights[0])
        knights_number += 1

# Call a knight and change their data
def change_data(knights):

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

# This is the menu and we make our selections here
def menu(knights_number):

    # Print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("0: Exit")

    # Allos a selection to be tested
    try:

        # Takes the users selection option
        select = int(input("Selection number: "))
        print() # Creates a blank line

        # Creates a new knight
        if select == 1:
            create_knight(knights)

            #Print out knight that was made
            print("\n--- Your Knight ---\n") #Alternative way to create new line
            print("Knight'n name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)

        elif select == 0:
            print("Goodbye")

        else:
            print("--- Try Again! ---\n")
            menu(knights_number)


    except:
        print("--- Try Again! ---")
        menu(knights_number)

# Setting the scene
knights_number = 0


menu(knights_number)
