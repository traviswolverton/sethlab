#Login System
#password and username storage
stored_password = "booleanrules1423" 
stored_username = "sethwolverton514" 

def user_dashboard(username):
    while True:
        print("Welcome to your dashboard, " + username + "!")
        print("1. View Profile")
        print("2. Manage Tasks")
        print("3. Access Resources")
        print("4. Logout")

        choice = input("Select an option: ")
#input for both username and password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
#says if you are logged in or not
is_logged_in = (input_username == stored_username) and (input_password == stored_password)
#what happens if you are logged in or not
if is_logged_in:
    print("Welcome, " + input_username + "!")
else:
    if input_username != stored_username:
        print("Incorrect username.")
    if input_password != stored_password:
        print("Incorrect password.")
