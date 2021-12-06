#10-9

file1 = 'cats.txt'
file2 = 'dogs.txt'
try:
    with open(file1) as f1:
        print (f"Attempting to read {file1}...")
        contents = f1.read()
        print (contents.rstrip())
        print()
except FileNotFoundError:
    pass
try:
    with open(file2) as f2:
        print (f"Attempting to read {file2}...")
        contents = f2.read()
        print (contents.rstrip())
except FileNotFoundError:
    pass
