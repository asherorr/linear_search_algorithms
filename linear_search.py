def linear_search(lst, target):
    #Returns the index position of the target if found, else returns None
    for index, value in enumerate(lst):
        if value == target:
            return index
    return None


def verify(index_value):
    if index_value is not None:
        print(f"Target found at {index_value}")
    else:
        print("Target not found in list.")
        
numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)
