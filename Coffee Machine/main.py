# This is a program that simulates a coffee machine


# Ask the user for how many cups of coffee he needs
print("Write how many cups of coffee you will need:")

# Input from the command line
cups = int(input("> "))
print(f"For {cups} cups of coffee you will need:")

# Calculate how much water, milk and coffee beans
water = cups * 200
milk = cups * 50
coffee_beans = cups * 15

# Print the total ammount of water, milk and coffee beans
print(f"{water} ml of water")
print(f"{milk} ml of milk")
print(f"{coffee_beans} g of coffee beans")