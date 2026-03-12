# n= int ( input("enter to find the factorial : "))
# for i in range(1, n+1):
#     n = n *n - i
#     i-=1
# print(n)
	
# lst=list(input("enter the numbers with comma separated : ").split(','))
# def print_list_length(lst):
# 	return len(lst)
# print(print_list_length(lst))


def converter(ind_rupee):
	print(f"the converted {ind_rupee} is {ind_rupee*92.18}")
converter(int(input("enter the amount in indian rupees : ")))
	