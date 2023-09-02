import os
import pandas as pd
import shutil
from zipfile import ZipFile

if not os.path.exists('dataset'):
    with ZipFile('dataset.zip', 'r') as f:
        f.extractall()
    print('Unzipped dataset')
else:
    print('Folder "dataset" already exist')

def all_files(folder):
    files = []
    for i,_,k in os.walk(folder):
        if len(k) != 0:
            for l in k:
                files.append(os.path.join(i, l))
    return files

data = [['Electric_Vehicle_Population_Data.csv'], 
        ['IEA-EV-dataEV_salesHistoricalCars.csv'],
        ['RS_Session_257_AU_2368_A.csv', 'RS_Session_256_AU_2673_2.i.csv', 
         'RS_Session_256_AU_2673_1.csv', 'RS_Session_258_AU_429_1.csv'],
        ['EV_India.csv', 'EV_cars_India_2023.csv'],
        ['4-wheeler-EV-cardekho.csv', '2-wheeler-EV-bikewale.csv', 
         '4-wheeler-EV-carwale.csv', 'EV_CARS _INDIA.csv']]

data_count = []
links = []

files = all_files('dataset')

for fs in data:
    link = []
    r, c = 0, 0
    for f in fs:
        for loc in files:
            if f in loc:
                link.append(loc)
                df = pd.read_csv(loc)
                r += df.shape[0]
                c += df.shape[1]
                break
    links.append(link)
    data_count.append([r, c])

for i,j in enumerate(data_count):
    print(f'Member {i+1} | {j[0]} | {j[1]}')

for i in links:
    print(i)

if not os.path.exists('Data Splitup') and not os.path.exists('zipfiles'):
    os.mkdir('Data Splitup')
    os.mkdir('zipfiles')
    for i in range(5):
        zf = ZipFile(f'zipfiles/member{i+1}.zip', 'w')
        os.mkdir(f'Data Splitup/member{i+1}')
        for loc in links[i]:
            shutil.copy(loc, f'Data Splitup/member{i+1}/{os.path.basename(loc)}')
            zf.write(loc, os.path.basename(loc))
        zf.close()
else:
    print('"Data Splitup" or "zipfiles" already exist')

print('Success')