#10-8

file1 = 'cats.txt'
file2 = 'dogs.txt'
try:
    with open(file1) as f1:
        print (f"Attempting to read {file1}...")
        contents = f1.read()
        print (contents.rstrip())
        print()
except FileNotFoundError:
    print(f"Sorry, the file {file1} does not exist.")
try:
    with open(file2) as f2:
        print (f"Attempting to read {file2}...")
        contents = f2.read()
        print (contents.rstrip())
except FileNotFoundError:
    print(f"Sorry, the file {file2} does not exist.")
