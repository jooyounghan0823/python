#학생관리 시스템의 학생 클래스 만들기
#이름과 나이 학년 전공 듣고 있는 수업

class Student:
    def __init__(self,a,b,c):
        self.name = a
        self.grade = b
        self.major = c
        self.courses = []
    def enroll_courses(self, courses):
        if len(self.courses) < 5:
            self.courses.append(courses)
        else:
            print('수업듣는 과목이 너무 많습니다.')
    def cancel_course(self):
        if len(self.courses) == 0:
            print('과목이 없습니다. 밸 수가 없어요')
        else:
            for index, item in enumerate(self.courses):
                print(f"{index}.{item}")
            removeTarger = int(input("빼고 싶은 과목의 번호를 선액:"))
            del self.courses[removeTarger]

    def imformate(self):
        print(f"{self.name} {self.grade} {self.major}")
        for index,elem in enumerate(self.courses):
            print(f"{index}. {elem}")

#kim = Student('김주영','3','철학과')
#kim.enroll_courses('철학의 이해')
#kim.enroll_courses('철학의 쓸모')
#kim.imformate()


##circle_변수_반지름
#함수: 원 넓이, 원 둘레


#lass Circle:
    #def __init__(self,x):
        #self.r = a
    #def width(self):
        #print(f"원의 넓이는 {self.r **2 *3.14}")
    #def round(self):
        #print(f"원의 둘레는 {self.r *2 *3.14}")
#a = Circle(5)
#a.width()
#a.round()
#b = Circle(7)
#b.width()
#b.round()


###Day11인데 저번 주 거 퀴즈
#1. 최대 5명씩 탑승가능한 놀이기구를 타기 위해 줄을 서있는 사람들의 이름이 담긴 문자열 리스트 names가 주어질때, 앞에서 부터 5명씩 묶은 그룹의 가장 앞에 서있는 이름을 담은
#리스트를 return 하도록 solution함수를 완성해 주세요. 마지막그룹이 5명이 되지 않더라도 가장 앞에 있는 사람의 이름을 포함합니다.


#def solution(riders):
    #for index, item in enumerate(riders):
        #print(f"{index}. {item}")














#2. ad 제거하기
#문자열 배열 strArr가 주어집니다. 배열 내의 문자열 중 "ad"라는 부분 문자아ㅕㄹ을 포함하고 있는 모든 문자열을 제거하고 남은 문자열을 순서를 유지하여 배열로 return하는 solution함수를 완성해 주세요.



####짝수번째 애들만 골라라



def get_even_items(list):
  """짝수번째 애들을 반환합니다."""
  return [item for i, item in enumerate(list) if i % 2 == 0]


list = ['아메리카노','라떼','빅메리카노','연유라떼','바닐라라떼','디카페인커피','맥심커피']
print(get_even_items(list))