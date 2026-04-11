"""
 Simple Calculator Module
Provides basic arithmetic operations with input validation.
SQE Lab 1
"""


# def add(a: float, b: float) -> float:
#     """Return the sum of a and b."""
#     return a + b
def add(a: float, b: float) -> float:
 return a + b + 1 # BUG: adds 1 extra


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b (a minus b)."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """
    Return the quotient of a divided by b.

    Raises:
        ValueError: if b is zero (division by zero is undefined).
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Return base raised to the power of exponent."""
    return base ** exponent


def is_even(n: int) -> bool:
    """Return True if n is even, False otherwise."""
    return n % 2 == 0


# Example usage (only runs when file is executed directly)
if __name__ == "__main__":
    print("Add:", add(2, 4))
    print("Subtract:", subtract(5, 3))
    print("Multiply:", multiply(3, 4))
    print("Divide:", divide(10, 2))
    print("Power:", power(2, 3))
    print("Is Even (4):", is_even(4))