import hashlib
import requests
import time
from datetime import datetime, date
import random, string
def random_no(x):
	z = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(x))
	return z
def webhook(device_data):
	url = "https://t.appsflyer.com/api/v4/androidevent"
	headers = {
		'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; A37fw Build/'+device_data['build']+')',
		'Content-Type': 'application/json',
		'Connection': 'Keep-Alive',
		'Host': 't.appsflyer.com'
		}
	PARAMS = {
		'buildnumber': '3.7',
		'app_id': 'kr.co.company.hwahae'
		}

	data = {
		'deviceFingerPrintId': 'ffffffff-'+random_no(4)+'-'+random_no(4)+'-'+random_no(4)+'-'+random_no(12),
		'uid':str(int(time.time()*1000))+'-'+str(''.join(random.choice(string.digits) for _ in range(16))),
		'appsflyerKey':'vyrpAMjHsud67YVPR5ZK4S',
		'model': device_data['model'],
		'advertiserId': device_data['adid'],
		'advertiserIdEnabled': 'true',
		'af_events_api': '1',
		'af_preinstalled': 'false',
		'af_timestamp':str(int(time.time()*1000)),
		'app_version_code':'120',
		'app_version_name':'3.11.2',
		'brand': device_data['brand'],
		'carrier': device_data['carrier'],
		'counter': '2',
		'country': device_data['locale']['country'],
		'date1': str(str(date.today())+'_'+time.strftime('%H%M')+'+'+'0530'),
		'date2': str(str(date.today())+'_'+time.strftime('%H%M')+'+'+'0530'),
		'device': device_data['device'],
		'deviceType': device_data['device_type'],
		'dkh': 'vyrpAMjH',
		'firstLaunchDate': str(str(date.today())+'_'+time.strftime('%H%M')+'+'+'0530'),
		'iaecounter':'0',
		'installDate':str(str(date.today())+'_'+time.strftime('%H%M')+'+'+'0530'),
		'installer_package':'com.android.vending',
		'isFirstCall':'false',
		'isGaidWithGps':'true',
		'lang':'English',
		'lang_code' :'en',
		'network': device_data['network'],
		'operator' :'',
		'platformextension':'android_native',
		'product' :device_data['product'],
		'referrer':'utm_source=(not%20set)&utm_medium=(not%20set)',
		'sdk':device_data['sdk'],
		'timepassedsincelastlaunch':'23',
		}
	str2 = data.get("appsflyerKey")
	str3 = data.get("af_timestamp")
	str1 = data.get("uid")
	v = (str2[0:7] + str1[0:7] + str3[-7:])
	v1 = hashlib.sha1(v.encode())
	data['af_v'] = v1.hexdigest()
	response = requests.post(url=url, params=PARAMS, headers=headers, json=data, verify=False)
	print(response.status_code)
	# extracting response text
	pastebin_url = response.text
	print("The pastebin URL is:%s" % pastebin_url)