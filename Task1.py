'''
import urllib
class AppURLopener(urllib.FancyURLopener):
    version = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
opener = AppURLopener()
url = "https://api.letgo.com/api/iplookup.json"
html = opener.open(url)
response = html.getcode()
if (response==200):
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html,'html.parser')
    print(soup)
'''   
import requests
url = "https://api.letgo.com/api/iplookup.json"
response = requests.get(url)
data = response.json()
latitude = data['latitude']
longitude = data['longitude']

API = "https://nominatim.openstreetmap.org/reverse"
sent_data = {'lat':latitude,
        'lon' : longitude,
             'format' : 'json'}
response = requests.post(url = API , params =sent_data)
data = response.json()
display_name = data['display_name']
city = data['address']['city']
print("DISPLAY NAME :%s\nCITY:%s\n"%(display_name, city))
