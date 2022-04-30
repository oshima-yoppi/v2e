from cProfile import label
from tkinter.ttk import LabelFrame
import numpy as np
import h5py
import torch
import re
filename = 'output/dvs0.h5'

with h5py.File(filename, "r") as f:
    print(f.keys())
    print(f["events"][()])
    print(f['truth'][()])
    x = f["events"][()]
    lable = f['truth'][()]
    print(lable)
    lable = lable[1:-1]
    lable = lable.split(',')
    lablex = float(lable[0])
    labley = float(lable[1])
    lablez = float(lable[2])
li = torch.zeros(3, 3)
print(li)
li[1, 0] = lablex
li[1, 1] = labley
li[1, 2] = lablez
print(li.view(-1))

##テキストファイルに書き込み
# with open('test.txt', 'w') as f:
#     for i in x:
#         f.writelines(str(i[0])) 
