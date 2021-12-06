#10-10 Common Words from Frankenstein

file = 'frankenstein.txt'

with open(file, encoding = 'utf-8') as f:
    contents = f.read()
    counter1 = contents.count('the')
    print (f"The number of times 'the' appears in {file} is {counter1}.")
    counter2 = contents.count('the ')
    print (f"The number of times 'the ' appears in {file} is {counter2}.")
    diff = int(counter1) - int(counter2)
    print(f"The difference between the two is {diff}.")
