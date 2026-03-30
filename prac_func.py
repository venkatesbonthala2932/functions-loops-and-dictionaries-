def div_1():
    while True:
        try:
            num1,num2 = map(int, input("Enter the first and second numbers separated by a comma: ").split(","))
            print(f"The result of {num1} divided by {num2} is: {num1 / num2}")
            break
        except ValueError:
            print("Invalid input. Please enter integers.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero second number.")
div_1()
