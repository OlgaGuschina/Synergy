﻿#Задание1
print("Сколько чисел вы будете вводить?")
N = int(input())
cnt = 0
for i in range(N):
    a = int(input())
    if a == 0:
        cnt += 1
print("Среди ваших чисел", cnt, "нулей.")    

#Задание2
print("Введите натуральное число")
N = int(input())
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
print("Число", N, "имеет", cnt, "делителей.")

#Задание3
print("Введите число A")
A = int(input())
print("Введите число B>=A")
B = int(input())
for i in range(A, B+1):
    if i % 2 == 0:
        print(i, end = " ")
        
#Задание3 способ 2
print()
print("Введите число A")
A = int(input())
print("Введите число B>=A")
B = int(input())
s = ""
for i in range(A, B+1):
    if i % 2 == 0:
        s += str(i) + " "
print(s)        