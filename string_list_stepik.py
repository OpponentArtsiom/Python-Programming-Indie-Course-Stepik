"""
print('Лев Николаевич Толстой написал "Война и мир"')
"""
"""
a = input()
b = input()
print(a,'\n',b,sep = '')

a=input()
b=input()
print(a,b, sep='\n')
"""
"""
t1, t2, t3 = input(), input(), input()
print(t3, t2, t1, sep='\n')
"""
"""
text = input()
print((text + ' ') * 4)
"""
"""
text = input()
print(len(text))
"""
"""
text1, text2 = input(), input()
print(text2 + text1)
"""
"""
text = input()
print(text * 3)
"""
"""
t1, t2, t3 = input().split()
print("Simvol code", t1, "is", ord(t1), end='.')
print("\nSimvol code", t2, "is", ord(t2), end='.')
print("\nSimvol code", t3, "is", ord(t3), end='.')
"""

#_________________________СРЕЗЫ______________________
"""
text = input()
print(text[0])
"""
"""
text = input()
print(text[-1])
"""
"""
text = input()
print(text[0:4])
"""
"""
text = input()
print(text[-4:])
"""
# четные индексы
"""
text = input()
print(text[::2])
"""
# нечетные индексы
"""
text = input()
print(text[1::2])
"""
# разворот строки
"""
text = input()
print(text[::-1])
"""
"""
text = input()
print(text[::-3])
"""
"""
text = input()
print(text[-1] + text[:-1])
"""
"""
text = input()
print(text.upper())

text = input()
print(text.lower())
"""
"""
text = input()
print(text.swapcase())
"""
"""
t1, t2 = input(), input()
print(t1.lower() == t2.lower())
"""
# На вход подается строка. Ваша задача отформатировать строку так,
# чтобы первые 3 и последние 3 символа были заглавными, а оставшиеся строчные.
"""
text = input()
a = text[:3].upper()
b = text[-3:].upper()
c = text[3:-3].lower()
print(a + c + b)
"""

# На вход программе поступает строка, состоящая как из заглавных так из строчных букв.
# Ваша задача преобразовать строку так, чтобы первая буква у каждого слова стала маленькой,
# а остальные буквы превратились в заглавные. Символы пунктуации и цифры не нужно преобразовывать.
"""
text = input()
text1 = text.title()
print(text1.swapcase())
"""
# На вход программе поступает строка, ваша задача подсчитать сколько раз в ней встречается латинская буква "e".
# При этом стоит учитывать как маленькие, так и заглавные буквы
"""
text = input()
print(text.lower().count('e'))
"""

# На вход программе поступает строка, ваша задача вывести на экран индекс первой найденной латинской буквы a
"""
text = input()
print(text.find('a'))
"""
# На вход программе поступает строка, ваша задача вывести на экран индекс последней найденной латинской буквы a
"""
text = input()
print(text.rfind('a'))
"""
# Программа получает на вход фразу, состоящую из нескольких слов, разделенных пробелом. 
# Ваша задача заменить все пробелы запятыми и вывести полученную строку.
"""
text = input()
print(text.replace(' ', ','))
"""
# На вход программе поступает строка, ваша задача удалить из нее все символы w и z.
"""
text = input()
text = text.replace('w','')
print(text.replace('z', ''))

print(input().replace('w','').replace('z',''))
"""
# Упражнение на строки
"""
a = input().lower()
a = a.replace("a", "")
a = a.replace("o", "")
a = a.replace("e", "")
a = a.replace("y", "")
a = a.replace("i", "")
a = a.replace("u", "")
a = ".".join(a)
a = "." + a
print(a)
"""
# Длина разбитой строки         МЕТОД SPLIT
"""
S = input()
print(len(S.split()))
"""
#                               МЕТОД JOIN
"""
list_strings = ['Follow', 'the', 'Cops', 'Back', 'Home']
print('-'.join(list_strings))
"""
#                               МЕТОД startswith
"""
text = input().lower()
print(text.startswith("mam"))
"""
#                               МЕТОД endswith
"""
s = input()
postfix = input()
print(s.endswith(postfix))
"""
"""
s, prefix, postfix = input(), input(), input()
print(s.startswith(prefix) and s.endswith(postfix))
"""
#                               МЕТОД isdigit
"""
text = input()
print(text.isdigit())
"""
#                               МЕТОД isupper
"""
text = input()
print(text.isupper())
"""
#                               МЕТОД islower
"""
text = input()
print(text.islower())
"""
#                               МЕТОД ljust
"""
text = input()
print(text.ljust(15, '-'))
"""
#                               МЕТОД rjust
"""
text = input()
print(text.rjust(10, '!'))
"""
#                               МЕТОД center
"""
text = input()
print(text.center(15, '_'))
"""
#                               МЕТОД zfill
"""
text = input()
print(text.zfill(10))
"""
#                               МЕТОД strip
"""
text = input()
print(text.strip('-_!?'))
"""
#                               МЕТОД 
"""
text = input()
print(text.lstrip('-_!?'))
"""
"""
text = input()
print(text.rstrip('-_!?'))
"""

