def div_1():
    while True:
        try:
            a = input (" enter your name :  ")
            b= int(input (" enter your age :  ") )
            with open("users.txt","r+") as f:
                f.write(f"{a}\n{b}\n")
            return a , b 
        except ValueError:
            print("Invalid input. Please try again.")

def div_2():
    global user_input
    user_input = input (" enter yes if you want append to the file ").lower()
    while user_input == "yes":
        try :
                a= input (" enter your name :  ")
                b= int(input (" enter your age :  ") )  
                with open("users.txt","a") as f:
                    f.write(f"{a}\n{b}\n")
                    break
        
        except ValueError:
            print("No user data to append. Please run div_1() first.")

def div_3():
    with open("users.txt","r") as f:
        for line in f:
            print(line.strip())
div_1()
div_2()
div_3()
