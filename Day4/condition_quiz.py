#조건문
#1. 알파벳 탐지기



#if 100>avg and avg>=90:
    #print("A")
#elif 90>avg and avg>=80:
    #print("B")
#elif 80>avg and avg>=70:
    #print("C")
#else:
    #print("과락입니다")

###########선생님 답지###########
# text = input("문자입력하세요:")
#if text.isalpha():
    #print("알파벳 입니다.")
#else:
    #print("알파벳이 아니다")




#대문자를넣으면 소문자가되고, 소문자를 넣으면 대문자가 되는 거############
#if text.isupper():
    #print(f"{text.lower()}")
#else:
    #print(f"{text.upper()}")


#### 비밀번호 타입체크
#####비밀번호를 입력하세요:
#1. 특수문자가 포함이 되야 합니다
#2. 첫번째 글자가 대문자야 합니다.
#3. 비밀번호의 길이가 8글자 이상이어야 한다.
#4. 비밀번호가 설정이 되었습니다.

password = input("비밀번호를 설정하세요:")

#isalumn_숫자 그리고 알파벳이 있으면 트루
if not password.isalnum():
    print("특수문자를넣으셔야 합니다")
elif not password[0].isupper():
    print("첫글자는 대문자어야 합니다")
elif len(password) <8:
    print("비밀번호가 8글자 이상이여야 합니다.")
else:
    print("비밀번호가 올바르게 설정되었습니다.")


####각도의 비밀을밝혀라
#각도를 입력해 주세요. 예각(0보다 크고 90보다 작은거)이면 직각이면 둔각(90보다 크고 180보다 작은각)이면 평각(180도)이면 4로 분류해서 알려드릴게요
#math = int(input("내가맞은 점수:"))
#if 100>math and math>=90:
    #print("A")
#elif 90>math and math>=80:
    #print("B")
#elif 80>math and math>=70:
    #print("C")
#else:
    #print("과락입니다")
angle = int(input("각도를 입력하라:"))
if 90<angle and angle>0:
    print("예각입니다")
elif 90==angle:
    print("직각입니다.")
elif 90<angle and angle<180:
    print("둔각입니다.")
else:
    print("잘못입력하셨습니다.")






