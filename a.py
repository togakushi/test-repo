#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("a.csv", index_col=0)
df2 =  pd.DataFrame(index=df.index.to_list() , columns=df.index.to_list())
df3 =  pd.DataFrame(index=df.index.to_list() , columns=df.index.to_list())
print(df)
print("-" * 20)

for idx1 in range(len(df)):
        p1 = df.iloc[idx1]
        for idx2 in range(len(df)):
                p2 = df.iloc[idx2]

                if p1.name == p2.name:
                        continue
                df2[p2.name][p1.name] = (p1 < p2).sum()
                df3[p2.name][p1.name] = len(pd.concat([p1,p2], axis=1).dropna())


print("-" * 20)
print(df2)
print(df3)
