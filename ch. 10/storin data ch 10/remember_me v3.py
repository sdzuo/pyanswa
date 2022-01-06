#remember_me v3 - refactored #3
import json

def get_stored_user():
    #Get stored usn if available.
    filename = 'username3.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    #Prompt for a new username!
    username = input("What is your name? ")
    filename = 'username2.json'
    with open(filename,'w') as f:
            json.dump(username.title(),f)
    return username.title()
    
def greet_user():
    #Greet the user by name."
    username = get_stored_user()
    if username:
        print(f"Welcome back, {username.title()}")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username.title()}!")
greet_user()
