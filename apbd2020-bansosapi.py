import requests
import json
import csv
from google.colab import drive
from datetime import datetime
from pytz import timezone
import sys

drive.mount('/content/drive')
path = F"/content/drive/My Drive/Colab Notebooks/Jaga.id APBD/"
filename = F"data-jaga-bansos-apbd-"+ datetime.now(timezone('Asia/Jakarta')).strftime("%Y-%m-%d--%H-%M") + ".csv"

#kab_keys = ['1172', '1174', '1173', '1113', '1112', '1114', '1115', '1116', '1117', '1118', '1175', '1209', '1211', '1207', '1206', '1210', '1205', '1213', '1204', '1208', '1203', '1201', '1202', '1212', '1275', '1271', '1272', '1273', '1274', '1276', '1277', '1215', '1214', '1216', '1218', '1217', '1219', '1221', '1220', '1222', '1223', '1224', '1225', '1278', '1307', '1306', '1309', '1305', '1308', '1301', '1303', '1302', '1304', '1375', '1374', '1371', '1376', '1373', '1372', '1377', '1312', '1310', '1311', '1403', '1404', '1402', '1401', '1409', '1405', '1407', '1406', '1408', '1472', '1471', '1410', '1504', '1508', '1501', '1502', '1505', '1503', '1506', '1507', '1509', '1571', '1572', '1604', '1606', '1605', '1603', '1602', '1601', '1671', '1674', '1672', '1673', '1607', '1610', '1608', '1609', '1611', '1612', '1613', '1701', '1703', '1702', '1771', '1704', '1705', '1706', '1707', '1708', '1709', '1804', '1801', '1802', '1803', '1807', '1806', '1805', '1808', '1871', '1872', '1809', '1810', '1811', '1812', '1813', '3204', '3216', '3201', '3207', '3203', '3209', '3205', '3212', '3215', '3208', '3210', '3214', '3213', '3202', '3211', '3206', '3273', '3275', '3271', '3274', '3276', '3272', '3278', '3277', '3279', '3217', '3218', '3304', '3302', '3325', '3316', '3309', '3329', '3301', '3321', '3315', '3320', '3313', '3305', '3324', '3310', '3319', '3308', '3318', '3326', '3327', '3303', '3306', '3317', '3322', '3314', '3311', '3328', '3323', '3312', '3307', '3371', '3375', '3373', '3374', '3372', '3376', '3402', '3403', '3401', '3404', '3471', '3526', '3510', '3505', '3522', '3511', '3525', '3509', '3517', '3506', '3524', '3508', '3519', '3520', '3507', '3516', '3518', '3521', '3501', '3528', '3514', '3502', '3513', '3527', '3515', '3512', '3529', '3503', '3523', '3504', '3572', '3571', '3577', '3573', '3576', '3575', '3574', '3578', '3579', '6107', '6108', '6106', '6104', '6102', '6101', '6103', '6105', '6171', '6172', '6109', '6110', '6111', '6112', '6204', '6205', '6203', '6201', '6202', '6271', '6206', '6207', '6208', '6209', '6210', '6211', '6212', '6213', '6303', '6304', '6306', '6307', '6308', '6302', '6309', '6301', '6305', '6372', '6371', '6311', '6310', '6403', '6402', '6407', '6408', '6401', '6471', '6474', '6472', '6409', '6411', '7101', '7102', '7103', '7172', '7171', '7104', '7105', '7173', '7106', '7109', '7174', '7108', '7107', '7110', '7111', '7201', '7207', '7205', '7204', '7203', '7206', '7202', '7271', '7208', '7209', '7210', '7211', '7212', '7303', '7311', '7308', '7302', '7316', '7306', '7304', '7317', '7322', '7309', '7310', '7373', '7324', '7315', '7307', '7301', '7314', '7312', '7305', '7318', '7313', '7372', '7371', '7326', '7404', '7402', '7401', '7403', '7471', '7472', '7405', '7406', '7407', '7408', '7409', '7410', '7412', '7411', '7413', '7414', '7415', '5103', '5106', '5108', '5104', '5101', '5107', '5105', '5102', '5171', '5206', '5205', '5201', '5202', '5203', '5204', '5271', '5272', '5207', '5208', '5305', '5304', '5308', '5306', '5301', '5313', '5310', '5309', '5307', '5312', '5311', '5302', '5303', '5371', '5314', '5315', '5316', '5318', '5317', '5319', '5320', '5321', '8103', '8101', '8102', '8104', '8171', '8106', '8105', '8107', '8172', '8108', '8109', '9106', '9103', '9102', '9101', '9109', '9104', '9108', '9107', '9105', '9171', '9110', '9111', '9113', '9112', '9114', '9116', '9117', '9118', '9115', '9119', '9120', '9121', '9122', '9123', '9124', '9126', '9125', '9127', '9128', '8202', '8271', '8201', '8206', '8204', '8203', '8205', '8272', '8207', '8208', '3602', '3601', '3604', '3603', '3672', '3671', '3673', '3674', '1901', '1902', '1971', '1903', '1904', '1905', '1906', '7502', '7501', '7571', '7504', '7503', '7505', '2103', '2105', '2102', '2171', '2172', '2104', '2101', '9203', '9202', '9201', '9271', '9205', '9204', '9206', '9207', '9208', '9210', '9209', '9211', '9212', '7605', '7602', '7604', '7603', '7601', '7606', '6501', '6502', '6503', '6571', '6504']
debug = 1
s = requests.Session()

