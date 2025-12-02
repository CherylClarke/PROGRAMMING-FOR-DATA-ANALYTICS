# breakdown and referencing in assignment.ipynb file,under assignment 2, this is just the code

# part 1.
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()
#print(data)

#for event in data["northern-ireland"]["events"]:
#    print(f"{event["title"]} on {event['date']}")

# part 2. modified
import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()



ni_events = data["northern-ireland"]["events"]
ew_events = data["england-and-wales"]["events"]
sc_events = data["scotland"]["events"]


ew_titles = {event["title"] for event in ew_events}
sc_titles = {event["title"] for event in sc_events}

print("Bank holidays UNIQUE to Northern Ireland:\n")

for event in ni_events:
    title = event["title"]
    date = event["date"]

    if title not in ew_titles and title not in sc_titles:
        print(f"{title} on {event['date']}")

