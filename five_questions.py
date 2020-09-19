list_answer = [1, 2, 3]
correct_answer = 0
wrong_answer = 0
while True:
    question1 = int(input('''Начнем с простого. Каким фильмом началась Киновселенная Marvel?
    1)Железный человек
    2)Тор
    3)Первый мститель\n'''))

    if question1 not in list_answer:
        print('такого ответа нет!!!')
    else:
        break

if question1 == 1:
    print('верно')
    correct_answer += 1
elif question1 == 2:
    print('нет это не тор, иди пересмотри железного человека')
    wrong_answer += 1
else:
    print('увы но это не фильм кэпа')
    wrong_answer += 1

while True:
    question2 = int(input('''А какая студия первоначально хотела заняться экранизацией "Железного человека"?
    1)FOX
    2)New Line Cinema
    3)Universal Picture\n'''))

    if question2 not in list_answer:
        print('такого ответа нет!!!')
    else:
        break

if question2 == 2:
    print('угу, это верный ответ')
    correct_answer += 1
elif question2 == 1:
    print('нее, врят-ли')
    wrong_answer += 1
else:
    print('нет')
    wrong_answer += 1

while True:
    question3 = int(input('''Капитану Марвел. Под каким прозвищем она геройствовала в комиксах до получения "капитанских лычек"?
    1)Мисс Марвэл
    2)Марвэл гёрл
    3)Марввелвумэн\n'''))

    if question3 not in list_answer:
        print('такого ответа нет!!!')
    else:
        break

if question3 == 1:
    print('да, именно так ее и звали')
    correct_answer += 1
elif question3 == 2:
    print('неугадал')
    wrong_answer += 1
else:
    print('мимо')
    wrong_answer += 1

while True:
    question4 = int(input('''В Киновселенную Marvel входят не только фильмы, но и сериалы. Какой из них мы выдумали?
    1)Защитники
    2)Плащь и кинжал
    3)лунный рыцарь\n'''))

    if question4 not in list_answer:
        print('такого ответа нет!!!')
    else:
        break

if question4 == 3:
    print('пока что такого сериала нет, ты угадал!!!')
    correct_answer += 1
elif question4 == 1:
    print('это не выдумка')
    wrong_answer += 1
else:
    print('этот сериал есть')
    wrong_answer += 1

while True:
    question5 = int(input('''У DC когда-то тоже был свой Капитан Марвел. Под каким именем он известен сейчас?
    1)Доктор фэйт
    2)Шазам
    3)масквелл Лорд\n'''))

    if question5 not in list_answer:
        print('такого ответа нет!!!')
    else:
        break

if question5 == 2:
    print('именно он!!!')
    correct_answer += 1
elif question5 == 1:
    print('неугадал((')
    wrong_answer += 1
else:
    print('ноуп!')
    wrong_answer += 1

print(f'количество правильный ответов {correct_answer}, а не правильных {wrong_answer}')