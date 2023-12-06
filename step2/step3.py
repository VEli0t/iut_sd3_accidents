import pandas as pd 

df = pd.read_csv("missing_values_deleted.csv", sep=",")

df = df.drop(columns=['an'])

hrmn=pd.cut(df['hrmn'],24,labels=[str(i) for i in range(0,24)])

df['hrmn']=hrmn.values

df.to_csv("../step3/time_encoding.csv")