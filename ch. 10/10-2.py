#10-2 Learning C:

file = 'learning_python.txt'

#replace method does not exist on a file object
#replace method exists with strings, so we convert the objects into
# a string called contents and then we can replace it
# can be done diff ways


with open(file) as file_object:
    contents = file_object.read()
    print(contents.replace('Python','C++').rstrip())
# the above is one way

# can also do:
# contents = file_object.read().replace('Python','C++')
# print(contents.rstrip())
print ("1")
print()
with open(file) as file_object:
    for line in file_object:
        print(line.replace('Python','C++').rstrip())
print ("2")
with open(file) as file_object:
          lines = file_object.readlines()
for line in lines:
    print(line.replace('Python','C++').rstrip())
print("3")
