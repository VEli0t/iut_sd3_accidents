import pandas as pd 
import numpy as np 
from sklearn.cluster import KMeans

df = pd.read_csv("time_encoding.csv", sep=",")

# On extrait du tableau la latitude et la longitude

X_lat = df['lat']
X_long = df['long']

# On définit tous nos points à classifier

X_cluster = np.array((list(zip(X_lat, X_long))))

# Kmeans nous donne pour chaque point la catégorie associée

clustering = KMeans(n_clusters=15, random_state=0)
clustering.fit(X_cluster)

# Enfin on ajoute les catégories dans la base d'entraînement

geo = pd.Series(clustering.labels_)
df['geo'] = geo

df.to_csv("../step4/gps_encoding.csv")
