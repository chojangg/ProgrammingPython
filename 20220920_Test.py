# 옆 친구와 클래스 구조 만들고
# 객체화 하고
# 상속하고
# 출력

# 차
# 색상, 기종, 가격, 최고 시속

class Car:
    def __init__(self, name):
        self.name = name
    def set_color(self, color):
        self.color = color
    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f'기종 : {self.name} \t 색상 : {self.color} \t 가격 : {self.price}$'

class RaceCar(Car):
    def __init__(self, name):
        super().__init__(name)
    def set_speed(self, speed):
        self.speed = speed

    def __str__(self):
        return f'{super().__str__()} \t 최고 시속 : {self.speed}km/h'

F1 = RaceCar('F1')
F1.set_color('Red')
F1.set_price('10.6')
F1.set_speed('350')
print(F1)