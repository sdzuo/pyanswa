#10-4 Guest Book

file = 'guest_book.txt'

#we have to open the file first or else when we write to the file, it will only write the last
#  line of input!
with open(file,'w') as fobject:
    while True:
        prompt = input("enter your name. enter 'q' to quit: ")
        if prompt != 'q':
            print (f"Greetings {prompt.title()}, your name will be added to the guest book.")
            fobject.write(f"{prompt.title()}\n")
        elif prompt == 'q':
            print("Thank you, goodbye.")
            break