# Модель кодирования RGB
"""
n1, n2, n3 = int(input()), int(input()), int(input())
R = hex(n1)
G = hex(n2)
B = hex(n3)
print('#' + R.lstrip('0x').upper().rjust(2, '0') + G.lstrip('0x').upper().rjust(2, '0') 
      + B.lstrip('0x').upper().rjust(2, '0'))
"""

#word = input()
#text = """Что Вы сказали? {0}? Какое интересное слово""".format(word)
#print(text)

#name = input()
#surname = input()
#text = """Здравствуйте, {0} {1}!""".format(name, surname)
#print(text)

#num = int(input())
#text1 = """Для числа {0} предыдущим будет число {1}.""".format(num, int((num) - 1))  
#text2 = """Для числа {0} следующим будет число {1}.""".format(num, int((num) + 1))
#print(text1)
#print(text2)

#num = int(input())
#num1 = num - 1
#num2 = num + 1
#print('Для числа {0} предыдущим будет число {1}.\nДля числа {0} следующим будет число {2}.'.format(num, num1, num2))

#name = input()
#text = f"""Мое имя {name}!"""
#print(text)

#name, age = input(), int(input())
#text = f"""Hello {name.upper()}. You are {age} years old."""
#print(text)

#name, year = input(), int(input())
#text = f"""{name}, вам исполнится 77 лет в {year + 77}"""
#print(text)

#second = int(input())
#text = f"""{second} сек - это {second // 60} мин. {second % 60} сек."""
#print(text)

#a, b = map(int, input().split())
#text1 = f"""Разрешение экрана: {a} x {b}."""
#text2 = f"""Общее количество пикселей = {a * b}."""
#print(text1)
#print(text2)

#a, b = int(input()), int(input())
#print(f"""{a} / {b} = {a / b}""")
#print(f"""{a} // {b} = {a // b}""")
#print(f"""{a} % {b} = {a % b}""")

#x, y, z = int(input()), int(input()), int(input())
#print(f"""Vector A({x}, {y}, {z})""")
#print(f"""Vector B({x + 5}, {y + 5}, {z + 5})""")

#kyrs, num = float(input()), int(input())
#text = f"""Current dollar rate is {kyrs}. You want to buy {num} dollars
#You must pay {kyrs * num}"""
#print(text)

"""
x, y = int(input()), int(input())
print(f"Точка(x = {x}, y = {y})")
"""
"""
number_pi = 3.141592653589793
print(f'{number_pi:.6f}')
"""
"""
number = float(input())
print(f'{number:.2f}')"""
"""
num = int(input())
print(f"{num:010d}")
"""
"""
number = int(input())
print(f"{number:-^25}")
"""
"""
text = input()
print(f"|{text:&^20}|")
print(f"|{text:&<20}|")
print(f"|{text:&>20}|")
"""

#_______________________LIST__________________#
"""
my_list = [-214, 181, -139, 448, -664, -66, 213, 832, 717, -462, -924, -706, -85, -244,
            -222, -340, -482, -518, -781, 759, -593, 905, -354, -377, -141, -742, 383, -381,
              109, -639, -480, -810, -686, 892, -612, 696, 993, 791, 631, -493, -218, -829, -275,
                619, -628, -241, -565, -835, -69, 747, 711, -252, -811, -407, -153, 904, 933, -254,
                  307, -493, -419, -109, -543, 155, -127, 613, -452, -459, 856, 562, 333, -66, -77, -598,
                    -779, -278, 867, 321, -20, -415, -357, 735, -906, -14, -370, 453, -630, -736, -830, -917,
                      32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
print(min(my_list), max(my_list))
"""
# Программа получает на вход список из целых чисел. Ваша задача вывести True в случае,
# если в данном списке встречается значение 777. В противном случае вывести False
"""
my_list = list(map(int,input().split()))
print(777 in my_list)
"""
# Программа получает на вход список из целых чисел. Ваша задача найти сумму списка
"""
my_list = list(map(int,input().split()))
print(sum(my_list))
"""
"""
my_list = list(map(int,input().split()))
print(min(my_list), max(my_list))
"""
# Средее арифметическое
"""
my_list = list(map(int,input().split()))
print(sum(my_list) / len(my_list))
"""
"""
a = list(map(int, input().split()))
print(a[1])
"""
# Программа получает на вход список целых чисел
# и ваша задача вывести срез списка с третьего элемента по пятый включительно.
"""
a = list(map(int, input().split()))
print(a[2:5])
"""
# Программа получает на вход список целых чисел и
# ваша задача вывести последние три элемента этого списка через срез
"""
a = list(map(int, input().split()))
print(a[-3:])
"""
# Программа получает на вход список целых чисел и 
# ваша задача вывести каждый третий элемент этого списка, начиная со второго по счету значения.
"""
a = list(map(int, input().split()))
print(a[1::3])
"""
# Программа получает на вход список целых чисел и 
# ваша задача вывести этот список  в обратном порядке
"""
a = list(map(int, input().split()))
print(a[::-1])
"""

