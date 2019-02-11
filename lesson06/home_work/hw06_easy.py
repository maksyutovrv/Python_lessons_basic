# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)

# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов

class TownCar:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def car_go(self):
        print('Машина {} начала свое движение!'.format(self.name))

    def car_stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def car_turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))

    def go(self):
        print('Машина {} поехала!'.format(self.name))

    def stop(self):
        print('Машина {} остановилась!'.format(self.name))

    def turn(self, direction):
        print('Машина {} повернула {}!'.format(self.name, direction))


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)



class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=False)


class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police=False):
        TownCar.__init__(self, speed, color, name, is_police=True)


my_car = TownCar(100, 'Blue', 'TESLA')

my_car.car_go()
my_car.car_turn('Налево')
my_car.car_stop()