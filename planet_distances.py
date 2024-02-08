"""
Usage: planet_distances.py
Allow the user to calculate distances between two planets based on average distances from the sun.

GitHub: https://github.com/lindllgrn/PlanetCalculator
"""

# metadata
__author__ = "Lindsay Green,  Hunter Schoch"
__date__ = "2024/02/08"
__email__ = "lindllgrn@gmail.com, hnschoch@gmail.com"
__version__ = "0.0.1"

DASH_LENGTH = 60
# Establishes a 60 character width limit for the dividing lines for aesthetic purposes
COLUMN_LENGTH = 60

planets = (  # tuple for holding values of planet names and their distance from the Sun
    ('Mercury', 57),
    ('Venus', 108),
    ('Earth', 150),
    ('Mars', 228),
    ('Jupiter', 779),
    ('Saturn', 1430),
    ('Uranus', 2880),
    ('Neptune', 4500)
)


def get_integer_input(message, min_num=0, max_num=0):
    """
    Get a valid integer value from the user.
    If the min and max values are both zero then there are enforced ranges
    :param message: user's prompt
    :param min_num: min integer input value allowed
    :param max_num:max integer input value allowed
    :return: user input
    """

    while True:  # keep looping until the user enters a valid value

        # prevent the program from ending due to a ValueError runtime error
        try:
            user_input = int(input(message))  # if this fails the except block will catch the error

            if min == 0 and max == 0:  # if there are no min and max values set
                return user_input
            elif min_num <= user_input <= max_num:
                return user_input
            else:
                print(f"\tInvalid input: please enter a number between {min_num} and {max_num}.")
                continue

        except ValueError:  # the user entered a non integer value
            print("\tinvalid input: please enter a number.")
            continue


def display_abs_distance(planet1_num, planet2_num):
    """
    Used to get absolute distance of two planet distances
    :param planet1_num: user input of first planet chosen
    :param planet2_num: user input of second planet chosen
    :return: absolute distance calculated from the two planets chosen
    """

    planet1_info = planets[planet1_num - 1]  # gathers info from the planets tuple for information on planet 1
    planet1_name, planet1_dist = planet1_info

    planet2_info = planets[planet2_num - 1]  # gathers info from the planets tuple for information on planet 2
    planet2_name, planet2_dist = planet2_info

    calc_dist = abs(planet1_dist - planet2_dist)  # calculates the absolute distance
    print(" ")
    print(planet1_name, " and ", planet2_name, " are ", calc_dist, "million miles apart")
    print(" ")


def planet_menu():
    """
    creates the starting menu which displays the planets and how many miles away from the Sun they are
    :return: user input
    """

    print('=' * DASH_LENGTH)
    print("Planet's Average Distance From Sun")
    print('=' * DASH_LENGTH)
    menu_number = 1
    for planet, distance in planets:  # displays the planets in order from the tuple
        print(f"#{menu_number} {planet:<7} = {distance:>4} million miles")
        menu_number += 1
    print('=' * DASH_LENGTH)
    print("To calculate the distance between two planets")


def main():
    """
    runs the program in its entirety, accounting for error handling
    :return: user input
    """

    planet_menu()  # displays the starting menu

    while True:
        print(
            "Enter two planet numbers or 0 to quit:")  # gathers user input and gives them an option to exit the program
        print('=' * DASH_LENGTH)
        planet1_num = get_integer_input("Please enter the 1st Planet # ", min_num=0,
                                        max_num=len(planets))  # gets the user's input for first planet chosen

        if planet1_num == 0:
            break

        while True:
            planet2_num = get_integer_input("Please enter the 2nd Planet # ", min_num=0,
                                            max_num=len(planets))  # gets the user's input for second planet chosen

            if planet1_num == planet2_num:  # error handles in case same planet was chosen
                print("Choose a different planet. Same planet was chosen.")

            else:
                break

        if planet2_num == 0:
            break

        display_abs_distance(planet1_num, planet2_num)  # displays the distance between the two planets chosen

        input("Press enter to continue...")
        print('=' * DASH_LENGTH)


if __name__ == '__main__':
    main()
