
num_floating_point = int(input("Please enter the number of floating-point values: "))

empty_list = []
for i in range(0, num_floating_point): 
    floating_point_val = float(input("Please enter a floating-point values: "))
    empty_list.append(f'{floating_point_val/100:.2f}')


print("Normalized Floating-Point Values: ")
for elements in empty_list: 
    print(elements)