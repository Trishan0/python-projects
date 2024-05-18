print("This is a simple Calculator")

history = []
result = None
while True:

    print("Select the operation you want to do (type it) ,")
    operation = input(
        "1. Addition = + \n"
        "2. Subtraction = -\n"
        "3. Multiplication = *\n"
        "4. Division = / \n"
        "5. Modulus = % \n"
        "6. Exponentiation = **\n"
        "7. Floor Division = // \n"
        "8. Exit = type 'Exit' \n"
        "9. History = type '?' \n"
        "Enter your operation : "
    )
    if operation.lower() == "exit":
        print("Exiting the Program")
        break
    if operation == "?":
        if len(history) == 0:
            print("No any past calculations \n")
            continue
        else:
            print(history)

    num1 = int(input("Enter the 1st number : "))
    num2 = int(input("Enter the 2nd number : "))

    if operation == "+":
        result = num1.__add__(num2)
        print(result, "\n")
    if operation == "-":
        result = num1.__sub__(num2)
        print(result, "\n")
    if operation == "*":
        result = num1.__mul__(num2)
        print(result, "\n")
    if operation == "/":
        result = num1.__truediv__(num2)
        print(result, "\n")
    if operation == "%":
        result = num1.__mod__(num2)
        print(result, "\n")
    if operation == "**":
        result = num1.__pow__(num2)
        print(result, "\n")
    if operation == "//":
        result = num1//num2
        print(result, "\n")

    history.append(f"{num1} {operation} {num2} = {result}")
