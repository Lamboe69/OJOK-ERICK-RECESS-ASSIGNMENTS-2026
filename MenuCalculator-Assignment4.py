def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b


while True:
    print()
    print("=" * 40)
    print("       CALCULATOR MENU")
    print("=" * 40)
    print("  1. Addition")
    print("  2. Subtraction")
    print("  3. Multiplication")
    print("  4. Division")
    print("  5. Exit")
    print("=" * 40)

    choice = input("  Enter your choice (1-5): ")

    if choice == "5":
        print("  Exiting calculator. Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("  Invalid choice. Please select 1-5.")
        continue

    print()
    num1 = float(input("  Enter first number: "))
    num2 = float(input("  Enter second number: "))
    print()

    if choice == "1":
        result = add(num1, num2)
        print(f"  {num1} + {num2} = {result}")
    elif choice == "2":
        result = subtract(num1, num2)
        print(f"  {num1} - {num2} = {result}")
    elif choice == "3":
        result = multiply(num1, num2)
        print(f"  {num1} × {num2} = {result}")
    elif choice == "4":
        result = divide(num1, num2)
        print(f"  {num1} ÷ {num2} = {result}")
