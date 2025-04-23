
data = eval(input("Enter a list: "))
element_to_find = eval(input("Enter the element whose position you want to find: "))


def find_element(data, element):
    for i, item in enumerate(data):
        if item == element:
            return f"{element} found at position [{i}]"
        elif isinstance(item, list) and element in item:
            return f"{element} found at position [{i}][{item.index(element)}]"
    return f"{element} not found in the list."


print(find_element(data, element_to_find))
