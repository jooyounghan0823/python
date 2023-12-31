#유저한테 양의 정수를 입력 받고
#0~n까지의 합을 나타내는 프로그램
#num = int(input("number 입력:"))+1
#sum = 0
#for i in range(num):
    #sum = sum+i#기존에 있었던 것 누적시키는 것
    #print(sum)

##0~100 사이에서 유저한테 입력받은 n
#n의 배수의 합을 구하세요
#2를 넣으면 2의 배수의 합
#3을 넣으면 3의 배수의 합
#n = int(input("정수입력:"))

#sum = (n *(n-1))/2
#print(sum)





#########N의 배수 출력########
#n = int(input("정수입력:"))
#sum = 0
#for x in range)101):
    #if x % n == 0:
    #sum += x
    #print(sum)


#####가우스 법칙이용해서 1억을 넣으면 다1억을 다 더한 값??(이게 뭔지 다시 확인필요 )
#n = int(input("정수입력:"))

#sum = (n *(n-1))/2
#print(sum)

####줄줄이 적힌대로 나온다.############
#nation = ['미국','일본']
#for x in nation:
    #print(x)

######1. num에 랜덤 정수(0-10000)를 100개 채우기,2. num의 평균값 도출하기 #########



#1번답
#num = []
#for i in range(100):
    #num.append(random.randit(0,10001))

#2번답
#sum = 0
#for i in num:
    #sum +=1
    #print(sum/100)


#######3번문제_정수랜덤[] 10개 채워주고 리스트의 값의 제곱을한 리스트
#랜덤리스트 = [2,1,5,6,7]
#제곱리스트 = [4,1,25,,36,49]

#1.빈리스트 만들기
#2. 빈리스트에 랜덤한 숫자 10개 채우기
import random
num = []
for i in range(10):
    num.append(random.randit(1,101))
#원래 리스트의 제곱한 리스트 만들기
double_num = []
for i in num:
    double_num.append(i**2)
print(num)
print(double_num)







