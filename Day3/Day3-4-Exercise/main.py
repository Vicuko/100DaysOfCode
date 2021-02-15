# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
pizza_size = ["S", "M", "L"]
pepperoni_added = ["N", "Y"]
cheese_added = ["N", "Y"]

pizza_price = 15 + pizza_size.index(size) * 5
pepperoni_price = pepperoni_added.index(add_pepperoni)*(2)

if pizza_size != "S" and add_pepperoni == "Y":
    pepperoni_price += 1

cheese_price = cheese_added.index(extra_cheese) * 1

total_price = pizza_price + pepperoni_price + cheese_price
print(f"Your final bill is: ${total_price}.")
