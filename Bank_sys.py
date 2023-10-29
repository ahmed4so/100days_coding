print("================== Bank System ========================")
# Initialize existing account usernames and passwords
Exis_acc_user = ["user123", "user124"]
Exis_acc_pass = ["pass123", "pass124"]

# Initialize empty lists for new account usernames and passwords
New_acc_user = []
New_acc_pass = []

# Initialize Variables for user input
req_user = ""
req_pass = ""
request = 0
balance = float(100)
# Main program loop
while True:
    # Display menu and ask for user choice
    Req = int(input("1-Sign in \n2-Sign up\n "))
    # Sign in
    if Req == 1:
        req_user = input("Enter your username")
        req_pass = input("Enter your password")
        #  Check if the entered username and password exist in the existing accounts
        if req_user in Exis_acc_user and req_pass in Exis_acc_pass:
            print("1.Show Account Balance \n")
            print("2.Deposit Money \n")
            print("3.Withdraw Money \n")
            print("4.Exit \n")
            # Ask the user to choose one option from the menu
            request = int(input("Choose an option \n"))
        else:
            print(f"There is no {req_user} and {req_pass} in the system")
    # Sign Up
    elif Req == 2:
        New_acc_user = input("Enter your New username")
        New_acc_pass = input("Enter Your New passwords")
        # Add the new user and password to the list of existing account
        Exis_acc_user.append(New_acc_user)
        Exis_acc_pass.append(New_acc_pass)
        print("1.Show Account Balance \n")
        print("2.Deposit Money \n")
        print("3.Withdraw Money \n")
        print("4.Exit \n")
        # Ask the user to choose option from the menu
        request = int(input("Choose an option \n"))
    # If the user choose number 1 Show Balance
    if request == 1:
        print(f"Your Account Balance is {balance}")
        break
    # If the user choose number 2 Deposit Money
    elif request == 2:
        Dep_Mon = int(input("Enter the amount the money you want to deposit \n"))
        print("Successful deposit the money to your account", Dep_Mon+balance)

        break
    # If the user choose number 3 Withdraw Money
    elif request == 3:
        With_Mon = int(input("Enter the amount the money you want withdrawal \n"))
        print(balance-With_Mon)
        break
    # If the user choose number 4 Exit
    elif request == 4:
        print("Exit .....")
        break
    else:
        print(" You did not choose an option ")
