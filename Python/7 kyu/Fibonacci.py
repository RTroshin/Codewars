def fibonacci(n: int) -> int:
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else n
