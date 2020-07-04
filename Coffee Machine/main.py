"""Coffee machine simulation
To make coffee you need 200ml of water, 50ml of milk and 15g of beans""" 

# Ask the user for how much water does he need
print("Write how many ml of water the coffee machine has:")
water = int(input("> "))

# Ask the user for how much milk does he need 
print("Write how many ml of milk the coffee machine has:")
milk = int(input("> "))

# Ask the user for how many grams of coffee beans he needs
print("Write how many grams of coffee beans the coffee machine has:")
beans = int(input("> "))

# Ask the user of how many cups of coffee he needs
print("Write how many cups of coffee you will need:")
cups = int(input("> "))

# The values of water, milk and beans needed
water_needed = 200
milk_needed = 50
beans_needed = 15

# The ratios of water, milk and beans
water_ratio = water // water_needed
milk_ratio = milk // milk_needed
beans_ratio = beans // beans_needed

# The min ratio
min_ratio = min(water_ratio, milk_ratio, beans_ratio)

if water_ratio > 0 and milk_ratio > 0 and beans_ratio > 0 and min_ratio < cups:
  print(f"No, I can make only {min_ratio} cups of coffee")
elif water_ratio > 0 and milk_ratio > 0 and beans_ratio > 0 and min_ratio > cups:
  print(f"Yes, I can make that amount of coffee (and even {min_ratio-cups} more than that)")
elif water_ratio == 0 and milk_ratio == 0 and beans_ratio == 0 and cups != 0:
  print(f"No, I can make only {water_ratio} cups of coffee")
else:
  print("Yes, I can make that amount of coffee")
