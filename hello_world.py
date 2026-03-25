#Login System
#password and username storage
stored_password = "booleanrules1423" 
stored_username = "sethwolverton514" 

def user_dashboard(username):
    while True:
        print("Welcome," + username + "!")
        print("1. Profile Management")
        print("2. Manage Tasks")        
        print("3. Access Resources")
        print("4. Logout")

        choice = input("Select an option: ")

        if choice == '1':
            view_profile(username)
        elif choice == '2':
            manage_tasks()
        elif choice == '3':
            access_resources()
        elif choice == '4':
            print("Logging out...")
            break
        
        else:
            print("Invalid option. Please selct a valid choice.")

def view_profile(username):
    print(f"Profile Manegment for {username}")
    print("Profile Name: " + username)
    print("Real Name: Seth A. Wolverton")
    print("Account Created: 3-24-2026")
    print("Email: sethwolverton514@gmail.com")
          
def manage_tasks():
    print("Task Management: ")
    print("Task List: (Placeholder)")
    #more options HERE
    input("Press Enter to return to the dashboard")

def access_resources():
    print("Resource Access: ")
    print("Resources: (Placeholder)")
    #more options HERE
    input("Press Enter to return to the dashboard")

#input for both username and password
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
#says if you are logged in or not
is_logged_in = (input_username == stored_username) and (input_password == stored_password)
#what happens if you are logged in or not
if is_logged_in:
    print("Welcome, " + input_username + "!")
    user_dashboard(input_username)
else:
    if input_username != stored_username:
        print("Incorrect username.")
    if input_password != stored_password:
        print("Incorrect password.")
