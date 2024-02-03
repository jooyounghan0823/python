# import pandas # 판다스
# import random

# fake = Faker('ko_KR')

# data = {
# 'name': [fake.name() for i in range(500)],
# 'ages': [random.randint(20,61) for i in range(500) ]
# }
# a = pandas.DataFrame(data)
# a.to_csv('people.csv', encoding = 'utf-8-sig', index = False)

# cgv 이름 나이 무비 팜콘 드링크 해서 데이터 500개 나오게.
import pandas
import random
from faker import Faker

faker = Faker('ko_KR')
age = [20, 30, 40, 50, 60]
agePer = [40, 30, 15, 10, 5]
movie = ['윙카', '시민덕희', '외계인', '너의 이름은', '도그맨', '위시']
moviePer = [35, 25, 10, 10, 10, 10]
popcorn = ['일반', '카라멜', '치즈', '어니언', '구매안함']
popcornPer = [20, 10, 10, 10, 50]
snack = ['맛밤', '오징어', '나초', '핫도그', '구매안함']
snackPer = [5, 5, 20, 10, 60]
drink = ['콜라', '제로콜라', '환타', '스프라이트', '에이드', '아메리카노', '물', '구매안함']
drinkPer = [15, 15, 10, 10, 10, 10, 20, 10]
times = ['조조', '일반', '심야']
timesPer = [20, 70, 10]
payment = ['현금', '체크카드', '신용카드', '카카오페이', '삼성페이']
paymentPer = [5, 10, 30, 5, 50]
data = {
    'name': [faker.name() for i in range(10000)],
    'age': [random.choices(age, weights=agePer, k=1)[0] for i in range(10000)],
    'movie': [random.choices(movie, weights=moviePer, k=1)[0] for i in range(10000)],
    'popcorn': [random.choices(popcorn, weights=popcornPer, k=1)[0] for i in range(10000)],
    'snack': [random.choices(snack, weights=snackPer, k=1)[0] for i in range(10000)],
    'drink': [random.choices(drink, weights=drinkPer, k=1)[0] for i in range(10000)],
    'times': [random.choices(times, weights=timesPer, k=1)[0] for i in range(10000)],
    'payment': [random.choices(payment, weights=paymentPer, k=1)[0] for i in range(10000)],
}

df = pandas.DataFrame(data)
df.to_csv('cgv.csv', encoding = 'utf-8-sig', index = False)


