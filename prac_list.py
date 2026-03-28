a = list(input("enter the numbers for the list : ").split(','))
def print_list_length(a):
    a.sort()
    global b
    b = a
    return len(a), b

print(print_list_length(a))
print(b)
