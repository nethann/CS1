cents = int(input("Please enter the cents you need to convert: "))
Quarter_Values = 25
Dime_Values = 10
Nickel_Values = 5
Penny_Values = 1

Quarters = cents // Quarter_Values
Quarters_Remainder = cents % Quarter_Values
Dimes = Quarters_Remainder // Dime_Values
Dimes_Remainder = Quarters_Remainder % Dime_Values
Nickles = Dimes_Remainder // Nickel_Values
Nickles_Remainder = Dimes_Remainder % Nickel_Values
Pennies = Nickles_Remainder // Penny_Values

# Display the results
print(f'Coins: Quarters:{Quarters} Dimes:{Dimes} Nickels:{Nickles} Pennies:{Pennies}')