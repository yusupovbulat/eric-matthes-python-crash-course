pizza_toppings = "\nPlease enter the desired pizza toppings: "
pizza_toppings += "\n(Enter 'quit' when you are finished) "

flag = True

while flag:
    toppings = input(pizza_toppings)
    if toppings == 'quit':
        flag = False
    else:
        print("The topping of the " + toppings + " will be added to the pizza!")

