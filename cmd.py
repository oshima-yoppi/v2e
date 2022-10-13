import os 
import glob
from tqdm import tqdm
# blenderで作成された動画が格納されているディレクトリを指定
dir = 'C:/Users/oosim/Desktop/avi3/'

# blenderで作成された動画のファイルパスのリストを加える
avi_data = []
for _, _, files in os.walk(dir):
    for file in files:
        avi_data.append(os.path.join(dir, file))
print(avi_data)

# 学習& テストデータを作成する。
for i, data in enumerate(tqdm(avi_data)):
    #ファイル名をアンダーバーで区切り、角速度ベクトルの各成分の教師データを代入する
    data_ = data.split('_')
    x ,y,z = data_[2], data_[3],data_[4]

    # コマンドを作成。引数があると思いますが、英語の説明見たらわかると思います。readme.mdに軽く説明記載しています。
    # string = "python v2e.py -i {}  --output_folder=output/ --dvs_text DVS_TEXT{} --dvs_h5 dvs{} --dvs_exposure duration 0.01 --overwrite --timestamp_resolution=0.01 --auto_timestamp_resolution=False --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --output_width=240 --output_height=180  --cutoff_hz=15 --disable_slomo --input_slowmotion_factor 1 --no_preview --truth [{},{},{}]".format(data, str(i),str(i),str(x),str(y),str(z))
    string = "python v2e.py -i {}  --output_folder=output_vector/ --dvs_h5 dvs{} --dvs_exposure duration 0.01 --overwrite --timestamp_resolution=0.01 --auto_timestamp_resolution=False --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --output_width=128 --output_height=128  --cutoff_hz=15 --disable_slomo --input_slowmotion_factor 1 --no_preview --label [{},{},{}] --dvs_aedat2 None --dvs_params clean".format(data, str(i).zfill(5),str(x),str(y),str(z))
    # string = "python v2e.py -i {}  --output_folder=output/ --dvs_h5 dvs{} --dvs_exposure duration 0.01 --overwrite --timestamp_resolution=0.01 --auto_timestamp_resolution=False --pos_thres=.15 --neg_thres=.15 --sigma_thres=0.03 --output_width=128 --output_height=128  --cutoff_hz=15 --disable_slomo --input_slowmotion_factor 1 --no_preview --label [{},{},{}] --dvs_aedat2 None --dvs_params clean".format(data, str(i),str(x),str(y),str(z))
    
    # 作成したコマンドを実行
    _ = os.system(string)

