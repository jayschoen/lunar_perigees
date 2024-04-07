import requests
import re

url = "https://aa.usno.navy.mil/calculated/ssconf"
payload = {
  "date":     "2024-04-07",
  "time":     "17:20:36",
  "intv_mag": "1.00",
  "intv_unit": "1",
  "reps":      "1",
  "lat":       "38.89",
  "lon":       "-77.03",
  "label":     "Washington, DC",
  "height":    "0",
  "submit":     "Get Data"
}

# https://aa.usno.navy.mil/calculated/ssconf?date=2024-04-07&time=17:20:36&intv_mag=1.00&intv_unit=1&reps=1&lat=38.89&lon=-77.03&label=Washington, DC&height=0&submit=Get Data

r = requests.get(url, params=payload)

pattern = 'Moon\s+[0-9]\s+[0-9]+.[0-9]+\s+-\s+[0-9]\s+[0-9]+\s+([0-9]+)\s+[0-9]+\s+[0-9]+\s+[E|W]\s+[0-9]+\s+[0-9]+\s+[0-9]+.[0-9]+\s+[0-9]+%'

m = re.search(pattern, r.text)

print(m.group(1))

