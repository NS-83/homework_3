import random
# Чтоб много не писать в словарях только дни и месяца из вопросов лотереи)
day_strings= {'03': 'третьего',
              '05': 'пятого',
              '06': 'шестого',
              '09': 'девятого',
              '10': 'десятого',
              '13': 'тринадцатого',
              '15': 'пятнадцатого',
              '29': 'двадцать девятого',}

months_strings = {'01': 'января',
                  '02': 'февраля',
                  '06': 'июня',
                  '09': 'сентября',
                  '10': 'октября',
                  '11': 'ноября',
                  '12': 'декабря'}
persons_list = {'А. С. Пушкин': '06.06.1983',
                  'М. Ю. Лермонтов': '15.10.1814',
                  'А. В. Жуковский': '09.02.1783',
                  'Н. А. Некрасов': '10.12.1821',
                  'А. А. Фет': '05.12.1820',
                  'И. С. Тургенев': '09.11.1818',
                  'И. А. Крылов': '13.02.1769',
                  'С. А. Есенин': '03.10.1895',
                  'Л. Н. Толстой': '09.09.1828',
                  'А. П. Чехов': '29.01.1860'}
while True:
    persons = random.sample(persons_list.keys(), 5)
    right_answers = 0
    wrong_answers = 0
    for person in persons:
        answer = input(f'Введите дату рождения писателя: {person}: ')
        birthday_string = persons_list[person]
        if answer == birthday_string:
            right_answers += 1
        else:
            wrong_answers += 1
            birthday_parts = birthday_string.split('.')
            print(f'{person} родился {day_strings[birthday_parts[0]]} {months_strings[birthday_parts[1]]} '
                  f'{birthday_parts[2]}')
    print(f'Правильных ответов: {right_answers}')
    print(f'Неправильных ответов: {wrong_answers}')
    play_again = None
    while play_again not in ['да', 'нет']:
        play_again = input('Сыграть ещё раз? (да/нет):')
    if play_again == 'нет':
        break






