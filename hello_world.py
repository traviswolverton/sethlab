#Login System
#password and username storage
stored_password = "booleanrules1423" 
stored_username = "sethwolverton514" 

def user_dashboard(username):
    while True:
        print("Welcome," + input_username + "!")
        print("1. Profile Management")
        print("2. Manage Tasks")        
        print("3. Access Resources")
        print("4. Logout")

        choice == input("Please select an option: ")

        if choice == '1':
            view_profile(username)
        elif choice == '2':
            manage_tasks()
        elif chouce == '3':
            access_resources()
        elif choice == '4':
            print("Logging out...")
            break
        
        else:
            print("Invalid option. Please selct a valid choice.")

def view_profile(username):
    print("Profile Mangemnet for {username}")
    print("Profile Name: " + {username})
    #more option HERE
    input("Press Enter to return to the dashboard")

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