# login
r = s.post('https://jaga.id/api/v5/auth/login', 
           json={'username': "beta.uliansyah@pknstan.ac.id", 
                 'password': "Bismillah123"})
if r.status_code==200:
    print(r.text) if debug else 0
    token_bearer = json.loads(r.text)['data']['token']
    print(token_bearer)
else:
    print(r.status_code)
    print(r.text)
    print(r.url)

kab_keys = ['1172', '1174', '1173', '1113', '1112', '1114', '1115', '1116', '1117', '1118', '1175', '1209', '1211', '1207', '1206', '1210', '1205', '1213', '1204', '1208', '1203', '1201', '1202', '1212', '1275', '1271', '1272', '1273', '1274', '1276', '1277', '1215', '1214', '1216', '1218', '1217', '1219', '1221', '1220', '1222', '1223', '1224', '1225', '1278', '1307', '1306', '1309', '1305', '1308', '1301', '1303', '1302', '1304', '1375', '1374', '1371', '1376', '1373', '1372', '1377', '1312', '1310', '1311', '1403', '1404', '1402', '1401', '1409', '1405', '1407', '1406', '1408', '1472', '1471', '1410', '1504', '1508', '1501', '1502', '1505', '1503', '1506', '1507', '1509', '1571', '1572', '1604', '1606', '1605', '1603', '1602', '1601', '1671', '1674', '1672', '1673', '1607', '1610', '1608', '1609', '1611', '1612', '1613', '1701', '1703', '1702', '1771', '1704', '1705', '1706', '1707', '1708', '1709', '1804', '1801', '1802', '1803', '1807', '1806', '1805', '1808', '1871', '1872', '1809', '1810', '1811', '1812', '1813', '3204', '3216', '3201', '3207', '3203', '3209', '3205', '3212', '3215', '3208', '3210', '3214', '3213', '3202', '3211', '3206', '3273', '3275', '3271', '3274', '3276', '3272', '3278', '3277', '3279', '3217', '3218', '3304', '3302', '3325', '3316', '3309', '3329', '3301', '3321', '3315', '3320', '3313', '3305', '3324', '3310', '3319', '3308', '3318', '3326', '3327', '3303', '3306', '3317', '3322', '3314', '3311', '3328', '3323', '3312', '3307', '3371', '3375', '3373', '3374', '3372', '3376', '3402', '3403', '3401', '3404', '3471', '3526', '3510', '3505', '3522', '3511', '3525', '3509', '3517', '3506', '3524', '3508', '3519', '3520', '3507', '3516', '3518', '3521', '3501', '3528', '3514', '3502', '3513', '3527', '3515', '3512', '3529', '3503', '3523', '3504', '3572', '3571', '3577', '3573', '3576', '3575', '3574', '3578', '3579', '6107', '6108', '6106', '6104', '6102', '6101', '6103', '6105', '6171', '6172', '6109', '6110', '6111', '6112', '6204', '6205', '6203', '6201', '6202', '6271', '6206', '6207', '6208', '6209', '6210', '6211', '6212', '6213', '6303', '6304', '6306', '6307', '6308', '6302', '6309', '6301', '6305', '6372', '6371', '6311', '6310', '6403', '6402', '6407', '6408', '6401', '6471', '6474', '6472', '6409', '6411', '7101', '7102', '7103', '7172', '7171', '7104', '7105', '7173', '7106', '7109', '7174', '7108', '7107', '7110', '7111', '7201', '7207', '7205', '7204', '7203', '7206', '7202', '7271', '7208', '7209', '7210', '7211', '7212', '7303', '7311', '7308', '7302', '7316', '7306', '7304', '7317', '7322', '7309', '7310', '7373', '7324', '7315', '7307', '7301', '7314', '7312', '7305', '7318', '7313', '7372', '7371', '7326', '7404', '7402', '7401', '7403', '7471', '7472', '7405', '7406', '7407', '7408', '7409', '7410', '7412', '7411', '7413', '7414', '7415', '5103', '5106', '5108', '5104', '5101', '5107', '5105', '5102', '5171', '5206', '5205', '5201', '5202', '5203', '5204', '5271', '5272', '5207', '5208', '5305', '5304', '5308', '5306', '5301', '5313', '5310', '5309', '5307', '5312', '5311', '5302', '5303', '5371', '5314', '5315', '5316', '5318', '5317', '5319', '5320', '5321', '8103', '8101', '8102', '8104', '8171', '8106', '8105', '8107', '8172', '8108', '8109', '9106', '9103', '9102', '9101', '9109', '9104', '9108', '9107', '9105', '9171', '9110', '9111', '9113', '9112', '9114', '9116', '9117', '9118', '9115', '9119', '9120', '9121', '9122', '9123', '9124', '9126', '9125', '9127', '9128', '8202', '8271', '8201', '8206', '8204', '8203', '8205', '8272', '8207', '8208', '3602', '3601', '3604', '3603', '3672', '3671', '3673', '3674', '1901', '1902', '1971', '1903', '1904', '1905', '1906', '7502', '7501', '7571', '7504', '7503', '7505', '2103', '2105', '2102', '2171', '2172', '2104', '2101', '9203', '9202', '9201', '9271', '9205', '9204', '9206', '9207', '9208', '9210', '9209', '9211', '9212', '7605', '7602', '7604', '7603', '7601', '7606', '6501', '6502', '6503', '6571', '6504']
debug = 0
s = requests.Session()
i = 0
for kab_key in kab_keys:
    r = s.get('https://jaga.id/api/v5/bansos/detail_apbd?id_provinsi='+str(kab_key[:2])+'&id_kota_kabupaten='+str(kab_key[-2:]), 
              headers = {'Authorization': 'Bearer ' + token_bearer})

    if r.status_code==200:
        print(r.text) if debug else 0
        print(json.loads(r.text)['data']['result'][0]) if debug else 0
        result = json.loads(r.text)['data']['result'][0]
        
        # writing headers
        if i == 0:
            i = i + 1
            with open(path+filename, mode='w', newline='') as apbdcsv_file:
                csv.DictWriter(apbdcsv_file, fieldnames=result, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writeheader()
        #print(header_dict)
    
        # writing datas
        #data_dict = {'tahun': tahun, **result}
        with open(path+filename, mode='a+', newline='') as apbdcsv_file:
            csv.DictWriter(apbdcsv_file, fieldnames=result, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL).writerow(result)
    else:
        print(r.status_code)
        print(r.text)
        print(r.url)    
