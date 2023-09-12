from glob import glob
import pandas as pd

for i in range(5):
    total_cells = 0
    for j in glob(f'../dataset splitup/dataset{i+1}/*'):
        df = pd.read_csv(j)
        total_cells += df.shape[0]*df.shape[1]
    print(f'dataset{i+1}: {total_cells}')