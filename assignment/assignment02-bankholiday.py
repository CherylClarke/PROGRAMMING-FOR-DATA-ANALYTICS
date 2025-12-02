# breakdown and referencing in assignment.ipynb file

# part 1.
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
print(data)

for event in data["northern-ireland"]["events"]:
    print(f"{event["title"]} on {event['date']}")

# part 2.

