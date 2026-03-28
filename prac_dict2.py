a= int(input("enter the number of students you want to add : "))
def student_info():
    dict_1 = {}
    for i in range(a):
        name=input("Enter the name: ")
        age=int(input("Enter the age: "))
        dict_1["name"]=name 
        dict_1["age"]=age
        dict_1["subjects"]={"python":int(input("Enter the python score: ")), "java":int(input("Enter the java score: ")), "c++":int(input("Enter the c++ score: "))}
        if dict_1["subjects"]["python"]>=30 and dict_1["subjects"]["java"]>=30 and dict_1["subjects"]["c++"]>=30:
            dict_1.update({"grades": "passed"})
            print(dict_1)
        else:
            dict_1.update({"grades": "failed"})
            print(dict_1)
student_info()
