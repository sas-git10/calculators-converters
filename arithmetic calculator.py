def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else "Error: Division by zero"

def calculator():
    print("--- Simple Python Calculator ---")
    while True:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /) or 'q' to quit: ")
        
        if op.lower() == 'q':
            break
            
        num2 = float(input("Enter second number: "))

        if op == '+': print(f"Result: {add(num1, num2)}")
        elif op == '-': print(f"Result: {subtract(num1, num2)}")
        elif op == '*': print(f"Result: {multiply(num1, num2)}")
        elif op == '/': print(f"Result: {divide(num1, num2)}")
        else: print("Invalid Operator")
        print("-" * 20)

if __name__ == "__main__":
    calculator()
