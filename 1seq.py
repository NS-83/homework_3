elements_number = ''
while not elements_number.isdigit():
    elements_number = input('Введите число элементов: ')
elements_number = int(elements_number)
elements_list = []
for i in range(0, elements_number):
    element = ''
    while not element.isdigit():
        element = input(f'Введите {i+1} элемент: ')
    elements_list.append(int(element))
elements_list.sort()
print(elements_list)



