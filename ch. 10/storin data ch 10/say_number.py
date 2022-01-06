#10 -11 fav number, print fav number

import json

filename = 'favnumber.json'

with open(filename) as f:
    number = json.load(f)
    print(f"I know what your favorite number is! It's {number}.")
