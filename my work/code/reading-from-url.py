# a program to demonstrate getting data from the web using the request objects
# author : Andrew Beatty

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)
# we can now analyze the data
#for events in data["northern-ireland"]["events"]:
#       print(f"{event}")
#      print(f"{event['title']} on {event['date']}")