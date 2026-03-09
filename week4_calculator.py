while True:
    def addition(a, b):
        return a + b
    
    def subtraction(a, b):
        return a - b

    def multiplication(a, b):
        return a * b

    def division(a, b):
        if b == 0:
            print("\nSyntax error!")
            pass
        else:
            return a / b

    def checkoperator(a):
        match a:
            case 1:
                return addition(num1, num2)
            case 2:
                return subtraction(num1, num2)
            case 3:
                return multiplication(num1, num2)
            case 4:
                return division(num1, num2)
            case _:
                print("\nInvalid operator!")
            
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nOperators: \n")
    print("1: Addition\n")
    print("2: Subtraction\n")
    print("3: Multiplication\n")
    print("4: Division\n")

    operator = int(input("Enter operator: "))
    answer = checkoperator(operator)

    print(f"\nThe answer is {answer}. \n")
    print("==========================================\n")
