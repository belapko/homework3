def my_sum():
    sum_result = 0
    exit = True
    while exit == True:
        result = 0
        number = input("Введите числа или 'q' для завершения работы программы: ").split()
        for i in range(len(number)):
            if number[i] == "q":
                exit = False
                break
            else:
                result = result + int(number[i])
        sum_result = sum_result + result

    print(f"Ваша сумма всех введённых чисел = {sum_result}")

my_sum()


