#10-12 Fav number remembered
import json

#combine both programs from 10-11

filename = 'favnumber2.json'

try:
    with open(filename) as f:
        number = json.load(f)
        print(f"I know what your favorite number is! It's {number}.")
except FileNotFoundError:
    fav_number = input("Enter your favorite number? ")
    fav_number = int(fav_number)
    with open(filename,'w') as f:
        json.dump(fav_number, f)

