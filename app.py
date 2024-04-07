import requests
import re
from datetime import datetime

url = "https://aa.usno.navy.mil/calculated/positions/geocentric"
payload = {
  "ID": "AA",
  "task": "5",
  "body": "11",
  "date": "2024-04-07", # use now()
  "time": "18:55:41",
  "intv_mag": "1.00",
  "intv_unit": "1",
  "reps": "365", # number of iterations
  "submit": "Get Data"
}

# https://aa.usno.navy.mil/calculated/positions/geocentric
#?ID=AA&task=5&body=11&date=2024-04-07&time=18:55:41&intv_mag=1.00&intv_unit=1&reps=365&submit=Get Data
r = requests.get(url, params=payload)

print(r.text)

pattern = '^(\d{4}\s[A-Za-z]{3}\s[0-9]{2}).*?(\d+\.\d{3})$'

results = re.findall(pattern, r.text, flags=re.MULTILINE)

#print(m)
#print(m.group(1))

grouped = {}
for result in results:
  #print(result)

  date = datetime.strptime(result[0], '%Y %b %d')
  day = date.day
  month = date.month
  year = date.year
  # print(month)
  # print(year)
  # break
  if year not in grouped:
    grouped[year] = {}

  if month not in grouped[year]:
    grouped[year][month] = {}

  grouped[year][month][day] = float(result[1])

data = grouped[2024][4]
print(data)
#data = {key: value for key, value in data.items()}
print(data.values())
smallest = min(data.values())
print(smallest)

# #if smallest in data:
# print(list(data.values()).index(smallest))
# print(list(data.values())[0])
#   #list(my_dict.values()).index(100)

smallest_day = ''
for key, value in data.items():
  if value == smallest:
    smallest_day = key
    break

print(smallest_day)

#print(grouped)
#print(grouped[2024][4])
  
#^^^convert 0th element of each in result into date object, then group by year/month ... 
#then within each year/month, order by min distance?
