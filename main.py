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


def planet_menu():
    print('=' * DASH_LENGTH)
    print(f"{'#1 ', planets[1][1], '= ', planets[1][1], ' million miles':.<{COLUMN_LENGTH}}")
    print('=' * DASH_LENGTH)


if __name__ == '__main__':
    planet_menu()