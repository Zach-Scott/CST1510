
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

n1 = float(input("Enter the first number: "))

keep_going = True

while keep_going:
    operator = input("Enter an operator (+, -, *, /): ")
    n2 = float(input("Enter the second number: "))

    if operator == "+":
        result = add(n1, n2)
    elif operator == "-":
        result = subtract(n1, n2)
    elif operator == "*":
        result = multiply(n1, n2)
    elif operator == "/":
        result = divide(n1, n2)
    else:
        print("Invalid operator")
        continue

    print(n1, operator, n2, "=", result)

    choice = input("Type 'y' to continue with the result, or 'n' to start over: ")

    if choice == "y":
        n1 = result
    else:
        n1 = float(input("Enter a new first number: "))