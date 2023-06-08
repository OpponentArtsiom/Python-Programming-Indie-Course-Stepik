"""
a, b, c, d = map(float,input().split())
print((a + b + c + d) / 4)
"""
"""
a, b, c, d, e = map(float,input().split())
print(max(a, b, c, d, e))
"""
"""
n, a, b = map(int, input().split()) 
print(((a * b) * 2) * n)
"""
"""
n = int(input())
a = n // 6
b = a * 4
c = n // 6
print(a, b, c)
"""
"""
x, y, z = map(int,input().split())
a = 3
b = 5
c = 12
print(a * x + b * y + c * z)
"""
"""
a, b = map(int,input().split())
total = a + b - 1
print(total - a, total - b)
"""
"""
x, y, z = map(int,input().split())
print(x, y, z, sep=',')
"""
"""
n = int(input())
a = n - 1
b = n + 1
print(a, n, b, sep='<')
"""
"""
a, b, c = input(), input(), input()
print(a, b, c, sep='---')
"""
"""
z = input()
print(1, 2, 3, 4, 5, sep=z)
"""
"""
text = input()
print(text, end=' - Сказала она!')
"""
"""
print('Гвидо', 'Ван', 'Россум', sep='*', end='-')
print('Основатель', 'Питона', sep='_', end='!')
"""
"""
n = int(input())
print(n // 1000)
"""
"""
n, k = int(input()), int(input())
print(k // n)
"""
"""
n, r = int(input()), int(input())
print(n // r)
"""
"""
n = int(input())
print(n % 1000 // 100)
"""
"""
n = int(input())
a = n % 10
b = n % 100 // 10
c = n % 1000 // 100
print(a + b + c)
"""

# Выиграть в лотерею
"""
n = int(input())
a = n // 100
total1 = n % 100
b = total1 // 20
total2 = total1 % 20
c = total2 // 10
total3 = total2 % 10
d = total3 // 5
total4 = total3 % 5
e = total4 // 1
print(a + b + c + d + e)
"""
"""
n = int(input())
n1 = n // 100 # купюры по 100
n2 = n % 100 // 20 # купюры по 20, после выдачи купюр по 100
n3 = n % 20 // 10 # купюры по 10, после выдачи купюр по 20
n4 = n % 10 // 5 # купюры по 5, после выдачи купюр по 10
n5 = n % 5 // 1 # купюры по 1, после выдачи купюр по 5
print(n1 + n2 +n3 + n4 + n5) # скалдываем кол-во купюр
"""

#Электронные часы - 1  2879
"""
n = int(input())
a = n // 60 % 24
b = n % 60
print(a, b)
"""

# Следующее четное
"""
x = int(input())
y = x // 2
print((y+1)*2)
"""

#Электронные часы - 1 3721
"""
n = int(input())
h = n // 3600 % 24
m = n // 60 % 60
s = n % 60
print('{}:{:02}:{:02}'.format(h,m,s))
"""
"""
a,b = map(int,input().split())
print((a and b) % 7 == 0)
"""
"""
x, y, z = map(int,input().split())
print(x == y == z)
"""
"""
s1, s2 = input(), input()
print(s1 == "awesome" or s2 == "awesome")
"""
"""
a, b, c = map(int, input().split())
print(a == b or a == c or b == c)
"""
"""
a, b, c = map(int, input().split())
print(a ** 2 + b**2 == c**2 or a ** 2 + c**2 == b**2 or b ** 2 + c**2 == a**2)
"""

# Перевязь
"""
from math import ceil
n = int(input())
print(ceil(n / 10))
"""
# _________
"""
from math import ceil
n = int(input())
print(ceil(n / 4))
"""
# Парты 
"""
from math import ceil
a, b, c = int(input()), int(input()), int(input())
print(ceil(a / 2) + ceil( b / 2) + ceil(c / 2))
"""
# Ремонт
"""
from math import ceil
L, W, H = map(int, input().split())
P = (L * H + W * H) * 2
print(ceil(P / 16))
"""







