# hello_world.py
age = int(input("Please enter your age: "))
citizen_input = input("Are you a citizen? (y/n)" )
is_citizen = citizen_input == "y"
is_of_voting_age = age >= 18
is_eligible_to_vote = is_of_voting_age and is_citizen
if is_eligible_to_vote:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")