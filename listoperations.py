
user_input = input("Enter a list: ")
element_to_find = input("Enter the element whose position you want to find: ")


data = eval(user_input)  
try:
    element_to_find = eval(element_to_find)
except:
    pass  


found = False


for i in range(len(data)):
    if isinstance(data[i], list):
        for j in range(len(data[i])):
            if data[i][j] == element_to_find:
                print(f"{element_to_find} found at position [{i}][{j}]")
                found = True
    else:
        if data[i] == element_to_find:
            print(f"{element_to_find} found at position [{i}]")
            found = True

if not found:
    print(f"{element_to_find} not found in the list.")

