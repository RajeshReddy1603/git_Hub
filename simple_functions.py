def greet(name):
    return f"Hello, {name}!"

def is_even(number):
    return number % 2 == 0

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def main():
    print(greet("Python"))
    print(f"Is 8 even? {is_even(8)}")
    print(f"Factorial of 5: {factorial(5)}")

main()