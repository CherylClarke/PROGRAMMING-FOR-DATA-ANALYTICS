import pandas as pd

FILENAME='population.csv'
DATADIR= "../my work/"
FULLPATH= DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

print (df.head(3))

