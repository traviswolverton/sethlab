# hello_world.py
#age factor authentication
age = int(input("Please enter your age: "))
is_of_voting_age = age >= 18
#citizen factor authentication
citizen_input = input("Are you a citizen? (y/n)" )
is_citizen = citizen_input == "y"
#legible or illegible to vote
is_eligible_to_vote = is_of_voting_age and is_citizen
if is_eligible_to_vote:
    print("Congratulations! You are eligible to vote.")
else:
    print("You are not eligible to vote.")