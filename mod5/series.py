import pandas as pd
dict={'a':'neha','b':'aarya','c':'aida','d':'little'}
s=pd.Series([6,2,3,4,4],index=['a','b','c','d','e'])
s2=pd.Series([1,2,3,4,4],index=['b','c','d','f','g'])

print(s>2)
print(s[s>2])
print(s[['a','c']])

print(s.agg(['mean','sum','count']))
print(s.rank())
print(s.unique())
print(s.value_counts())
# print(s.mean())
# print(s.mode())
# print(s.median())
# print(s.var())
# print(s.std())

# print(s.abs())
# print(s.count())
# print(s.max())
# print(s.min())

# print(s.sum())
# print(s.prod())
# print(s.cumsum())
# print(s.cumprod())

# print(s.nunique())
# print(s.describe())

# print(s)
# print(s2)
# print(s+s2)
# print(s.head(2))
# print(s.tail())
# print(s.axes)
# print(s.ndim)
# print(s.size)
# print(s.dtype)
# print(s.values.itemsize)
