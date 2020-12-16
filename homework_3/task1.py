def my_div(divisor, divisible):
    quot = divisor / divisible
    return quot

try:
    print(my_div(divisor = int(input("Введите делимое: ")), divisible = int(input("Введите делитель: "))))
except ZeroDivisionError:
    print("Деление на ноль!")
