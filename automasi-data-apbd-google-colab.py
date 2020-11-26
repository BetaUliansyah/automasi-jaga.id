import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import datetime
from pytz import timezone
import sys
from google.colab import drive
drive.mount('/content/drive')

debug = False
filename = "data-jaga-detail-apbd-"+ datetime.now(timezone('Asia/Jakarta')).strftime("%Y-%m-%d--%H-%M") + ".csv"
path = F"/content/drive/My Drive/Colab Notebooks/Portal APBD/"

# Populate kab_keys 
kab_keys = []
s = requests.Session()
r = s.get('https://jaga.id/api/v5/apbd/list_apbd?limit=1000&offset=12&tahun=2020&type=2&year=2020&category=apbd&keyword=')
if r.status_code==200:
    for row in json.loads(r.text)['data']['result']:
        kab_keys.append(row['kab_key'])
        print(row['kab_key']) if debug else 0 
print(kab_keys) if debug else 0

i = 0
# looping 2020 APBD
for tahun in [2019, 2020]:
    for kab_key in kab_keys:
        print('Populating data ' +str(kab_key) + ' tahun ' + str(tahun))
        r = s.get('https://jaga.id/api/v5/apbd/detail_apbd/'+str(kab_key)+'?tahun='+str(tahun))
        if r.status_code==200:
            print(json.dumps(r.text)['data']['result'][0]) if debug else 0
            result = json.loads(r.text)['data']['result'][0]
            print(result)
            # one time create header
            if i == 0:
                i = i + 1
                header_dict = {'tahun': tahun, **result}
                with open(path+filename, mode='w', newline='') as apbdcsv_file:
                    csv.DictWriter(apbdcsv_file, fieldnames=header_dict, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writeheader()
                print(header_dict)
            
            # writing datas
            data_dict = {'tahun': tahun, **result}
            with open(path+filename, mode='a+', newline='') as apbdcsv_file:
                csv.DictWriter(apbdcsv_file, fieldnames=header_dict, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(data_dict)
            print(data_dict)
