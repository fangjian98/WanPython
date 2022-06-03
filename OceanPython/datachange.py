import numpy as np
import pandas as pd
import csv

# data = pd.read_csv("imdb_top_1000.csv")
# 数据切片：data 列Series_Title 到 列Certificate
# data = data.loc[:, 'Series_Title':'Certificate']
# data = data(1)
# print(data)

# chunksize参数，设定读取的行数，返回一个固定行数的迭代器，每次读取只消耗相应行数对应的dataframe的内存，
# 从而可以有效的解决内存消耗过多的问题
# reader = pd.read_csv("imdb_top_1000.csv", header=None, chunksize=10)
reader = pd.read_csv("imdb_top_1000.csv", chunksize=10)

for i in range(1, 5):
    print(i)
    idata = reader.read(i).to_dict(orient="records")
    print(idata)
    # title = reader.read(i)
    # print(title)

# print(reader)
# print(reader.read(1))
# co = reader.loc[3:6]
# print(co)

# label = reader.get_chunk(5)
# print(label)
# dic = label.values.tolist()
# print(dic)

# print(dic[1].get(1))
# music_dict_list = label.to_dict(orient="records")
# d = dict(dic[1])
# print("this is my data")
# print(d.get(5))

# key = []
# value = []
# for i in df["Series_Title"]:  # “number”用作键
#     key.append(i)
# for j in df["Certificate"]:  # “score”用作值
#     value.append(j)
# dic = dict(zip(key, value))
# print("this is my data")
# print(dic)
