
def calculate(a: float, b: float, operation: str) -> dict:
    """Perform a mathematical operation on two numbers.

    Args:
        a: First number.
        b: Second number.
        operation: add, subtract, multiply, divide, or power.
    """
    print(f"[TOOL CALL] Calculator: {a}, {b}, {operation}")
    operation = operation.lower().strip()

    try:
        if operation == "add":
            result = a + b

        elif operation == "subtract":
            result = a - b

        elif operation == "multiply":
            result = a * b

        elif operation == "divide":
            if b == 0:
                return {"error": "Cannot divide by zero."}
            result = a / b

        elif operation == "power":
            result = a ** b

        else:
            return {"error": "Unsupported operation."}

        if isinstance(result, complex):
            return {"error": "Complex results are not supported."}

        return {
            "tool": "calculator",
            "operation": operation,
            "result": result
        }

    except (ArithmeticError, ValueError) as e:
        return {"error": str(e)}
