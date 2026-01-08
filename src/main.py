# Team Project: Calculator Application
# Version: 1.2.0

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    result = a * b
    print(f"Multiplying {a} x {b}")
    return result

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

if __name__ == "__main__":
    print("Calculator v1.2.0")
    print(f"10 + 5 = {add(10, 5)}")
    print(f"10 - 5 = {subtract(10, 5)}")
    print(f"10 x 5 = {multiply(10, 5)}")
    print(f"10 / 5 = {divide(10, 5)}")