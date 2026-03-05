def calculate(num1, operation, num2):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1 - num2
    if operation == '/':
        if num2 == 0:
            return None
        else:
            return num1 / num2
    if operation == '*':
        return num1 * num2
