#10-5 Programming Poll

file = 'programming_poll.txt'

#'a' to append so whenever this .py is run we don't overwrite existing data
with open(file,'a') as fobject:
    while True:
        prompt = input ("Why do you like programming? Enter 'q' to quit. ")
        if prompt != 'q':
            fobject.write(f"{prompt}\n")
        elif prompt == 'q':
            print ("Thanks for doing the poll.")
            break
