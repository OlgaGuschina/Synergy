#Задание1
N = int(input("Сколько чисел вы будете вводить? "))
cnt = 0
for i in range(N):
    a = int(input())
    if a == 0:
        cnt += 1
print("Среди ваших чисел", cnt, "нулей.")    

#Задание2
N = int(input("Введите натуральное число: "))
cnt = 0
for i in range(1, N+1):
    if N % i == 0:
        cnt += 1
print("Число", N, "имеет", cnt, "делителей.")

#Задание3
A, B = map(int, input("Введите числа A и В через пробел (В >= А): ").split())
for i in range(A, B+1):
    if i!=0 and i % 2 == 0:
        print(i, end = " ")
        
#Задание3 способ 2
print()
A, B = map(int, input("Введите числа A и В через пробел (В >= А): ").split())
s = ""
for i in range(A, B+1):
    if i!=0 and i % 2 == 0:
        s += str(i) + " "
print(s)        