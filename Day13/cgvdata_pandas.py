import pandas

df = pandas.read_csv('../Day14/cgv.csv')
#print(df.index) #몇개 행
#print(df.column) #몇개 열이 있는지
#print(df.values) # 데이터 알려주기
#print(df.describe()) #수치형 통계
#print(df['snack']) # 스낵에 해당하는 열 보여주기
#print(df[['movie','drink']])
#print(df[df['movie'] == '윙카']) #영화 윙카 본 사람들 보여주기
#print(df[df['snack'] == '나초'][df['movie'] == '윙카']) #윙카 본 사람이랑 나초 같이 먹은 사람들 이름 나오게 하기.
print(df[df['age'] == 30][df['payment'] == '신용카드'][df['times'] == '조조'])

