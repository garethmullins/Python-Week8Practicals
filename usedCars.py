"""
CP1404 Practical
Car class and it's subclasses
Gareth Mullins JCU Student
Started 17/09/2016
"""

from Prac08.car import Taxi, UnreliableCar, SilverServiceTaxi


def main():
    car = 0
    # car class, name, fuel, reliability (UnreliableCar), fanciness (SilverServiceTaxi)
    cars = [UnreliableCar("Old Jon", 100, 90),
            Taxi("Prius 1", 100),
            SilverServiceTaxi("Hummer", 200, 4)]

    # Old Jon
    cars[car].drive(30)
    print(str(cars[car]))

    cars[car].add_fuel(15)
    cars[car].drive(100)
    print(str(cars[car]))

    print()
    car += 1

    # Prius 1
    cars[car].drive(40)
    print(str(cars[car]))

    cars[car].add_fuel(30)
    cars[car].start_fare()
    cars[car].drive(130)
    print(str(cars[car]))

    print()
    car += 1

    # V.I.P service 2
    cars[car].drive(10)
    print(str(cars[car]))

    cars[car].drive(40)
    print(str(cars[car]))

    cars[car].add_fuel(30)
    cars[car].start_fare()
    cars[car].drive(130)
    print(str(cars[car]))

    print()
    car += 1

    # finish
    for vehicle in cars:
        print(str(vehicle))


if __name__ == "__main__":
        main()
