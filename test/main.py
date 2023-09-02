import os
import pandas as pd

datasets = 'datasets'

def all_files(folder):
    files = []
    for i,_,k in os.walk(folder):
        if len(k) != 0:
            for l in k:
                files.append(os.path.join(i, l))
    return files

files = all_files(datasets)

lengths = []
dfs = {}
for f in files:
    df = pd.read_csv(f)
    dfs[f] = df
    length = len(df)
    lengths.append(length)
    print(f'{os.path.basename(f)}: {length} rows')

print('5 members')
print(f'Rows per person: {sum(lengths)/5}')
print(dfs)