def my_func(arg1,arg2,arg3):
    my_list = sorted([arg1,arg2,arg3])
    quot = my_list[1] + my_list[2]
    return quot


print(my_func(float(input("Введите первое значение: ")),float(input("Введите второе значение: ")),float(input("Введите третье значение: "))))