correct_input = False
while not correct_input:
    correct_input = True
    numbers_string = input('Введите первый список чисел: ')
    separator = ','
    if numbers_string.find(';') != -1:
        separator = ';'
    elif numbers_string.find('/') != -1:
        separator = '/'
    numbers_strings_list = numbers_string.split(separator)
    numbers_list_1 = []
    for number_string in numbers_strings_list:
        number = number_string.strip()
        if number.isdigit():
            numbers_list_1.append(int(number))
        else:
            print('Введена некорректная строка')
            correct_input = False
            break
correct_input = False
while not correct_input:
    correct_input = True
    numbers_string = input('Введите второй список чисел: ')
    separator = ','
    if numbers_string.find(';') != -1:
        separator = ';'
    elif numbers_string.find('/') != -1:
        separator = '/'
    numbers_strings_list = numbers_string.split(separator)
    numbers_list_2 = []
    for number_string in numbers_strings_list:
        number = number_string.strip()
        if number.isdigit():
            numbers_list_2.append(int(number))
        else:
            print('Введена некорректная строка')
            correct_input = False
            break
numbers_set_1 = set(numbers_list_1)
numbers_set_2 = set(numbers_list_2)
print(numbers_set_1.difference(numbers_set_2))