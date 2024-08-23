#!/usr/bin/env python3

import pandas as pd

df = pd.read_csv("a.csv", index_col=0)
df2 =  pd.DataFrame(index=df.index.to_list() , columns=df.index.to_list() + ["total"])
print(df)
print("-" * 20)

for idx1 in range(len(df)):
        p1 = df.iloc[idx1]
        t_c = 0
        t_w = 0
        for idx2 in range(len(df)):
                p2 = df.iloc[idx2]
                if p1.name == p2.name:
                        df2[p2.name][p1.name] = ""
                        continue

                t = len(pd.concat([p1,p2], axis=1).dropna())
                w = (p1 < p2).sum()
                l = t - w

                t_c += t
                t_w += w

                if t:
                        p = round(float(w / t * 100), 1)
                else:
                        p = "--.-"
                df2[p2.name][p1.name] = f"{w}-{l} ({p}%)"

        if t_c:
                t_p = round(float(t_w / t_c * 100), 1)
        else:
                t_p = "--.-"
        df2["total"][p1.name] = f"{t_w}-{t_c-t_w} ({t_p}%)"
