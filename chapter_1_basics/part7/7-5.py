age = int(input("Please enter your age: "))

message = "The price of your ticket is "
price = ""

if age < 3:
    price = "free of charge"
elif 3 <= age <= 12:
    price = "$10"
else:
    price = "$15"

print(message + price)

