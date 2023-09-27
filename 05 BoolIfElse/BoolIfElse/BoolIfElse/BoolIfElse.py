#Задача 1
# Пользователь вводит целое число. Выведите его строку-описание вида 
# "отрицательное четное число", "нулевое число", "положительное нечетное число", например, численным описанием числа 190 является строка 
# "положительное четное число". Если число не является четным - выведите сообщение "число не является четным" 

#Последнее предложение задачи кажется лишним, но сделала как задано
N = int(input())
if N == 0:
    print("Нулевое число")
else:
    add_str = ""
    if N > 0:
        sign = "Положительное"
    else:
        sign = "Отрицательное"
    if N % 2 == 1:
        parity = "нечётное"
        add_str = "Число не является чётным"
    else:
        parity = "чётное"
    print(sign, parity, "число.")
    if add_str != "":
        print(add_str)
        
#Задача 2
def print_letter(name, count):
    if count > 0:
        print(name+":", count, "шт.")
    else:
        print(name+":", str(False))
        
print()
print("Введите слово маленькими латинскими буквами:")
word = input()
Na = No = Ni = Ne = Nu = N = 0
for char in word:
    if char == 'a':
        Na += 1
    elif char == 'o':
        No += 1
    elif char == 'i':
        Ni += 1
    elif char == 'e':
        Ne += 1
    elif char == 'u':
        Nu += 1
    else:
        N += 1
print("Согласных", N, "букв.")
print("Гласных", Na+No+Ne+Ni+Nu, "букв.")
print("Из них")
print_letter("a", Na)
print_letter("o", No)
print_letter("i", Ni)
print_letter("e", Ne)
print_letter("u", Nu)

#Задача 3
print()
print("Введите минимальную сумму инвестиций: ")
X = int(input())
print("Введите сумму Майкла: ")
A = int(input())
print("Введите сумму Ивана: ")
B = int(input())
if A + B < X:
    print(0)
elif A < X and B < X:
    print(1)
elif A >= X and B < X:
    print("Mike")
elif A < X and B >= X:
    print("Иван")
else:
    print(2)
    


         
