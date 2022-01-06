#remember_me v2 - combined

#Load the usn if it has been stored prev
#otherwise, prompt for the username and store it!

import json

filename = 'username2.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename,'w') as f:
        json.dump(username.title(),f)
        print(f"We'll remember you when you come back, {username.title()}!")
else:
    print(f"Welcome back, {username}!")
