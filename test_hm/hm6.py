# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

def output_numbers(*args):
    with open('celchisl.txt', 'w') as file:
        for arg in args:

            file.write(str(arg) + '\n')

    with open('celchisl.txt', 'r') as file:
        numbers_str = file.readlines()
        if len(numbers_str) <= 3:
            return 'ERR'
        else:
            numbers = [int(num.strip()) for num in numbers_str]
            f_e = numbers[0]
            s_e = numbers[1]
            t_e = numbers[-2]
            l_e = numbers[-1]
            return f_e, s_e, t_e, l_e


# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их
# квадраты.

def func_square():
    kvdr = []
    try:
        with open ('vesh.txt', 'r') as file:
            numbers_str = file.readline ().split ()
            numb = [float(num) for num in numbers_str]
    except ValueError:
        return "ERROR"

    for num in numb:
        kvdr_num = num ** 2
        kvdr.append (kvdr_num)

    kvdr_st = ' '.join(str(i) for i in kvdr)

    with open('vesh.txt', 'w') as file:
        file.write(kvdr_st)

    return kvdr_st