# program showing how to read csv from a url using pandas
# author : Andrew Beatty

import pandas as pd

url = # insert url here 

# or a different protocol (you will need to pip instal S3fs)
url + "s3:p//noaa-gsod-pds/2020/72278023183.csv"

df = pd.read_csv(url)
print(df.head)