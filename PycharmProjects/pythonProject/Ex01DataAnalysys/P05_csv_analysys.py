import pandas as pd
import csv
import matplotlib.pyplot as plt

# open()으로 읽을 때
f = open('download_file.csv','r',encoding='cp949')
result = csv.reader(f)
# result = csv.reader(f): print(r) # 반복문으로 읽을 떼
# print(next(result)) #건바이 건으로 읽을 수 있다.
# print(next(result)) #건바이 건으로 읽을 수 있다.
# print(next(result)) #건바이 건으로 읽을 수 있다.

#pandas에서 읽을 때
result = pd.read_csv('download_file.csv',encoding='cp949')
print(result, type(result)) #<class 'pandas.core.frame.DataFrame'>
print(result.columns)
print(result.iloc[1,0])
print(result.iloc[:,1])

gu = []; population = result.iloc[:,1]; population2 = result.iloc[:,2]
for g in result.iloc[:,0]:
    gu.append(str(g).split(" (")[0])
print(gu, type(gu))
print(population, type(population))