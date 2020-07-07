"""Coffee machine simulation
1- For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans. 
It costs $4.
2- For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans.
It costs $7.
3- And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee. 
It costs $6.

At the moment, the coffee machine has 
$550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups
"""


# Print the state of the coffee machine
print("The coffee machine has:")
print("400 of water")
print("540 of milk")
print("120 of coffee beans")
print("9 of disposable cups")
print("550 of money")
print("")

def buy(choice):
  # Introduce the content of the coffee machine
  water = 400  # in ml
  milk = 540  # in ml
  beans = 120  # in g
  cups = 9
  money = 550  # in $
  
  if choice == 1:
    print(choice)
    # After buying espresso
    water -= 250
    beans -= 16
    milk = milk
    money += 4
    cups -= 1
    
  elif choice == 2:
    # After buying latte
    print(choice)
    water -= 350
    milk -= 75
    beans -= 20
    money += 7
    cups -= 1
  
  elif choice == 3:
    # After buying cappuccino
    print(choice)
    water -= 200
    milk -= 100
    beans -= 12
    money += 6
    cups -= 1
  else:
    pass

  print("")
  print("The coffee machine has:")
  print(f"{water} of water")
  print(f"{milk} of milk")
  print(f"{beans} of coffee beans")
  print(f"{cups} of disposable cups")
  print(f"{money} of money")

def fill():
  # Introduce the content of the coffee machine
  water = 400  # in ml
  milk = 540  # in ml
  beans = 120  # in g
  cups = 9
  money = 550  # in $

  print("Write how many ml of water do you want to add:")
  added_water = int(input("> "))
  print("Write how many ml of milk do you want to add:")
  added_milk = int(input("> "))
  print("Write how many grams of coffee beans do you want to add:")
  added_beans = int(input("> "))
  print("Write how many disposable cups of coffee do you want to add:")
  added_cups = int(input("> "))

  # Update the values after the fill
  water += added_water
  milk += added_milk
  beans += added_beans
  cups += added_cups
  money = money

  print("")
  print("The coffee machine has:")
  print(f"{water} of water")
  print(f"{milk} of milk")
  print(f"{beans} of coffee beans")
  print(f"{cups} of disposable cups")
  print(f"{money} of money")


def take():
  # Introduce the content of the coffee machine
  water = 400  # in ml
  milk = 540  # in ml
  beans = 120  # in g
  cups = 9
  money = 550  # in $

  print(f"I gave you ${money}")

  money -= money

  print("")
  print("The coffee machine has:")
  print(f"{water} of water")
  print(f"{milk} of milk")
  print(f"{beans} of coffee beans")
  print(f"{cups} of disposable cups")
  print(f"{money} of money")

# Print the action to be done
print("Write action (buy, fill, take):")

# Input the function choice either buy,fill or take
choice1 = input("> ")

# The choice is buy
if choice1 == "buy":
  print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
  choice2 = int(input("> "))
  buy(choice2)


# The choice is fill
elif choice1 == "fill":
  # Introduce the content of the coffee machine
  fill()

# The choice is take
else:
  take()

