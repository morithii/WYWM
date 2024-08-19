
# call for this when you want to create a new knight
def create_knight(knights):

    # Creates a new List for the knight
    knights_data = []

    print("Let's create a knight!")

    # Set the information up for the knight
    knights_data.append(str(input("What is the knight's name: ")))

    # Adds the information to the knight
    knights.append(knights_data)

# Call a knight and change their data
def change_data(knights):

    print("--- What would you like to update? ---")
    print("1: Knight's name: " + knights[0] )

    try:


        selection = int(input("Select your option: "))

        if selection  == 1:
            if knights_number == 0:
                print("You have a knight!")

            knights[0] = str(input("What is their new name: "))
            print("Your knight's new name is: " + knights[0])
            return
        else:
            print("--- Please select a valid option ---")

    except:
        print("--- Try Again! ---")
        change_data(knights)

 # Show the current knights and select one
def select_knight(knights):

    # Reset to print all the knights you have
    knights_number = 0
    print("What knight do you want to update? \n")
    while knights_number < int(len(knights)):
        print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number][0]))
        knights_number += 1
    selection = (int(input("\nSelect the knights number: "))) -1
    change_data(knights[selection])


# This is the menu and we make our selections here
def menu(knights_number):

    # Print the display options
    print("What do you want to do?")
    print("1: Create a new knight")
    print("2: Update the knight")
    print("0: Exit")

    # Allow a selection to be tested
    try:

        # Takes the users selection option
        select = int(input("Selection number: "))
        print() # Creates a blank line

        # Creates a new knight
        if select == 1:
            create_knight(knights)

            #Print out knight that was made
            print("\n--- Your Knight ---\n") #Alternative way to create new line
            print("Knight's name: " + str(knights[knights_number][0] + "\n"))
            knights_number += 1
            menu(knights_number)

        elif select == 2:
            if int(len(knights)) == 0:
                print("You need to create a knight first!! \n")
            else:
                select_knight(knights)


        elif select == 0:
            print("--- All your Knights! ---\n")

            # Reset the knights_number, to count all the knights
            knights_number = 0

            while knights_number < int(len(knights)):
                print(str(knights_number + 1) + "- Knight's name: " + str(knights[knights_number][0]))
                knights_number += 1

        # Required for catching an integar selection
        else:
            print("--- Try Again! ---\n")
            menu(knights_number)

    # We are looking for an integar selection
    except:
        print("--- Try Again! ---")
        menu(knights_number)

# Setting the scene
knights_number = 0
knights = []


# Run the program
menu(knights_number)
