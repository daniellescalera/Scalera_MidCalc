from calculator.calculations import Calculation

def main():
    while True:
        operation = input("Enter operation (add, subtract, multiply, divide or exit): ").strip().lower()
        if operation == "exit":
            print("Goodbye!")
            break
        num1 = input("Enter first number: ").strip()
        num2 = input("Enter second number: ").strip()

        try:
            calc = Calculation(operation, num1, num2)
            print(f"Result: {calc.result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
