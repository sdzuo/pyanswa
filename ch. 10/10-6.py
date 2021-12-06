#10-6 Addition

print("This program will add two numbers that you input.")

while True:
    try:
        prompt1 = input("Enter a number: ")
        prompt1 = int(prompt1)

    except ValueError:
        print (f"Sorry, {prompt1} is not a valid integer.")
        break
    try:
        prompt2 = input("Enter another number: ")
        prompt2 = int(prompt2)
    except ValueError:
        print (f"Sorry, {prompt2} is not a valid integer.")
        break
    else:
            answer = prompt1 + prompt2
            print (answer)
            break
    
    
