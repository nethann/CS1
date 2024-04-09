class Number:
  def __init__(self, num):
      self.num = num

  def __str__(self):
      return str(self.num)

  def __add__(self, other):
      return Number(self.num + other.num)

  def __sub__(self, other):
      return Number(self.num - other.num)

  def __mul__(self, other):
      return Number(self.num * other.num)

  def __truediv__(self, other):
      return Number(self.num // other.num)  

def evaluate_expression(expression):
  try:
      while '(' in expression:
          start_index = expression.rfind('(')
          end_index = start_index + expression[start_index:].find(')')
          sub_expression = expression[start_index + 1:end_index]
          result = evaluate_expression(sub_expression)
          expression = expression[:start_index] + str(result) + expression[end_index + 1:]

      parts = expression.split()
      num1 = Number(int(parts[0]))
      for i in range(1, len(parts), 2):
          operator = parts[i]
          num2 = int(parts[i + 1])

          if operator == '+':
              num1 = num1 + Number(num2)
          elif operator == '-':
              num1 = num1 - Number(num2)
          elif operator == '*':
              num1 = num1 * Number(num2)
          elif operator == '/':
              num1 = num1 / Number(num2)
          else:
              return "Invalid operator. Please use +, -, *, or /."

      return num1
  except ValueError:
      return "Invalid input. Please enter a valid expression (e.g., 30 + 40)."

user_expression = input("Enter an arithmetic expression: ")
result = evaluate_expression(user_expression)
print(f"Result: {result}")
