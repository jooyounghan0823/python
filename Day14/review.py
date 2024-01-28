#올리브영
#name->faker
#age->20 30 40 50
#gender->2:8
#items->바디워시, 선크림, 스킨, 로션, 샴푸, 스낵, 향수, 헤어제품
#times-> 아침 점심 저녁 밤


# cgv 이름 나이 무비 팜콘 드링크 해서 데이터 100개 나오게.
import pandas
import random
from faker import Faker

faker = Faker('ko_KR')
age = [20, 30, 40, 50]
agePer = [40, 30, 20, 10]
gender = ['남자','여자']
genderPer = [20, 80]
items = ['바디워시', '선크림', '스킨', '로션', '샴푸','스낵','향수','헤어제품']
itemsPer = [13,13,13,13,13,13, 10, 12]
times = ['아침', '점심', '저녁', '밤']
timesPer = [5, 35, 40,20]

data = {
    'name': [faker.name() for i in range(100)],
    'age': [random.choices(age, weights=agePer, k=1)[0] for i in range(100)],
    'gender': [random.choices(gender, weights=genderPer, k=1)[0] for i in range(100)],
    'items': [random.choices(items, weights=itemsPer, k=1)[0] for i in range(100)],
    'times': [random.choices(times, weights=timesPer, k=1)[0] for i in range(100)],

}

df = pandas.DataFrame(data)
df.to_csv('olive.csv', encoding = 'utf-8-sig', index = False)



cgv

