#int, float, bool, str, dict, list, tuple, set


#나만의 데이터 타입 만들기.
#기본형 -> 구조체(c언어)[struct](기본형 모음)라고 한다.-> 구조체에 함수를 넣은게 클래스[class]=구조체(변수)+ 함수
#height[float] -> student[str, int, int]

#class Dog:
    #def __init__(self):_
        #self.breed = '말티즈'
        #self.snackList = ['개껌','개사료']
    #def bark(self):
        #print("멍멍!")
#a = Dog()
#a.bark()
#b = Dog()
#b.bark()


#class burger:
    #def __init__(self):
        #self.bread = '참깨방'
        #self.ingredients = ['토마토','양파']
        #self.source = '마요네즈'
    #def addIngredient(self,x):
        #self.ingredients.append(x)

#c = burger()
#print(c.bread)
#print(c.ingredients)

#c를 인스턴스라고 한다.
#객체 지향 프로그래밍[oop]
#object oriented programming

#클래스 변수
class Dog:
    def __init__(self,x):
        self.name = x
        self.hp = 100
        self.emotionstate = 'happy'
        self.hungry = 0
        self.friends = []

    def eating(self):
        if self.hp <200:
            self.hp +=10
        else:
            print("체력이 꽉 찼습니다.")
a = Dog('jenny')
for i in range(100):
    print(f"{i}")
    a.eating










a.eating()
a.eating()
b = Dog('donald')
print(f"{a.name} {a.hp}")
print(f"{b.name} {b.hp}")





