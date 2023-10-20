class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} - {capacity} пассажиров"

#Задание №1        
#Создайте объект Autobus, который унаследует все переменные и методы родительского класса Transport
#и выведете его.Ожидаемый результат вывода:Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12

print("Задание 1")
autobus = Transport("Renault Logan", 180, 12)
print(f"Название автомобиля: {autobus.name} Скорость: {autobus.max_speed} Пробег: {autobus.mileage}")

#Задание 2
#Создайте класс Autobus, который наследуется от класса Transport. Дайте аргументу Autobus.seating_capacity()значение по умолчанию 50.
#Используйте переопределение метода.

class Autobus(Transport):
        
    def seating_capacity(self, capacity = 50):
        return f"Вместимость одного автобуса {self.name} - {capacity} пассажиров"
    
print("Задание 2")
autobus2 = Autobus("Renault Logan", 180, 12)
print(autobus2.seating_capacity())