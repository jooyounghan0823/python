#gruopby
#대학교에서 1학년 기준으로
#의과대생 기준으로
#유학생기준으로  라는 느낌으로 하는게 그룹바이임.

#import pandas

#df = pandas.read_csv('cgv.csv')

#groupby_movie = df.groupby('movie').value_counts()


#print(groupby_movie)


################################

#import pandas

#df = pandas.read_csv('cgv.csv')

#groupby_movie = df.groupby('movie')
#wongka = groupby_movie.get_group('윙카')

# print(wongka)

#############################
#스낵별로 묶고 무비를 보여줘.


# import pandas

#df = pandas.read_csv('cgv.csv')

#group_by_times = df.groupby('times')
#payments_by_times = group_by_times['drink'].value_counts()

#print(payments_by_times)



###########

#import pandas

#df = pandas.read_csv('cgv.csv')

#group_by_times = df.groupby('times')
#payments_by_payment = group_by_times['payment'].value_counts()

#print(payments_by_payment)


#############apply



import pandas

df = pandas.read_csv('cgv.csv')
def isElderAndNight(row):
    if row['age'] == 50 and row['times'] == "심야":
        return '이벤트 대상'
    else:
        return'아님'

def WongkaEvent(row):
    if row['movie'] == "윙카" and row['snack'] == "카라멜":
        return '이벤트 대상'
    else:
        return'아님'

df['elder_event'] = df.apply(isElderAndNight, axis=1)
df['wongka_Event'] = df.apply(WongkaEvent, axis=1)
print(df[df['elder_event']=='이벤트 대상'][df['wongka_Event'] == '이벤트 대상'])

# 어르신 이벤트에 해당하는 사람만 가져와라










