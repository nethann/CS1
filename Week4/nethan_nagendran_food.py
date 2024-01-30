menu_item = {
    'Hot_dog': 1.50,
    'slice_of_pizza': 1.99,
    'whole_pizza': 9.95,
    'soft_drink': 0.59,
}


hot_dogs_input = int(input("Please enter the number of Hot Dogs: "))
pizza_slices_input = int(input("Please enter the number of Pizza Slices: "))
whole_pizza_input = int(input("Please enter the number of Whole Pizzas: "))
soft_drink_input = int(input("Please enter the number of Soft Drinks: "))


Total = (menu_item["Hot_dog"] * hot_dogs_input) + (menu_item["slice_of_pizza"] * pizza_slices_input) + (menu_item["whole_pizza"] * whole_pizza_input) + (menu_item["soft_drink"] * soft_drink_input)

print("The total cost of the order is", "{:.2f}".format(Total))
