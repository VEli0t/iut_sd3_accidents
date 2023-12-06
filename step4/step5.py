import pandas as pd 

df = pd.read_csv("gps_encoding.csv", sep=",")

y = df['grav']

features = ['catu','sexe','trajet','secu',
            'catv','an_nais','mois',
            'occutc','obs','obsm','choc','manv',
            'lum','agg','int','atm','col','gps',
            'catr','circ','vosp','prof','plan',
            'surf','infra','situ','hrmn','geo']

X_train_data = pd.get_dummies(df[features].astype(str))

X_train_data.to_csv("../step5/train.csv")

