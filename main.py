# Shared drink recipes
drink_recipes = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Initial resources
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report(resources):
    print("Current resources:")
    for resource, amount in resources.items():
        print(f"{resource.capitalize()}: {amount}")

def is_resource_sufficient(drink_name, resources):
    drink = drink_recipes.get(drink_name)
    if not drink:
        print("Invalid drink choice.")
        return False
    
    for ingredient, amount in drink["ingredients"].items():
        if resources.get(ingredient, 0) < amount:
            return False
    return True

def make_drink(drink_name, resources):
    drink = drink_recipes.get(drink_name)
    if not drink:
        print("Invalid drink choice.")
        return

    if is_resource_sufficient(drink_name, resources):
        for ingredient, amount in drink["ingredients"].items():
            resources[ingredient] -= amount
        print(f"Here is your {drink_name}. Enjoy!")
    else:
        print("Unable to make the drink due to insufficient resources.")

def turn_off_machine(user_input):
    if user_input == "off":
        print("Turning off the machine...")
        return True
    return False

def user_choice():
    return input("What would you like? (espresso/latte/cappuccino): ")

def process_payment(cost):
    print(f"Please insert coins. The cost is ${cost:.2f}.")
    quarters = int(input("How many quarters? "))  
    dimes = int(input("How many dimes? "))      
    nickels = int(input("How many nickels? "))  
    pennies = int(input("How many pennies? "))  

    total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    
    if total_amount >= cost:
        change = total_amount - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
    else:
        print(f"Sorry, that's not enough money. You inserted ${total_amount:.2f}.")
        return False

def resources_sufficient_for_any_drink(resources):
    for drink_name in drink_recipes:
        if is_resource_sufficient(drink_name, resources):
            return True
    return False

def coffee_machine():
    while True:
        if not resources_sufficient_for_any_drink(resources):
            print("Sorry, we're out of resources. Please restock.")
            break
        
        choice = user_choice()
        if turn_off_machine(choice):
            break

        drink = drink_recipes.get(choice)
        if drink and is_resource_sufficient(choice, resources):
            if process_payment(drink["cost"]):
                make_drink(choice, resources)
        else:
            print("Unable to make the drink due to insufficient resources.")
        
        print_report(resources)  # Show resources after each operation

# Example usage
coffee_machine()