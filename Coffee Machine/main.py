"""Coffee machine simulation

The user can buy, fill, take, see the remaining or exit from the coffee machine

1- For one espresso, the coffee machine needs 250 ml of water and 16 g of coffee beans.
It costs $4.
2- For a latte, the coffee machine needs 350 ml of water, 75 ml of milk, and 20 g of coffee beans.
It costs $7.
3- And for a cappuccino, the coffee machine needs 200 ml of water, 100 ml of milk, and 12 g of coffee.
It costs $6.

At the moment, the coffee machine has
$550, 400 ml of water, 540 ml of milk, 120 g of coffee beans, and 9 disposable cups
"""

# Import the sys library
import sys


def main():
    # The state of the coffee machine
    water = 400  # in ml
    milk = 540  # in ml
    beans = 120  # in g
    cups = 9
    money = 550  # in $

    while True:
        # Print the action to be done
        print("Write action (buy, fill, take, remaining, exit):")

        # Input the function choice either buy,fill or take
        choice1 = input("")

        # The choice is buy
        if choice1 == "buy":
            print("")
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            choice = input("")
            # Go back to the buy menu
            if choice == "back":
                main()

            elif int(choice) == 1 and water >= 250 and beans >= 16:
                # After buying espresso
                water -= 250
                beans -= 16
                money += 4
                cups -= 1

                print("")
                print("I have enough resources, making you a coffee!")

            elif int(choice) == 2 and water >= 350 and milk >= 75 and beans >= 20:
                # After buying latte
                water -= 350
                milk -= 75
                beans -= 20
                money += 7
                cups -= 1

                print("")
                print("I have enough resources, making you a coffee!")

            elif int(choice) == 3 and water >= 200 and milk >= 100 and beans >= 12:
                # After buying cappuccino
                water -= 200
                milk -= 100
                beans -= 12
                money += 6
                cups -= 1

                print("I have enough resources, making you a coffee!")
                print("")

            elif int(choice) == 1 and water < 250:
                print("Sorry, not enough water!")
                print("")

            elif int(choice) == 1 and beans < 16:
                print("Sorry, not enough coffee beans!")
                print("")

            elif int(choice) == 2 and water < 350:
                print("Sorry, not enough water!")
                print("")

            elif int(choice) == 2 and milk < 75:
                print("Sorry, not enough milk!")
                print("")

            elif int(choice) == 2 and milk < 20:
                print("Sorry, not enough coffee beans!")
                print("")

            elif int(choice) == 3 and water < 200:
                print("Sorry, not enough water!")
                print("")

            elif int(choice) == 3 and milk < 100:
                print("Sorry, not enough milk!")
                print("")

            elif int(choice) == 3 and beans < 12:
                print("Sorry, not enough coffee beans!")
                print("")

            else:
                pass

        # The choice is fill
        elif choice1 == "fill":
            # Introduce the content of the coffee machine
            print("Write how many ml of water do you want to add:")
            added_water = int(input(""))
            print("Write how many ml of milk do you want to add:")
            added_milk = int(input(""))
            print("Write how many grams of coffee beans do you want to add:")
            added_beans = int(input(""))
            print("Write how many disposable cups of coffee do you want to add:")
            added_cups = int(input(""))

            # Update the values after the fill
            water += added_water
            milk += added_milk
            beans += added_beans
            cups += added_cups

        # The choice is take
        elif choice1 == "take":

            print("")
            print(f"I gave you ${money}")
            money -= money

        elif choice1 == "remaining":
            print("")
            print("The coffee machine has:")
            print(f"{water} of water")
            print(f"{milk} of milk")
            print(f"{beans} of coffee beans")
            print(f"{cups} of disposable cups")
            print(f"{money} of money")
            print("")

        elif choice1 == "exit":
            sys.exit()

        else:
            pass


if __name__ == "__main__":
    main()
