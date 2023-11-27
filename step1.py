import pandas as pd 

carac = pd.read_csv("data/carac.csv", sep= ";") 
lieux = pd.read_csv("data/lieux.csv", sep= ";")
veh = pd.read_csv("data/veh.csv", sep= ";")
vict = pd.read_csv("data/vict.csv", sep= ";")

data = carac.merge(lieux, how= "inner", on = "Num_Acc")
data = data.merge(veh, how= "inner", on = "Num_Acc")
data = data.merge(vict, how= "inner", on = "Num_Acc") 

data.to_csv( "data.csv", index=False)