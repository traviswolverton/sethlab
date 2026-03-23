stored_username = ("sethwolve0514")
stored_password = ("seth0514@ggies!!" )
input_username = input ("Enter Username: ")
input_password = input ("Enter Password: ")
is_logged_in = (input_username == stored_username) and (input_password == stored_password)
if is_logged_in:
    print("Login Successful!")
    my_list = ["1. Tic Tac Toe",  "2. Quiz",  "3. Chess"]
    print("Here is a list of games.")
    for item in my_list:
        print(item)
    choice = ("Please select a game number: ")

    if choice == 1:
        print("Selected 1")
        print("Starting Tic Tac Toe...")
    #Tic-Tac-Toe programming HERE

    elif choice == 2:
        print("Selected 2")
        print("Starting Quiz...")
    #Quiz programming HERE

    elif choice == 3:
        print ("Selected 3")
        print ("Starting Chess...")

    else:
        print("Invalid selection. Select a valid number.")


else: 
    print("Login Failed. Invalid username/password.")