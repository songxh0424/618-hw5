import pandas as pd
df = pd.read_csv('si618_f17_hw5_batch_result_songxh_jihzhong.csv')
df=df[['Input.pagename','Input.post_id','Input.comment_id','Answer.question']]
df = df.rename(columns=lambda x: x.replace('Input.', ''))
df=df.assign(answer_1=0, answer_2=0,answer_3=0,answer_4=0,answer_5=0,answer_6=0)
for i in range(300):
    m=df['Answer.question'].iloc[i].split("|")
    if len(m)>1:
        for k in range(len(m)):
            for j in list(range(1, 7)):
                if int(m[k]) == j:
                    df.iloc[i, j + 3]=1
    else:
        for j in list(range(1, 7)):
           if int(df['Answer.question'].iloc[i])==j:
             df.iloc[i,j+3]=1

df = df.drop('Answer.question', 1)
df = df.groupby(['pagename','post_id','comment_id'], as_index=False)['answer_1', 'answer_2','answer_3','answer_4','answer_5','answer_6'].sum()
df.to_csv('si618_f17_hw5_cleaned_data_songxh_jihzhong.csv', index=False)
