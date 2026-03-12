#printing numbers from 0 to 100
i=0
while i<=100:
    print(i)
    i+=1
#printing numbers from 100 to 0
while i>=1:
    print(i)
    i-=1


#printing multiplication table of a number
n=int (input("enter the number for multiplication : "))
for i in range (1, 11):
    print(f"{n} x {i} = {n*i}  ")
lst=[1,4,9,16,25,36,49,64,81,100]
for i in range (len(lst)):
    print(f"the square root of {lst[i]} is {i+1}")


#searching for an element in a tuple
lst=tuple(lst)
srch=int(input("enter the number to search in the tuple : "))
for i in range (len(lst)):
    if lst[i]==srch:
        print(f"{srch} is found at index {i}")
        break
else:
    print(f"{srch} is not found in the list")