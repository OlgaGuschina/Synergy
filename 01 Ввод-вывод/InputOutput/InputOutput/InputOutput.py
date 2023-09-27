print("Пожалуйста, введите, кто ваш питомец?")
type = input()
print("Введите имя:")
name = input()
print("Введите возраст:")
age = int(input())
rem = age % 10
if rem == 1 :
    str_end = "год."
elif rem > 1 and rem < 5:
    str_end = "года."
else:
    str_end = "лет."
print("Это ", type, "по кличке \"", name, ". Возраст: ", age, str_end)

#Классификаций разных много, я выбрала что попроще, не на биолога же учимся))) https://xn--e1adcaacuhnujm.xn--p1ai/evolyuciya-cheloveka.html
print("Введите 4 основные стадии антропогенеза, разделяя разные стадии запятой:")
a,b,c,d = input().split(sep=",")
print(a.strip(), b.strip(), c.strip(), d.strip(), sep="=>")
