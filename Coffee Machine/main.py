from sys import exit


class CoffeeMachine:
    """
    The coffee machine have 400 ml of water, 540 ml of milk, 
    120 g of coffe beans, 9 disposable cups, $550 in cash.
    """
    water = 400  # in ml
    milk = 540  # in ml
    beans = 120  # in g
    cups = 9
    money = 550  # in $
    
    def __init__(self):
        self.buy = None
        self.fill = None
        self.take = None
        self.remaining = None
        self.exit = None
    
    def action(self, arg=None):
        self.arg = input()
        
        if self.arg == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:)")
            
            self.kind = input()
            if self.kind == "1" and c.water >= 250 and c.beans >= 16:
                # After buying espresso
                c.water -= 250
                c.beans -= 16
                c.money += 4
                c.cups -= 1
                
                print("")
                print("I have enough resources, making you a coffee!")
            elif self.kind == "2" and c.water >= 350 and c.milk >= 75 and c.beans >= 20:
                # After buying latte
                c.water -= 350
                c.milk -= 75
                c.beans -= 20
                c.money += 7
                c.cups -= 1
    
                print("")
                print("I have enough resources, making you a coffee!")
                
            elif self.kind == "3" and c.water >= 200 and c.milk >= 100 and c.beans >= 12:
                # After buying cappuccino
                c.water -= 200
                c.milk -= 100
                c.beans -= 12
                c.money += 6
                c.cups -= 1
    
                print("I have enough resources, making you a coffee!")
                print("")
                
            elif self.kind == "1" and c.water < 250:
                print("Sorry, not enough water!")
                print("")
                
            elif self.kind == "1" and c.beans < 16:
                print("Sorry, not enough beans!")
                print("")
                
            elif self.kind == "2" and c.water < 350:
                print("Sorry, not enough water!")
                print("")
                
            elif self.kind == "2" and c.milk < 75:
                print("Sorry, not enough milk!")
                print("")
                
            elif self.kind == "2" and c.beans < 20:
                print("Sorry, not enough coffee beans!")
                print("")
                
            elif self.kind == "3" and c.water < 200:
                print("Sorry, not enough water!")
                print("")
                
            elif self.kind == "3" and c.milk < 100:
                print("Sorry, not enough milk!")
                print("")
                
            elif self.kind == "3" and c.beans < 12:
                print("Sorry, not enough coffee beans!")
                print("")
                
            else:
                pass
        elif self.arg == "exit":
            exit(0)
        
        elif self.arg == "fill":
            # Introduce the content of the coffee machine
            print("Write how many ml of water do you want to add:")
            self.added_water = input("")
            print("Write how many ml of milk do you want to add:")
            self.added_milk = input("")
            print("Write how many grams of coffee beans do you want to add:")
            self.added_beans = input("")
            print("Write how many disposable cups of coffee do you want to add:")
            self.added_cups = input("")
            
            # Update the values after the fill
        
            self.water += int(self.added_water)
            self.milk += int(self.added_milk)
            self.beans += int(self.added_beans)
            self.cups += int(self.added_cups)
            
        elif self.arg == "remaining":
            print("")
            print("The coffee machine has:")
            print(f"{self.water} of water")
            print(f"{self.milk} of milk")
            print(f"{self.beans} of coffee beans")
            print(f"{self.cups} of disposable cups")
            print(f"${self.money} of money")
            print("")
        
        else:
            print("")
            print(f"I gave you ${self.money}")
            self.money -= self.money


if __name__ == "__main__":
    c = CoffeeMachine()
    while True:
        print("Write action (buy, fill, take, remaining, exit):")
        c.action()
