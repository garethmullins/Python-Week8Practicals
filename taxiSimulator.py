"""
CP1404 Practical
Car class and it's subclasses
Gareth Mullins JCU Student
Started 17/09/2016
"""

from Prac08.car import Taxi, SilverServiceTaxi


def main():
    menu_choices = "q)uit, c)hoose taxi, d)rive"
    menu_input = "a"
    total_bill = 0
    # car class, name, fuel, fanciness (SilverServiceTaxi)
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    taxi_choice = choose(taxis)

    while menu_input != "q":
        menu_input = menu(menu_choices)
        if menu_input == "c":
            taxi_choice = choose(taxis)
        elif menu_input == "d":
            total_bill = drive(taxis, taxi_choice, total_bill)
        elif menu_input != "q":
            print("Invalid option")
        print("Bill to date: ${:,.2f}".format(total_bill))
        print()

    print("Total trip cost: {}".format(total_bill))
    print("Taxis are now:")
    for taxi in range(len(taxis)):
        print("{} - {}".format(taxi, taxis[taxi]))


def menu(menu_choices):
    """
    get the user's choice of what they want to do
    :param menu_choices:
    :return: menu_input
    """
    print(menu_choices)
    menu_input = input().lower()
    return menu_input


def choose(taxis):
    """
    get the taxi to be used
    :param taxis:
    :return: taxi_choice
    """
    taxi_choice = -1
    while taxi_choice < 0 or taxi_choice >= len(taxis):
        for taxi in range(len(taxis)):
            print("{} - {}".format(taxi, taxis[taxi]))
        try:
            taxi_choice = int(input("Choose taxi by it's number: "))
            if taxi_choice < 0 or taxi_choice > len(taxis):
                print("Invalid taxi number")
        except ValueError:
            print("Invalid taxi number")
        print()
    return taxi_choice


def drive(taxies, taxi_choice, total_bill):
    """
    drive the chosen taxi and calculate the fare
    :param taxies:
    :param taxi_choice:
    :param total_bill:
    :return: total_bill
    """
    distance = -5
    trip_cost = 0
    while distance < 0:
        try:
            distance = int(input("Drive how far? "))
            trip_cost = taxies[taxi_choice].drive(distance)
            if distance <= 0:
                print("Invalid input, distance must be greater then 0")
        except ValueError:
            print("Invalid input, only enter numbers")
    print("Your {} trip cost you ${:,.2f}".format(taxies[taxi_choice].name, trip_cost))
    total_bill += trip_cost

    return total_bill


if __name__ == "__main__":
        main()
