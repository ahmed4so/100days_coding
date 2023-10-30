List = []  # Create an empty list to store items

while True:
    print("=================== To-Do List =============================")

    # Display menu options
    print("1. Add something")
    print("2. Show me the list")
    print("3. Remove something from the list")
    print("4. Exit program")

    # Ask the user to choose an option
    user = int(input("Choose one option: "))

    if user == 1:  # If the user chooses to add an item
        new_item = input("Enter something: ")  # Ask for the item to add
        List.append(new_item)  # Add the item to the list
        print("The item was added")

    elif user == 2:  # If the user chooses to show the list
        print(List)  # Display the current list

    elif user == 3:  # If the user chooses to remove an item
        remove_item = input("Enter the item you want to delete: ")  # Ask for the item to remove
        List.remove(remove_item)  # Remove the item from the list
        print("The item was removed")

    elif user == 4:  # If the user chooses to exit the program
        print("Exit ......")
        break  # Exit the loop and end the program

    else:
        print("You did not choose a valid option!")  # If the user enters an invalid option
