def add(a, b): return a + b
def sub(a, b): return a - b
def multi(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Помилка: ділення на нуль!"

try:
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    action = input("Введіть дію (+, -, *, /): ")
    
    if action == '+':
        result = add(num1, num2)
    elif action == '-':
        result = sub(num1, num2)
    elif action == '*':
        result = multi(num1, num2)
    elif action == '/':
        result = divide(num1, num2)
    else:
        result = "Невірна дія!"
    
    print(f"Результат: {result}")
except ValueError:
    print("Помилка: введіть тільки цифри!")