import pandas
import matplotlib.pyplot as plt

#x = [i for i in range(10)]
#y = [i for i in range(10,20)]
#plt.plot(x,y)
#plt.show()


##시간ㄷ때에 보는 영화를 나오게 하고 시각화 하게 하라#####

#영화 너의 이름은 본 사람중에서 스낵 비율을 나타내라

# 30대가 시민덕희를 보는 사람 중에 음료 비율을 뽑아라.


df = pandas.read_csv('cgv.csv')

age_30_civil_df = df[df['age']==30][df['movie']=='시민덕희']
drink = age_30_civil_df['drink'].value_counts()
plt.rcParams["font.family"] = 'Malgun Gothic' #한글 폰트로 나오게설정
#drink.plot.pie(autopct = '%1.1f%%')#숫자 비율을 소수점 1까지 보여주기
drink.plot(kind='bar') #바 그래프로 나타내기
plt.title("음료와 30대가 시민덕희 본 사람의 관계")
plt.show()























