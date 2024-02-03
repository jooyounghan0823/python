#1. 정삼각형의 넓이를 돌려주는 함수
#-매개변수는 밑변, 높이 돌려주는 건 넓이
#2. 정사각형의 넓이를 만들어주는 함수
#-매개변수는 변
#3. 원의 넓이 또는 둘레를 돌려주는 함수
#-반지름, flag(true[넓이],false[둘레])
#(밑변 × 높이) / 2

#정삼각형
#def triangle(base,height):
    #return base * height * 0.5
#print(폰에 있음)


#2. 정사각형의 넓이를 만들어주는 함수
#-매개변수는 변
#def squre(slide)
    #return slied**2
#프린트하는것은폰에 있음


#print("피자완성")

def marasoup(*topping):
    topList = []
    for i in topping:
        topList.append(i)
    print(f"{topList} 마라탕 완성!")

marasoup(*topping:'당면','새우')


#marasoup(*toppimg:'당면','새우','두부','라면')