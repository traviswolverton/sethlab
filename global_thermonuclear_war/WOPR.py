stored_username = ("sethwolve0514")
stored_password = ("seth0514@ggies!!" )
input_username = input ("Enter Username: ")
input_password = input ("Enter Password: ")
is_logged_in = (input_username == stored_username) and (input_password == stored_password)
if is_logged_in:
    print("Login Successful!")
    print("Here is a list of games:")
    my_list = ["1. Tic Tac Toe", "2. Quiz," "3. Chess"]
    for item in my_list:
        print(item)
else: 
    print("Login Failed. Invalid username/password.")