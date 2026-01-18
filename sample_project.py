def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

def main():
    length = 5
    width = 3
    result = calculate_area(length, width)
    print(f"Area: {result}")

main()