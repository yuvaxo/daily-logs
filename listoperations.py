
user_input = input("Enter a list: ")
data = eval(user_input)  
found = False


for i in range(len(data)):
    if isinstance(data[i], list):
        for j in range(len(data[i])):
            if data[i][j] == 5:
                print(f"5 found at position [{i}][{j}]")
                found = True
    else:
        if data[i] == 5:
            print(f"5 found at position [{i}]")
            found = True

if not found:
    print("5 not found in the list.")
