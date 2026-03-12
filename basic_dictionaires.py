n=int(input("Enter the number of key-value pairs you want to add: "))
null_dict={}    
for i in range(n):
    null_dict={ input("Enter the key: "): input("Enter the value: ") }
print(null_dict)
null_dict=list(null_dict.keys())
print(null_dict)
null_dict=set(null_dict)
print(null_dict)