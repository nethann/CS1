
#defining variables
Principal = int(input("Please enter the loan principal: "))
Term = int(input("Please enter the laon term in months: "))
Rate = float(input("Please enter the annual interest rate of the loan in decimal: "))
amount = Principal*(1+Rate/12)**Term-Principal

#printing output
print(f'Amount of interest in this loan: {amount}')
