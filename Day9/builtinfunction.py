#built in function



#numList = [1,2,3,4,5]
#a = map(lambda x: x+10,numList)
#print(list(a))


#numList = [1,2,3]
#a = map(lambda x: x**2, numList)
#print(list(a))


#numList = [1,2,3]
#a = map(lambda x: '토끼' if x % 2 == 0 else '당근',numList)
#print(List(a))

#fruitsList = ['apple','strawberry','banana','orange']
#a = map(lambda x: x.upper(), fruitsList)
#print(list(a))

#fruitsList = ['apple','strawberry','banana','orange']
#a = map(lambda x: len(x), fruitsList)
#print(list(a))


#1.랜덤(1-100)을 이욯해서 리스트 길이가 10 인거 구현하고 출력후, 여기서 홀수 따로 짝수 따로 나누고 출력하기.
#2.랜덤(1-30)뽑고 리스트 길이가 10 출력,1-10은 토끼, 11-20 원숭이 21-30 개 로 바꾸로 출력하기.
#3.함수를 구현하는데 이 함수는 n,m 이라는 매개변수 주면, n~m까지의 정수인 리스트 5개를 만들어주는 함수 구현하기.
#1번답
#import random
#numList = []
#for i in range(10):
    #numList.append(random.randint(1, 101))
#print(numList)
#oddList = []
#evenList = []
#for i in numList:
    #if i %2 ==0:
        #evenList.append(i)
    #else:
        #oddList.append(i)
#print(oddList)
#print(evenList)

#2번답
numList = [random.randint(1,31) for i in range(101)]
zooList = []
for i in numList:
    if 1<= i and i <= 10:
        zooList.append('개')
    elif 11<= i and i<= 20:
        zooList.append('토끼')
    else:
        zooList.append('당근')
print(numList)
print(zooList)


#3번답
def makeList(m,n):
    return[random.randint(m,n+1) for i in range(5)]
lambda m,n:[random.randint(m,n+1) for i in range(5)]











