# 3 Напишите функцию generate_squares, которая принимает произвольное количество аргументов и возвращает список,
# состоящий из их квадратов.Тоесть generate_squares(1, 2, 3) -> [1, 4, 9]


def generate_squares(*args):
    if all(isinstance(i, int) for i in args):
        return [i ** 2 for i in args]
    if all(isinstance(i, str) for i in args) or not all(isinstance(i, int)for i in args):
        return 'Error'
    if all(isinstance(i, bool)for i in args):
        return 'Error'
    if all(isinstance(i, float)for i in args):
        return 'Error'
print(generate_squares(-1, -2, -3))


# 4 Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы), и возвращает
# самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.


def get_longest_word(text):
    word = text.split()
    get_longest_word = max(word, key=len)
    return get_longest_word


text = 'Hello my name is Vseslav , I am from Belarus'
print(get_longest_word(text))