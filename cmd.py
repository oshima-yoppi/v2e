import os 
import glob
from tqdm import tqdm
dir = 'C:/Users/oosim/Desktop/avi/'
avi_data = []
for _, _, files in os.walk(dir):
    for file in files:
        avi_data.append(os.path.join(dir, file))
print(avi_data)
for i, data in enumerate(tqdm(avi_data)):
    print(f'data:{data}')
    data_ = data.split('_')
    print(data_)
    x ,y,z = data_[1], data_[2],data_[3]
    print(x,y,z)
    print(data)
    string = "python v2e.py -i {}  --output_folder=output/ --dvs_text DVS_TEXT{} --dvs_h5 dvs{} --dvs_exposure duration 0.01 --overwrite --timestamp_resolution=0.01 --auto_timestamp_resolution=False --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --output_width=240 --output_height=180  --cutoff_hz=15 --disable_slomo --input_slowmotion_factor 1 --no_preview --truth [{},{},{}]".format(data, str(i),str(i),str(x),str(y),str(z))
    _ = os.system(string)

