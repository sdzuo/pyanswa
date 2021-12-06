#10-3 Guest

prompt = input("Please enter your name: ")
file = 'guest.txt'

with open(file,'w') as fobject:
    fobject.write(prompt.title())
