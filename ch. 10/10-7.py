#10-6 Addition Calculator

print("This program will add any two integers you enter.")
#idea: program has to keep going until the user's input is an int, adds two ints together

def get_input():
    while True:
        try:
            int1 = input("Enter a number: ")
            int1 = int(int1)
        except ValueError:
                print ("sorry that's not an integer! try again: ")
                continue
            #this is the magic word to return to the start, until the user enters an integer
        else:
            break #exits and goes to to the next number!
    while True:
        try:
            int2 = input ("Enter another number: ")
            int2 = int(int2)
        except ValueError:
            print (f"sorry {int2} not an integer! try again: ")
            continue
        else:
            answer = int1 + int2
            print (f"{int1} + {int2} = {answer}")
            break
get_input()
