MENU = {
    "espresso": {"water": 50, "coffee": 18, "milk": 0, "cost": 1.5},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "cost": 2.5},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "cost": 3.0}
}
resources = {"water": 300, "coffee": 100, "milk": 200, "revenue": 0 }
coin_values = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}

def money():
    total = coin_values["quarter"]*quarter + coin_values["dime"]*dime + coin_values["nickel"]*nickel + coin_values["penny"]*penny
    return total
revenue = 0
while resources["water"] >0 and resources["coffee"] >0 and resources["milk"] >0 :
    
    print("WELCOME TO THE COFFEE MACHINE!\nready to age fast, drinking caffine all day long?!")

    coffee_type = input("what would you like to have today? (espresso, latte, cappuccino)\nor if you need the resources left details, type (report):\n").lower()
    
    if coffee_type =="off":
        print("machine is shutting down! BYE!")
        break
    if coffee_type == "report":
        print(resources)
        coffee_type = input("what would you like to have today? (espresso, latte, cappuccino)\nor if you need the resources left details, type (report):\n").lower()

    quarter = int(input("how many quarter? : "))
    dime =  int(input("how many dime? : "))
    nickel = int(input("how many nickel? : "))
    penny = int(input("how many penny? : "))

    
    if coffee_type == "espresso":
        if (MENU["espresso"]["water"] <= resources["water"]) and (MENU["espresso"]["coffee"] <= resources["coffee"]) and (MENU["espresso"]["milk"] <= resources["milk"]):
            
            if money() >= MENU["espresso"]["cost"]:
                balance = money() - MENU["espresso"]["cost"]
                print(f"here is your espresso☕! and here is your balance chance ${round(balance,2)}")
                next = input("type 'n' to make cofee again!").lower()
                if next == "n":
                    print("\n"*50)
                resources["water"] -= MENU["espresso"]["water"]
                resources["coffee"] -= MENU["espresso"]["coffee"]
                resources["milk"] -= MENU["espresso"]["milk"]
                resources["revenue"] += MENU["espresso"]["cost"]
                

            else:
                print(f"sorry begger! you can't afford this with this money!\n here is your refunded money: {money()}")
        
        else:
            print("sorry, we dont have enough resourses right now!!")

    if coffee_type == "latte":
        if (MENU["latte"]["water"] <= resources["water"]) and (MENU["latte"]["coffee"] <= resources["coffee"]) and (MENU["latte"]["milk"] <= resources["milk"]):

            if money() >= MENU["latte"]["cost"]:
                balance = money() - MENU["latte"]["cost"]
                print(f"here is your latte☕! and here is your balance chance ${round(balance,2)}")
                next = input("type 'n' to make cofee again!").lower()
                if next == "n":
                    print("\n"*50)
                resources["water"] -= MENU["latte"]["water"]
                resources["coffee"] -= MENU["latte"]["coffee"]
                resources["milk"] -= MENU["latte"]["milk"]
                resources["revenue"] += MENU["latte"]["cost"]

            else :
                print(f"sorry begger! you can't afford this with this money!\n here is your refunded money: {money()}")
        
        else:
            print("sorry, we dont have enough resourses right now!!")

    if coffee_type == "cappuccino":
        if (MENU["cappuccino"]["water"] <= resources["water"]) and (MENU["cappuccino"]["coffee"] <= resources["coffee"]) and (MENU["cappuccino"]["milk"] <= resources["milk"]):
            
            if money() >= MENU["cappuccino"]["cost"]:
                balance = money() - MENU["cappuccino"]["cost"]
                print(f"here is your cappuccino☕! and here is your balance chance ${round(balance,2)}")
                next = input("type 'n' to make cofee again!").lower()
                if next == "n":
                    print("\n"*50)
                resources["water"] -= MENU["cappuccino"]["water"]
                resources["coffee"] -= MENU["cappuccino"]["coffee"]
                resources["milk"] -= MENU["cappuccino"]["milk"]
                resources["revenue"] += MENU["cappuccino"]["cost"]

            else:
                print(f"sorry begger! you can't afford this with this money!\n here is your refunded money: {money()}")
        
        else:
            print("sorry, we dont have enough resourses right now!!")
    else:
        print("type the correct spelling!!")
print("not enough resources! machine is shutting down!\naccess after refill! now shoo...")
print("refilling... \n\n\npress RUN to complete refill!!")