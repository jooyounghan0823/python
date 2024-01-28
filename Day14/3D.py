import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv('cgv.csv')

#시간때 별로 음료 고를게요


grouping = df.groupby(['movie','popcorn'])
#크기계산
sizeGroup = grouping.size()
print(sizeGroup)
#테이블화
table = sizeGroup.unstack(fill_value=0)
plt.rcParams["font.family"] = 'Malgun Gothic'
sns.heatmap(table,cmap='coolwarm')
plt.xticks(rotation=45)
plt.yticks(rotation=45)
plt.show()
