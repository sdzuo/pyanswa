#10-11 Favorite Number
import json

filename = 'favnumber.json'
fav_number = input("Enter your favorite number? ")
fav_number = int(fav_number)

with open(filename,'w') as f:
    json.dump(fav_number, f)
    
