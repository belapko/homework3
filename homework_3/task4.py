def my_func(x,y):
    return x**y
print(my_func(float(input("Первое число: ")), int(input("Второе число: "))))

def my_func(x,y):
    i = 1
    while y > 0:
        i *= x
        y -=1
    return i

print(my_func(float(input("Первое число: ")), int(input("Второе число: "))))

