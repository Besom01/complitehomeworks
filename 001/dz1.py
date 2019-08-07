print('знак # как то влияет на код?')
right = 1
wrong = 1
chose = '0'
answer1 = 'no'
answer11 = 'нет'
flag = 0
while (flag != 1):
    chose = input('Ответ?')
    if(answer1 == chose or answer11 == chose):
        print('Правильно!')
        right+=1
        flag = 1
    else:
        print('Не верно!')
        wrong+=1
print('чему равно True?')
answer2 = '1'
while chose != answer2:
    chose = input('Ответ?')
    if (chose == answer2):
        print('Right!')
        right+=1
    else:
        print('Nope')
        wrong+=1
print('с помощью какой команды можно узнать сколько символов в строке ?')
answer3 = 'Len'
while chose != answer3:
    chose = input('Ответ?')
    if (chose == answer3):
        print('Good job!')
        right+=1
    else:
        wrong+=1
        print('No No No')
flag = 0
print('в имени переменной может быть символ @ ?')
while (flag != 1):
    chose = input('Ответ?')
    if(answer1 == chose or answer11 == chose):
        print('Правильно!')
        right+=1
        flag = 1
    else:
        print('Не верно!')
        wrong+=1
flag = 0
print('можно ли сложить сложить 2 переменных когда одна их них строка а другая число ?')
while (flag != 1):
    chose = input('Ответ?')
    if(answer1 == chose or answer11 == chose):
        print('Правильно!')
        right+=1
        flag = 1
    else:
        print('Не верно!')
        wrong+=1
flag = 0
print('какой тип данных получиться (int или float) если выполнить такое выражение - 3/3')
answer7 = 'float'
while chose != answer7:
    chose = input('Ответ?')
    if (answer7 == chose):
        print('Gratz!')
        right+=1
    else:
        print('Bad!')
        wrong+=1
flag = 0
print('с помощью какой команды можно узнать есть ли в этой строке буква "о" написанная на англиском языке ?')
answer8 = 'in'
while chose != answer8:
    chose = input('Ответ?')
    if(answer8 == chose):
        print('Molodec')
        right+=1
    else:
        print('No!')
        wrong+=1
flag = 0
print('сколько будет 2 + 2 * 2 / 2 = ?')
answer9 = '2'
while chose != answer9:
    chose = input('Ответ?')
    if (chose == answer9):
        print('Krasava')
        right+=1
    else:
        print('Ny net je')
        wrong+=1
flag = 0
print('Сколько вы дали не вырных ответов?')
wrongg = '0'
while chose != wrongg:
    chose = input('И?')
    if (chose == wrongg):
        print('Pravilno')
    else:
        print('Ne verno')
print('Правильных ответов', right)
print('Не правильных попыток', wrong)
print('Всего попыток', right + wrong)