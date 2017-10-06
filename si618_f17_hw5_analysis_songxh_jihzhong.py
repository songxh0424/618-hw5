import pandas as pd
import numpy as np

df = pd.read_csv('./si618_f17_hw5_cleaned_data_songxh_jihzhong.csv')
df = df.assign(attack = df.iloc[:, 3:7].sum(axis = 1), noattack = df.iloc[:, 7])

# 1: all three workers agree on whether or not there is a personal attack
frac1 = sum((df['attack'] >= 3) & (df['noattack'] == 0)) + \
    sum((df['attack'] == 0) & (df['noattack'] >= 3))
frac1 = frac1 / 100

# 2: at least 2 workers believe there is a personal attack
frac2 = sum(df['attack'] >= 2) / 100

# 3: at least 1 worker believe there is a personal attack
frac3 = sum(df['attack'] >= 1) / 100

# write txt file
with open('si618_f17_hw5_analysis_output_songxh_jihzhong.txt', 'w+') as f:
    f.write('%s\n%s\n%s' % (frac1, frac2, frac3))

