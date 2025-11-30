import pandas as pd

FILENAME='population.csv'
DATADIR= "../my work/"
FULLPATH= DATADIR + FILENAME

df = pd.read_csv(FULLPATH)


drop_col_list = ["Statistic Label","CensusYear","Sex","UNIT"]

# can be done like this-
# df =df.drop(columns=drop_col_list)
# or like this-
df.drop(columns=drop_col_list, inplace=True)

# to change from all ages to single year of age

df = df[df["Single Year of Age"] != "All ages"]

# changing the column, replace under 1 with 0
df["Single Year of Age"] = df["Single Year of Age"].str.replace("Under 1 year",'0')



print (df.head(3))

