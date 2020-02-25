import os,time

import sample_script_appsflyer_call as i

if True:
	os.environ['http_proxy'] = "http://127.0.0.1:8888"
	os.environ['https_proxy'] = "http://127.0.0.1:8888"


device_data={ "User-Agent": "Mozilla/5.0 (Linux; Android 5.1; en-us; A5 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750 Mobile Safari/537.36",
  "adid": "e992cc8a-e393-45d2-bff9-78ff898a659b",
  "android_id": "fb71733466072fd3",
  "bluetooth": "3.0",
  "brand": "Android",
  "build": "LMY47I",
  "carrier": "T-Mobile",
  "country": "Usa",
  "cpu": "armeabi",
  "cpu_core": "4",
  "device": "gxq6580_weg_l",
  "device_type": "mobile",
  "dpi": "320",
  "fingerprint": "alps/full_gxq6580_weg_l/gxq6580_weg_l:5.1/LMY47I/1461734077:user/test-keysHARDWARE: mt6580ID: LMY47ITAGS: release-keysuser/release-keys",
  "gpu": { "name": "Mali-400 MP",
      "vendor": "ARM",
      "version": "OpenGL ES-CM 1.1"
    },
  "hardware": "MT6580Revision",
  "imei": "911596309716707",
  "internal_memory": { "available": "7.125",
      "shown": "8"
    },
  "kernel": "3.10.72+ ",
  "local_timezone": "Mountain Time Zone",
  "local_tz": "MST",
  "local_tz_name": "America/Phoenix",
  "locale": {"country": "US",
      "language": "en"
    },
  "mac": "3e:38:34:ab:0c:04",
  "mainboard": "unknown",
  "manufacturer": "Android",
  "mcc": "310",
  "mnc": "026",
  "model": "A5",
  "network": "WiFi",
  "os_codename": "REL",
  "os_incremental": "1461734077ro.custom.build.version",
  "os_version": "5.1",
  "private_ip": "192.168.153.239",
  "processor": "ARMv7 Processor rev 3 (v7l)",
  "product": "gxq6580_weg_l",
  "ram": { "available": "473",
      "shown": "512"
    },
  "resolution": "1280x720",
  "sdk": "22",
  "serial": "a9c89299e13a58ad",
  "timezone": "-0700"
}	
print(i)
i.webhook(device_data)
