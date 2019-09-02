// Домашнее задание будет полной копией задач из первых лекций для python. Нужно реализовать логику и сравнить подходы двух языков.

// + Напишите программу, которая считает площадь прямоугольника, спрашивая у пользователя длину двух сторон

function Ploshad(a,b) {return a*b}

// + Напишите программу, которая спрашивает у пользователя два числа и знак: "+" или "-". В зависимости от знака выводит их сумму или разницу

function zagadka(a, b, c) { 
    if (c == '+') {return a + b}
    else {return a - b}}

// + Напишите программу, которая находит все простые числа между 0 и пользовательским числом

function ProstoeChislo(end) {
    var all = []
    for (var i = 2; i <= end; i++) 
        {
        var check = [];
        for (var z = 2; z <= i; z++){
            if (i % z === 0) {
                check.push(z);
            }
        };
    if (check.length === 1) {all.push(i)}
        }

return console.log(all)}

// + Напишите программу, которая выводит все кратные 5 числа между двумя пользовательскими числами

function Kratnoe5(a, b)
{
    var all = []
    for (a; a < b; a++)
    {
        if ( a % 5 === 0)
        {
            all.push(a)
        }
    }
return console.log(a)
}

// + Создать лист из 6 любых чисел. Отсортировать его по возрастанию

function Sortirovka()
{
    sprisok = []
    for (var i = 1; i <= 6; i++)
    {
        var z = Math.round(Math.random()*100)
        sprisok.push(z)
    };
    return sprisok.sort()
}

// + Создать словарь из 5 пар: int -> str, например {6: '6'}, вывести его в консоль попарно

var slovar = {1:'1',2:'2',3:'3',4:'4',5:'5',6:'6'}

function VivodSlovarya()
{
    for (var item in slovar)
    {
        console.log(item, slovar[item])
    }
}
// + Создать tuple из 10 любых дробных чисел, найти максимальное и минимальное значение в нем



function MinMaxLog()
{
    var ti = []
    for (var i = 1; i <= 10; i++)
    {
        var z = Math.random()
        ti.push(z)
    };
    var minti = Math.min.apply({}, ti)
    var maxti = Math.max.apply({}, ti)
    return console.log(minti, maxti)
}

// + Создать лист из 3 слов: ['Earth', 'Russia', 'Moscow'], соеденить все слова в единую строку, чтобы получилось: 'Earth -> Russia -> Moscow'

var l = ['Earth', 'Russia', 'Moscow']

function Heh(a)
{
    var complite = ''
    for (var item in a)
    {
        complite =complite + a[item] + ' -> '
    }
    complite.slice(-4)
    return console.log(complite.slice(0, -4))  
}

// + Взять строку '/bin:/usr/bin:/usr/local/bin' и разбить ее в список по символу ':'

var str = '/bin:/usr/bin:/usr/local/bin'
var paths = str.split(':')
console.log(paths)


// + Пройти по всем числам от 1 до 100, написать в консоль, какие из них делятся на 7, а какие - нет

function Kratnoe7(a, b)
{
    var all = []
    var neAll = []
    for (a; a < b; a++)
    {
        if ( a % 7 === 0)
        {
            all.push(a)
        }
        else
        {
            neAll.push(a)
        }
    }
return console.log('Delitsya:' + all, 'Ne delitsya: '+ neAll)
}

// + Создать матрицу любых чисел 3 на 4, сначала вывести все строки, потом все столбцы

// ????

// + Создать список любых объектов, в цикле напечатать в консоль: объект и его индекс

var spisok = [1,2,3,4,5,6]

function VivodSpiska()
{
    for (var item in spisok)
    {
        console.log(item, spisok[item])
    }
}

// + Создать список с тремя значениями 'to-delete' и нескольми любыми другими, удалить из него все значения 'to-delete'

var spisok = [1,'to-delete',2,'to-delete',3,'4',5,6,'to-delete']


function Udalittodel()
{
    for (var item in spisok)
    {
        if (spisok[item] == 'to-delete')
        {
            spisok.splice(item, 1)
        }
    }
    return spisok
}

// + Пройти по всем числам от 1 до 10 в обратную сторону (то есть: от 10 до 1), напечатать их в консоль

var l = [1,2,3,4,5,6,7,8,9,10]

function to10do1 ()
{
    for (var i = 10; i > 0; i--)
    {
        console.log(i)
    }
}