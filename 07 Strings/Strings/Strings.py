﻿#Задание 1
# На вход подается 1 строка без пробелов. По данной строке определите, является ли она палиндромом (то есть, можно ли прочесть ее наоборот, как, 
# например, слово "шалаш"). Необходимо вывести ”yes”, если строка является палиндромом, и “no” в противном случае.

print("Задача 1. Палиндром.")
s = input("Введите строку без пробелов: ")
if s == s[::-1]:
    print("yes")
else:
    print("no")
    

#Задание No2
#Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд пробелы в один. Выведите измененную строку.

print("Задача 2. Удаление лишних пробелов.")
s = input("Введите строку: ")
start = end = i = 0
new_s = ""
is_space = s[0]==' '
while start < len(s):
    while end < len(s) and ((is_space and s[end] == ' ') or (not is_space and s[end] != ' ')):
        end += 1
    if is_space:
        new_s = new_s + " " 
    else:
        new_s = new_s + s[start:end]
    start = end            
    is_space = not is_space    
print(new_s)