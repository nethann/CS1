
def addition(left, right): 
    return left + right 

def subtraction(left, right): 
    return left - right 

def multiplication(left, right): 
    return left * right 

def division(left, right): 
    if right != 0:
        return left / right 
    else:
        return "Error: Division by zero"

def modulus(left, right): 
    if right != 0:
        return left % right 

def power(left, right): 
    return left ** right 

def floor_division(left, right): 
    if right != 0:
        return left // right 
    else:
        return "Error: Floor division by zero"

while True: 
    calculator_input = input(":> ")
    expression = calculator_input.split()

    if calculator_input.lower() == 'quit': 
        break

    if len(expression) != 3:
        print("Error: Invalid input format")
        continue

    
    left = float(expression[0])
    operator = expression[1]
    right = float(expression[2])
    # except ValueError:
    #     print("Error: Invalid input format")
    #     continue

    if operator == "+": 
        print(addition(left, right))
    elif operator == "-": 
        print(subtraction(left, right))
    elif operator == "*":
        print(multiplication(left, right))
    elif operator == "/":
        print(division(left, right))
    elif operator == "%":
        print(modulus(left, right))
    elif operator == "**":
        print(power(left, right))
    elif operator == "//":
        print(floor_division(left, right))
    else:
        print("Error: Invalid operator")
