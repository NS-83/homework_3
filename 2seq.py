correct_input = False
while not correct_input:
    correct_input = True
    numbers_string = input('Введите строку чисел: ')
    separator = ','
    if numbers_string.find(';') != -1:
        separator = ';'
    elif numbers_string.find('/') != -1:
        separator = '/'
    numbers_strings_list = numbers_string.split(separator)
    numbers_list = []
    for number_string in numbers_strings_list:
        number = number_string.strip()
        if number.isdigit():
            numbers_list.append(int(number))
        else:
            print('Введена некорректная строка')
            correct_input = False
            break
print(set(numbers_list))




