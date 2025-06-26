import pandas as pd
dict={'name':['neha','nelson','nebin','arya','aida'],'age':[21,19,11,21,22]}
df=pd.DataFrame(dict,index=['a','b','c','d','e'])

rf=pd.read_csv('student.csv')
rf.set_index('Name',inplace=True)
print(rf[0:4])
print(rf)
print(rf['Place'].str.strip().rank())

# rf.loc[rf['Mark']<=25,'Grade']='Fail'
# print(rf)
# max_marks=rf['Mark'].max()
# print(rf.query("Mark==@max_marks")['Name'])
# print(rf.sort_values(by='Mark',ascending=False))
# rf.set_index('Rollno',inplace=True)

# print(rf.loc[2:5,'Name':'Mark'])
# print(rf.loc[rf['Name'].str.startswith('A') & rf['Mark']>=0,'Name':'Mark'])
# print()
# print(rf['Name'].str.startswith('A'))
# print(rf['Mark']>25)
# print(rf.loc[(rf['Name'].str.startswith('A')) & (rf['Mark']>25),'Name'])

# print(rf)
# df.to_csv('vikaram.csv')
# print(df)

# print(df.index)
# print(df.columns)
# print(df.dtypes)