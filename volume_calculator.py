def calculate_volume(length, width, height):
    """Calculate the volume of a box."""
    volume = length * width * height
    return volume

def main():
    length = 4
    width = 6
    height = 2
    result = calculate_volume(length, width, height)
    print(f"Volume: {result}")

main()