# Программа принимает на вход натуральное число N. 
# Ваша задача: вывести на экран все числа от 1 до N, каждое число на отдельной строке. 
"""
num = int(input())
for i in range(1, num + 1):
    print(i)
"""

# Напишите программу, которая выведет все элементы арифметической прогрессии от 0 до 500 включительно с шагом 5.
"""
for i in range(0, 501, 5):
    print(i)
"""

# Программа принимает на вход натуральное число N. 
# Ваша задача: вывести на экран все числа от N до 1 в сторону уменьшения, каждое число на отдельной строке. 
"""
num = int(input())
for i in range(num, 0, -1):
    print(i)
"""

# Минутка сожаления
"""
for i in range(13):
    i = "Надо было брать биткоин в 2012!"
    print(i)
"""

# Повторение - мать учения 
"""
text, num = input(), int(input())
for i in range(num):
    print(text)
"""

# Напишите программу, которая считывает два натуральных числа a и b (гарантируется, что a<b), 
# после чего для всех чисел от a до b включительно выводит:
# “Fizz”, если это число делится на 3;
# “Buzz”, если это число делится на 5;
# “FizzBuzz”, если выполнены оба предыдущих условия;
# само это число в остальных случаях.
"""
a, b = int(input()), int(input())
for i in range(a, b + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)
"""

# Квадрат и куб
"""
a, b = int(input()), int(input())
for i in range(a, b + 1):
    kv = i ** 2
    kyb = i ** 3
    print(f"Число {i}; его квадрат = {kv}; его куб = {kyb}")
"""    
# Кратные 3 или 5
"""
num = int(input())
sum = 0
for i in range(1, num):
    if i % 3 == 0 or i % 5 == 0:
        sum += i
print(sum)
"""
# Напишите программу, которая найдет сумму кубов натуральных чисел от 50 до 100 включительно
"""
sum = 0
for i in range(50, 101):
    i = i ** 3
    sum += i
print(sum)
"""

#  Факториал числа

"""
num = int(input())
fak = 1
for i in range(1, num + 1):
    fak *= i
print(fak)
"""

# Мишка и игра
"""
raund = int(input())
count_M = 0
count_C = 0
for i in range(1, raund + 1):
    M, C = map(int,input().split())
    if M > C:
        count_M += 1
    elif C > M:
        count_C += 1
if count_M > count_C:
    print("Mishka")
elif count_M < count_C:
    print("Chris")
else:
    print("Friendship is magic!^^")
"""

# Найдите, в каких строках из введённых и в каком месте упоминается "рок", причем регистр букв не важен.
# Вместо явного цикла прохода по строке в цикле используйте подходящий метод строки.
"""
n = int(input())
for i in range(1, n + 1):
    word = input().lower()
    if 'рок' in word:
        print(i, word.find('рок') + 1)
"""
# Предположим, вы переписываете у друга рецепты в блокнотик, но вам не нравится "соль".
# Переписывайте без этого слова.
"""
n = int(input())
sp = []
for i in range(1, n + 1):
    text = input()
    if not'соль' in text:
        sp.append(text)
print(', '.join(sp))
"""

# Слишком длинные слова
"""
n = int(input())
for i in range(1, n + 1):
    word = input()
    if len(word) < 10:
        print(word)
    else:
        print(word[0] + str(len(word[1:-1])) + word[-1])
"""

# Перед вами список numbers, состоящий из 100 целых чисел
#Ваша задачи пройтись в цикле по элементам списка и вывести на экран каждый элемент на отдельной строке
"""
numbers = [99, 50, -16, 9, 47, -62, 5, -64, -68, 85, 11, -20, 16, 96, -43, 46, -25, 33, 81, -30, 64, 66, -11, 60, 3, -5, -1,
 -80, 49, -12, -86, -40, -98, -92, -91, -71, 56, -76, -30, -82, 17, -2, -64, 47, 22, -28, 40, 55, 54, -3, -58, -10,
 -35, -15, -2, -60, 70, 50, -77, 83, -49, 42, 27, -58, -79, -2, -100, -42, -18, 38, 95, 9, 98, -89, -46, 96, 64,
 -35, 41, 94, 1, -90, 29, 23, 39, -3, 11, -65, -64, 52, -69, 32, -14, -49, -28, -11, 85, -75, -6, 15]

for i in numbers:
    print(i)
"""

