#Создать лист из 6 любых чисел. Отсортировать его по возрастанию

list = [01293, 1231254, 542653467, 2345, 21124]
list.sort()

#Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

slovo = {1: 'asd', 2: '23f2', 3: 'gg0gf', 4: 'fas', 5: '55453d', 6: '4f4f4f4'}
for key in slovo:
    print(key, slovo[key])


#Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем

tuple = (324.3, 4362.5345274, 425642358356.73567537, 3567.43234, 3425123.123, 213.12312312312, 1241235432.333)
print('maximalnoe -', max(tuple))
print('minimalnoe -', min(tuple))

#Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку,
чтобы получилось: 'Earth -> Russia -> Moscow'

list = ['Earth', 'Russia', 'Moscow']
print(list[0], '->', list[1], '->', list[2])

#Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

a = '/bin:/usr/bin:/usr/local/bin'
print(a.split(':'))

#Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

for m in range(1,101):
    if m % 7 == 0:
        print('delitsya', m)
    else:
        print('ne delitsya', m)

#Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

A = [[1, 2, 3, ], [4, 5, 6, ], [7, 8, 9, ], [10, 11, 12, ]]
print('stroka 1 -', A[0])
print('stroka 2 -', A[1])
print('stroka 3 -', A[2])
print('stroka 4 -', A[3])
print('stolb 1 -', A[0][0], A[1][0], A[2][0], A[3][0])
print('stolb 1 -', A[0][1], A[1][1], A[2][1], A[3][1])
print('stolb 1 -', A[0][2], A[1][2], A[2][2], A[3][2])

#Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

list = [None, True, -2, 'asd', 2456.34, ]
for m in list:
    print(m, list.index(m))


#Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

list = [True, 'to-delete', True, 'to-delete', 'asd', 2456.34, 'to-delete', None, ]
for m in list:
    if m == str('to-delete') :
        list.remove('to-delete')

#Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

for m in range(10,1,-1):
    print(m)