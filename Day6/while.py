######업앤다운 게임######
# 1)0~100까지 랜덤한 숫자 뽑기
# 2)유저가 맞출때 까지 게임 진행
# 만약에 유저가 숫자가 랜덤보다 크면 출력 후 다시 맞추기
# 유저가 랜덤보다 높으면 다시 맞추기
# 유저가 랜덤이랑 같으면 정답입니다. 때려맞춘 횟수 n 프로그램 종료
###이거 폰에 있음_확인해라

#####유저가 0을 입력 할 때까지 여러정수를 입력받고 정수의 총합을 구하는 프로그램

# sum = 0
# while true:
# num = int(input("숫자를 입력(0은 종료):"))
# if num == 0:
# print(sum)
# break
# sum += num

######## 일본여행 todolist_폰에 있음
#######다하기 빼기 프로그램
# 1. 더하기
# 1-1) 첫번째
# 1-2)두번째
# 1-3) 더한값은 ~입니다.
# 2. 빼기
# 3. 종료


while True:
    code = int(input("1.두수의 더하기 2. 두수의 빼기 3. 종료"))
    if code == 1:
        one = int(input("숫자를입력:"))
        two = int(input("숫자를 입력:"))
        print(one+two)


