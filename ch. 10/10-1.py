#10-1 reading files

file = 'learning_python.txt'

with open(file) as file_object:
    contents = file_object.read()
    print (contents.rstrip())
print ("1")
with open(file) as file_object:
    for line in file_object:
        print(line.rstrip())
print ("2")
with open(file) as file_object:
          lines = file_object.readlines()
for line in lines:
    print(line.rstrip())
print("3")
