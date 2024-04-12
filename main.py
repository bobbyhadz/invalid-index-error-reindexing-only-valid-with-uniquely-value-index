# Reindexing only valid with uniquely valued Index objects

import pandas as pd


df1 = pd.DataFrame(index=[1, 0, 1], columns=['A'], data=[1, 2, 3])

df2 = pd.DataFrame(index=[0, 1, 1], columns=['B'], data=[4, 5, 6])

df1 = df1.reset_index()
df2 = df2.reset_index()

df3 = pd.concat([df1, df2], axis=1)

#    index  A  index  B
# 0      1  1      0  4
# 1      0  2      1  5
# 2      1  3      1  6
print(df3)