
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

    if calculator_input.lower() == 'quit' or calculator_input.lower() == 'q': 
        break

    if len(expression) != 3:
        print(f"Error: Invalid Expression - ({calculator_input}) ")
        continue

    
    left = float(expression[0])
    operator = expression[1]
    right = float(expression[2])


    if operator == "+": 
        print("Result: ",addition(left, right))
    elif operator == "-": 
        print("Result: ",subtraction(left, right))
    elif operator == "*":
        print("Result: ",multiplication(left, right))
    elif operator == "/":
        print("Result: ",division(left, right))
    elif operator == "%":
        print("Result: ",modulus(left, right))
    elif operator == "**":
        print("Result: ",power(left, right))
    elif operator == "//":
        print("Result: ",floor_division(left, right))
    else:
        print("Error: Invalid operator")



