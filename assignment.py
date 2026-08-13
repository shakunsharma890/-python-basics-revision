"""
assignment.py
Calculate the area of a circle from a diameter input.
"""

def main():
    try:
        diameter = float(input("Enter a diameter: "))
        radius = diameter / 2
        area_of_circle = 3.14 * (radius ** 2)
        print(f"Area of the circle with diameter {diameter} is {area_of_circle}")
    except ValueError:
        print("Please enter a valid number for diameter.")


if __name__ == "__main__":
    main()
