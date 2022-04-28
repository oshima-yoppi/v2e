import os 
from tqdm import tqdm
for i in tqdm(range(2)):
    string = "python v2e.py -i C:/Users/oosim/Desktop/avi/{}.avi  --output_folder=output/ --dvs_text DVS_TEXT{} --dvs_exposure duration 0.01 --overwrite --timestamp_resolution=0.01 --auto_timestamp_resolution=False --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --output_width=240 --output_height=180  --cutoff_hz=15 --disable_slomo --input_slowmotion_factor 1 --dvs_h5 dvs{}".format(str(i), str(i),str(i))
    # string = "python {}.py".format("a")
    _ = os.system(string)