# Перед вами список words, состоящий из 100 строк
# Ваша задачи пройтись в цикле по элементам списка и вывести на экран только те элементы, длина которых больше 6.
# Выводить каждый элемент нужно на отдельной строке в том же порядке, в котором слова расположены в списке words
"""
words = ['require', 'build', 'head', 'land', 'dark', 'seat', 'have', 'five', 'particularly', 'focus', 'moment',
           'visit', 'past', 'turn', 'bad', 'modern', 'once', 'future', 'pay', 'assume', 'himself', 'physical', 'chance',
           'remember', 'better', 'former', 'believe', 'explain', 'reduce', 'whatever', 'theory', 'during', 'enough',
           'wall', 'commercial', 'challenge', 'tell', 'actually', 'include', 'somebody', 'decade', 'by', 'better',
           'would', 'five', 'cost', 'kitchen', 'our', 'affect', 'board', 'practice', 'full', 'instead', 'apply', 'good',
           'past', 'clearly', 'special', 'both', 'analysis', 'peace', 'truth', 'cultural', 'light', 'answer', 'build',
           'each', 'watch', 'buy', 'theory', 'pretty', 'expect', 'account', 'music', 'sell', 'newspaper', 'reach',
           'fish', 'tax', 'employee', 'start', 'most', 'during', 'citizen', 'develop', 'carry', 'only', 'certainly',
           'rock', 'economy', 'risk', 'later', 'one', 'body', 'star', 'they', 'choice', 'appear', 'return', 'sometimes']

for i in words:
    if len(i) > 6:
        print(i)
"""

# Перед вами список numbers, состоящий из 100 целых чисел
# Ваша задача пройтись в цикле по элементам списка и увеличить каждый в 2 раза.
# В итоге изначальный список numbers  должен измениться
# В качестве ответа распечатайте измененный список numbers
"""
numbers = [-35, 68, -91, 23, -92, -82, -74, 32, 39, -30, -100, -29, 54, 26, 54,
            -45, 20, 53, -17, 68, -35, 11, 26, -17, 70, 89, -81, -4, 61, -45, 13,
              63, -48, -66, -92, -15, -88, -87, -75, 44, -49, -81, 19, -33, -59, 85,
                -69, -60, 9, -98, 28, 11, 15, -35, -80, 5, -20, -52, -45, 26, 47, -16,
                  40, -14, -12, 15, 73, -16, 29, -98, 93, -77, 1, 85, 77, 73, 100, -71,
                    99, 39, 2, -38, 49, -31, 15, 43, 94, -39, -89, -46, -71, 39, -56, 41,
                    -93, 4, -79, 48, 88, -51]
for i in range (len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers)
"""

# Заполняем список
# Ваша задача создать список из n строк. Программа сперва будет принимать натуральное число n, 
# а затем n строк в каждой отдельной строке. 
# В качестве ответа выведите получившийся список.
"""
n = int(input())
sp = []
for i in range(1, n + 1):
    word = input()
    sp.append(word)
print(sp)
"""

# На первой строке вводится один символ — строчная буква.
# На второй строке вводится предложение.
# Нужно вывести список слов (словом считается часть предложения, окружённая символами пустого пространства), 
# в которых присутствует введённая буква в любом регистре, в том же порядке, в каком они встречаются в предложении.
"""
symbol = input()
text = list(input().split())
sp = []
for i in range(len(text)):
    if symbol in text[i].lower():
        sp.append(text[i])
print(*sp, sep='\n')
"""
# Линейный поиск
# Программа получает на вход в одной строке элементы списка - целые числа, разделенные пробелом. 
# Количество элементов произвольное
# И на следующей строке вводится одно число r - значение поиска
"""
numbers = list(input().split())
num = input()
for i in range(len(numbers)):
    if num in numbers[i]:
        print(i + 1)
        break
else:
    print("ErrorValue")
"""
# На вход программе поступает список из целых чисел. 
# Ваша задача найти в данном списке наименьшее положительное значение. 
# В случае, если положительных значений нет, выведите строку "Empty"
"""
numbers = list(map(int,input().split()))
sp = []
for i in range(len(numbers)):
    if numbers[i] > 0:
        sp.append(numbers[i])
if len(sp) > 0:
    print(min(sp))
else:
    print("Empty")
"""


