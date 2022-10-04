born = 1799
answer = int(input('Год рождения'))
while  answer != born:
    print('Неверно')
    answer = int(input('Год рождения'))
else:
    print('Верно')