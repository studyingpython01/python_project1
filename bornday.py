year = 1799
day = 6
answer = int(input('Год рождения'))
if answer == year:
    answer2 = int(input('День рождения'))
    if answer2 == day:
        print('Верно')
    else:
        print('Неверно')
else:
    print('Неверно')