# Перед вами список топовых сериалов по версии кинопоиска. 
# Ваша задача заменить в нем сериал "Бригада" на "Сверхъестественное" и "Друзья" на "Настоящий детектив"
"""
top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие',
        'Доктор Хаус', 'Теория большого взрыва', 'Бригада']
my_list = top[:]
my_list[2] = "Настоящий детектив"
my_list[6] = "Сверхъестественное"
print(my_list)
"""
"""
top = ['Игра престолов', 'Шерлок', 'Друзья', 'Во все тяжкие',
        'Доктор Хаус', 'Теория большого взрыва', 'Бригада']

top[top.index('Бригада')] = 'Сверхъестественное'
top[top.index('Друзья')] = 'Настоящий детектив'
print(top)
"""
# Вывод месяцев года
"""
num = int(input())
num = num - 1
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
print(months[num])
"""
# Метод append
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.append(111)
numbers.append(222)
numbers.append(789)
numbers.append(201)
print(numbers)
"""
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.extend([111, 222, 789, 201])
print(numbers)
"""
# Метод insert
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.insert(5, 111)
numbers.insert(8, 222)
numbers.insert(0, 789)
numbers.insert(11, 201)
print(numbers)
"""

# Метод extend

"""numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
extra = [43, 54, 23, 87, -4, -832, 90, 32, 543, 432, 4, 76, 8, 0, 21, 90, 32]
numbers.extend(extra)
print(numbers)
"""

# Метод pop
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
a = numbers.pop(-1)
b = numbers.pop(0)
c = numbers.pop(12)
d = numbers.pop(7)
print(numbers)
print(a + b + c + d)
"""

# Метод remove
"""
numbers = [-214, 777, 181, 9, 32, -139, 43, 89, 77, 448, -20, -917, 54, 5, 432, 43, 32,
            422, -895, 7, 198, 284, 472, 3, -986, -964, -989, 29]
numbers.remove(3)
numbers.remove(5)
numbers.remove(7)
numbers.remove(9)
print(numbers)
"""
# Метод sort
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
numbers.sort(reverse=True)
print(numbers)
"""

# Разворот
"""
my_list = list(map(int,input().split()))
my_list.reverse()
print(my_list)
"""

# Программа получает на вход список из целых чисел. Подсчитайте сколько раз в нем присутствует число 999
"""
a = list(map(int, input().split()))
print(a.count(999))
"""
# Метод copy
"""
numbers = [-214, 181, -139, 448, -20, -917, 32, 422, -895, 198, 284, 472, -986, -964, -989, 29]
copy_numbers = numbers.copy()
print(copy_numbers)
"""
# Дефиснутая фраза
# Вводится два слова через пробел. Ваша задача преобразовать данную фразу таким образом,
# чтобы все буквы стали заглавными и между буквами в каждом слове появились дефисы
"""
sp = input().upper()
word1, word2 = sp.split()
list1 = list(word1)
list2 = list(word2)
print('-'.join(list1), '-'.join(list2))
"""
# Инициалы
#Ваша программа получает на вход строку, содержащую имя, отчество и фамилию человека
"""
i, o, f = list(input().split())
print(f"{f} {i[0]}.{o[0]}.")
"""

# Напишите программу, которая выводит слова введённой строки 
# (части, разделённые символами пустого пространства) в столбик.
# Нужно обойтись только методами split и join у строк, в программе должен быть всего один вызов print.
"""
my_list = list(input().split())
print('\n'.join(my_list))
"""

