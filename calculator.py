import re
from src.utils import add, mul, sub, div


print("Operation Menu:")
print("1. for addition, type: a + b")
print("2. for subtraction, type: a - b")
print("3. for multiplication, type: a * b")
print("4. for division, type: a / b (b != 0)")
print()


def run_calculator():
    while True:
        user_input = input("Input (Type 'exit' to quit): ").strip()

        # Exit condition
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye!")
            break

        # Match expressions like '3+3', '3 + 3', '-2.5 * 4', etc.
        match = re.match(r'^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/])\s*(-?\d+(?:\.\d+)?)\s*$', user_input)

        if not match:
            print("❌ Invalid format. Please use something like '3+3' or '3 + 3'.\n")
            continue

        a = float(match.group(1))
        op = match.group(2)
        b = float(match.group(3))

        try:
            if op == '+':
                result = add(a, b)
            elif op == '-':
                result = sub(a, b)
            elif op == '*':
                result = mul(a, b)
            elif op == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result = div(a, b)
            else:
                raise ValueError("Unsupported operator.")
            print(f"Result: {result}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    run_calculator()
