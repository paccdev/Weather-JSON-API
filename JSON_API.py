import requests, json, sys

if len(sys.argv) < 2:
    print('Usage: JSON_API.py location')
    sys.exit()
location = ''.join(sys.argv[1:])

url = "http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=07962ccac61bfcb3c775a8f6614e61cb" % (location)

response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

