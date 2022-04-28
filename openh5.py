import numpy as np
import h5py
filename = 'output/dvs.h5'

with h5py.File(filename, "r") as f:
    print(f.keys())
    print(f["events"][()])
    x = f["events"][()]
with open('test.txt', 'w') as f:
    for i in x:

        f.writelines(str(i[0])) 