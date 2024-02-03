#inheritance(상속)
#class Shape:
    #def get_area(self):
        #pass
    #def get_round(self):
        #pass


class Animal:
    def __init__(self, b, g):
        self.breed = b
        self.gender = g
    def running(self):
        print('신나게 달립니다')
class Dog(Animal):
    def __init__(self, b, g, body):
        super().__init__(b,g)
        self.body = body
    def bark(self):
        print('멍멍')
class Cat(Animal):
    def __init__(self, b, g, eyes):
        super().__init__(b,g)
        self.eyes = eyes
    def crying(self):
        print('냐옹')
kingyul = Dog('이탈리안 하우즈', 'female', 'white')
samseki = cat('치즈냥이','male','blue')

kingyul.bark()
kingyul.running()
samseki.crying()
samseki.running()



