#2

import pandas as pd

df = pd.read_csv('info.csv')
kval = int(input())
verifierset = list()

for i in (0, df.shape[0]-1):
  (gender, age, membership) = df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2]
  info = (gender, age, membership)
  verifierset.append(info)
verifierset = set(verifierset)
if len(verifierset) == kval:
  print('YES')
else:
  print('NO')