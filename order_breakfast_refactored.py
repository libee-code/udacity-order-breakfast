
import time


def print_pause(message):  # refactoring to remove repetition
    print(message)
    time.sleep(2)


def intro():  # distinct purpose therefore turn into function
    print_pause("Hello! I am Bob, the Breakfast Bot.")
    print_pause("Today we have two breakfasts available.")
    print_pause("The first is waffles with strawberries and whipped cream.")
    print_pause("The second is sweet potato pancakes with butter and syrup.")


def valid_input(prompt, option1, option2):  # checks for valid input
    while True:
        response = input(prompt).lower()
        if option1 in response:
            return response
        elif option2 in response:
            return response
        else:
            print_pause("Sorry, I don't understand.")


def get_order():  # distinct purpose therefore turn into function
    response = valid_input(
        "Please place your order. Would you like waffles or pancakes?\n", "waffles", "pancakes")
    if "waffles" in response:
        print_pause("Waffles it is!")
    elif "pancakes" in response:
        print_pause("Pancakes it is!")
    print_pause("Your order will be ready shortly.")


def order_again():
    response = valid_input(
        "Would you like to place another order? Please say 'yes' or 'no'.\n", "yes", "no")
    if 'no' in response:
        print_pause("OK, goodbye!")
    elif 'yes' in response:
        print_pause("Very good, I'm happy to take another order.")
        get_order()


def order_breakfast():
  intro()
  get_order()
  order_again()

order_breakfast() # single entry point - one line controls whether entire program will run. Entry point - place in code that gets everything started.


