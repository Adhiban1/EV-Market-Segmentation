import os
import pandas as pd
from zipfile import ZipFile
import random
from time import time

# Extraction dataset.zip
if not os.path.exists('dataset'):
    with ZipFile('dataset.zip', 'r') as f:
        f.extractall()
    print('Unzipped dataset')
else:
    print('Folder "dataset" already exist')

# This will return all the files locations from the given dir
def all_files(folder):
    'This will return all the files locations from the given dir'
    files = []
    for i,_,k in os.walk(folder):
        if len(k) != 0:
            for l in k:
                files.append(os.path.join(i, l))
    return files

files = all_files('dataset')

# change detection
with open('files.csv', 'r') as f:
    pre_files = f.read().split('\n')

if pre_files == files:
    print('No change in files')
    new_files = False
else:
    new_files = True
    print('New files:')
    for i in files:
        if i not in pre_files:
            print(i)

with open('files.csv', 'w') as f:
    f.write('\n'.join(files))

# Details of csv files
def csv_details(files):
    'This gets list or csv file\'s locations \
    and returns them as dfs, and details of rows, columns and cells'
    dfs = {}
    data = []
    for f in files:
        df = pd.read_csv(f)
        name = os.path.basename(f)
        dfs[name] = df
        data.append([name, df.shape[0], df.shape[1], 
                     df.shape[0]*df.shape[1]])
    details = pd.DataFrame(
        data, 
        columns=['filename', 'rows', 'columns', 'cells']
    ).sort_values('cells').reset_index(drop=True)

    no_duplicate_filenames = len(files) == len(dfs)

    return dfs, details, no_duplicate_filenames

dfs, details, no_duplicate_filenames = csv_details(files)
print(details)
print(no_duplicate_filenames)

# dataset splitup to 5 team members
d = {}
for i in details.values:
    d[i[3]] = i[0]

print(f'{details["cells"].sum()/5 = }')
print(f'{(details["cells"].sum()-1914778)/5 = }')

cells = list(details["cells"])

def cells_split():
    while True:
        l = []
        for _ in range(5):
            l.append(random.randint(3, len(cells)//2))
        if sum(l) == len(cells):
            break
    return l

def split_dataset():
    cells = list(details["cells"])
    random.shuffle(cells)
    rearrage = []
    k = 0
    for i in cells_split():
        l = []
        for _ in range(i):
            l.append(cells[k])
            k += 1;
        rearrage.append(l)
    return rearrage

def even_splitup(min_rows):
    start = time()
    while True:
        splitup = split_dataset()
        temp = []
        sum_val = []
        for i in splitup:
            temp.append(min_rows < sum(i))
            sum_val.append(sum(i))
        print(f'\r({round(time()-start)}s) {sum_val = }    ', end='', flush=True)
        if all(temp) or time()-start > 60:
            if time()-start > 60:
                print('[Time out]')
            else:
                print('[Findout]')
            break
    print()

    splitup_name = []
    for i in splitup:
        temp = []
        for j in i:
            temp.append(d[j])
        splitup_name.append(temp)
    return splitup, sum_val, splitup_name

if new_files:
    splitup, sum_val, splitup_name = even_splitup(5000)

    print(f'{splitup = }')
    print(f'{splitup_name = }')

    with open('splitup.txt', 'w') as f:
        f.write(f'{splitup = }\n{splitup_name = }')

# seperate dataset in folders
m = 0
if not os.path.exists('splitup'):
    os.mkdir('splitup')
    for i in splitup_name:
        m += 1
        os.mkdir(f'splitup/member{m}')
        for j in i:
            dfs[j].to_csv(f'splitup/member{m}/{j}', index=False)
elif new_files:
    os.system('rm -rf splitup')
    os.mkdir('splitup')
    for i in splitup_name:
        m += 1
        os.mkdir(f'splitup/member{m}')
        for j in i:
            dfs[j].to_csv(f'splitup/member{m}/{j}', index=False)
    print('"splitup" folder modified')
else:
    print('"splitup" no change')