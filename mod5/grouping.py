import pandas as pd

df = pd.DataFrame({
    'Department': ['CS', 'CS', 'Math', 'Math', 'Physics'],
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Marks': [85, 75, 90, 95, 80]
})

print(df)
print(df['Department'].value_counts())
print(df['Marks'].idxmax())
print(df.loc[df.groupby('Department')['Marks'].idxmax(),['Student','Department']])
# print(df.groupby('Department')['Marks'].agg(['mean','median','count']))
# print(df.groupby('Department')['Marks'].agg(['mean', 'sum', 'count']))
