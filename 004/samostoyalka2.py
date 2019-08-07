import random
words = ['мама', 'папа', 'собака', 'дом', 'огород', 'ветер', 'стул', 'мотоцикл', 'пила', 'слон']
random.shuffle(words)
slovo = words[0] 
slovo_print = ':*' * int(len(slovo))
slovo_print2 = slovo_print.split(':')
slovo_print2.pop(0)
print(slovo_print2)
life = 10
slovo2 = []
for z in slovo:
    slovo2.append(z)
slovo22 = tuple(slovo2)
slovo222 = list(slovo22)
while life != 0:
    x = str(input('введите букву:'))
    if x in slovo222:
        print('угадал')
        s = slovo222.index(x)
        slovo_print2[s] = x
        slovo222[s] = 'asd'
        print(slovo_print2)
        if slovo_print2 == slovo2:
            print('Молодец! - Победа!')
            break
    else:
        life -= 1
        print('не угадал, осталось жизней -',life)