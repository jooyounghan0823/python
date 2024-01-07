import pandas as pd

df = pd.read_csv('breast.csv')

selected_columns = df.iloc[:, [1, 3]]
selected_data = selected_columns.iloc[2:]
data_dict = selected_data.to_dict(orient='list')
patientList = data_dict['하위']
hmgb1List = data_dict['Unnamed: 1']
data = [{'patient':patientList[i],'HMGB1':float(hmgb1List[i])} for i in range(1, len(patientList))]
data.sort(key=lambda x: x['HMGB1'], reverse=True)

onePercent = 0.01


# for i in range(1,158):
#     genes[0]['HMGB1']
#     a.append(genes[0]['HMGB1'])
#     a.sort()
#     rank = len(a)*0.01
#     print(rank)
