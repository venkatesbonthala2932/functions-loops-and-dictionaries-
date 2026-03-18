
user_marks=list(map(int, input("enter your marks : ").split(',')))
print(" marks entered by the user : ", user_marks)
sum_user=sum(user_marks)
print(sum_user)
avg= sum_user/len(user_marks)
print("Average marks : ", avg)
hihg_num=max(user_marks)
print("highest marks : ", hihg_num)
lowest_num=min(user_marks)
print("lowest marks : ", lowest_num)
a=0
b=0
def highest_and_lowest(user_marks):
    global a
    global b
    for i in range(len(user_marks)):
        if user_marks[i] > a:
            a = user_marks[i]
        elif user_marks[i] < b:
            b = user_marks[i]
    print("highest marks : ", a)
    print("lowest marks : ", b)

highest_and_lowest(user_marks)