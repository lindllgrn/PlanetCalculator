DASH_LENGTH = 100
# Establishes a 40 character width limit for the dividing lines for aesthetic purposes
COLUMN_LENGTH = 100

planets = (
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
    while True:

        try:
            user_input = int(input(message))

            if min == 0 and max == 0:
                return user_input
            elif min_num <= user_input <= max_num:
                return user_input
            else:
                print(f"\tInvalid input: please enter a number between {min_num} and {max_num}.")
                continue

        except ValueError:
            print("\tinvalid input: please enter a number.")
            continue


def display_abs_distance(planet1_num, planet2_num):
    planet1_info = planets[planet1_num - 1]
    planet1_name, planet1_dist = planet1_info

    planet2_info = planets[planet2_num - 1]
    planet2_name, planet2_dist = planet2_info

    calc_dist = abs(planet1_dist - planet2_dist)
    print(calc_dist)


def planet_menu():
    print('=' * DASH_LENGTH)
    print("Planet's Average Distance From Sun")
    print('=' * DASH_LENGTH)
    menu_number = 1
    for planet, distance in planets:
        print(f"#{menu_number} {planet:<7} = {distance:>4} million miles")
        menu_number += 1
    print('=' * DASH_LENGTH)


if __name__ == '__main__':
    # Docstring
    planet_menu()

    while True:
        planet1 = print(get_integer_input("Please enter the 1st Planet # ", min_num=0, max_num=len(planets)))

        if planet1 == 0:
            break

    while True:
        planet2 = print(get_integer_input("Please enter the 2nd Planet # ", min_num=0, max_num=len(planets)))

        if planet2 == 0:
            break
