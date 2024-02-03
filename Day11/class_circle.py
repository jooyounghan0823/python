#class Circle:
    #def __init__(self,r):
        #self.radius = r
        #def get_area(self):
            #return 3.14 * self.radius **2
        #def get_round(self):
            #return 3.14 * self.radius *2
#a = Circle(10)
#print(a.get_area())
#print(a.get_round())


#정삼각형, 정사각형 넓이 구하라.
#class triangle:
    #def __init__(self,b,h):
        #self.base = b
        #self.height = h
   #def get_area(self):
       #return self.base * self.height *0.5
   #def get_round(self):
       #return self.base *3

#class square:
    #def __init__(self,s):
        #self.side = s
    #def get_area(self):
        #return self.side * self.side

###클래스 연습하기.
#은행계좌 클래스(BANK acoount)
#속성: 계좌번호, 소유자이름. 잔액
#메서드: 입금하기, 출금하기, 잔액 확인하기

#class Account:
    #def __init__(self,a,b,c):
        #self.number = a
        #self.owner = b
        #self.balance= c

    #def depoist(self, money):
        #self.balance += money
        #print('입금이 되었습니다.')

    #def withdraw(selfself, money):
        #if(self.balance < money):
            #print('잔고가 부족합니다')
        #else:
            #self.balance -= money
            #print('출금이 되었습니다')
    #def checkBalnce(self):
        #print(f"잔액은 {self.balance}  남았습니다.")

#han = Account(100, 'han', 100000)
#han.deposit(50000)
#han.checkBalance()
#han.withdraw(500000)
#han.withdraw(30000)
#han.checkBalance()


##쇼핑카트 시스템_속성: 상품목록, 총금액, 메서드: 상품추가하기, 상품삭제
class Cart:
    def __init__(self):
        self.itemList = []
        self.total = 0

    def additem(self, item):
        self.itemList.append(item)
        print(f"{item.name} 이 추가 되었습니다.")
        self.itemList.append(item)
    def removeItem(self):
        for index, item in enumerate(self.itemList):
            print(f"{index}.{item}")
        num = int(input("삭제할 상품의 번호를 선택하세요:"))
        self.itemList.pop(num)
        print("삭제 되었습니다.")
    def totalAmount(self):
        total = 0
        for i in self.itemList:
            total = i['price']
        print(f"총 금액은 {total}입니다.")

    myCart = Cart()
    myCart.addItem({'name': '샴푸','price':'5000'})
    myCart.addItem({'name': '린스', 'price': '10000'})
    myCart.addItem({'name': '트리트먼트', 'price': '8000'})
    myCart.addItem({'name': '에센스', 'price': '7000'})
    myCart.removeItem()
    myCart.totalAmount()







