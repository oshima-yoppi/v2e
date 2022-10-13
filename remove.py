import os

path = 'output_vector/dvs'

for i in range(3002, 10000):
    
    path = 'output_vector/dvs'
    n = str(i).zfill(5)
    path = path + n + '.h5'
    os.remove(path)