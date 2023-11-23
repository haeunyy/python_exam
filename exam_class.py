# 부모 클래스
class Car:
    def __init__(self, tier, price):
        self.tier = tier
        self.price = price

    def info(self):
        pass

# 상속받는 class
class Bicycle(Car):
    def __init__(self, tier, price, machine):
        super().__init__(tier, price)
        self.machine = machine

    def info(self):
        print("바퀴수 : {0} \n가격 : {1} \n구동계 : {2}".\
              format(self.tier, self.price, self.machine))

ben = Bicycle(2, 25000, "시마노") 

ben.info()

