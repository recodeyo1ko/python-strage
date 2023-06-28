# モジュールのインポート
import numpy as np
import cv2
import csv
import json
import os
import sys

# 関数定義

def load_row_data(case, movie_number):
    current_dir= os.getcwd()
    current_dir_path = os.path.dirname(current_dir)

    row_mp4_path = os.path.join(current_dir_path, "row_data", case, movie_number, "fullstream.mp4")
    row_json_path = os.path.join(current_dir_path,"row_data", case, movie_number, "livedata.json")
    
    if not os.path.isfile(row_mp4_path) or not os.path.isfile(row_json_path) :
        print('The file does not exist. Prease check path')
        sys.exit()

    return row_mp4_path, row_json_path

def create_trimmed_data(case, movie_number):
    current_dir= os.getcwd()
    current_dir_path = os.path.dirname(current_dir)
    dir_path = os.path.join(current_dir_path, "trimmed_row", case, movie_number)

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    # 処理後の保存先パスを指定
    trimmed_video_mp4file_path = os.path.join(current_dir_path, "trimmed_row", case, movie_number, "fullstream.mp4")
    trimmed_coord_csvfile_path = os.path.join(current_dir_path, "trimmed_row", case, movie_number, "livedata.csv")

    return trimmed_video_mp4file_path, trimmed_coord_csvfile_path

def read_vid(video_path):
    # 動画を読み込む関数
    # 引数：動画のパス
    # 戻値：動画
    
    vid = cv2.VideoCapture(video_path)
    if vid.isOpened()==False:
        print('Error!:The video is not found.')
        return -1
    else:
        return vid
    
def check_start_stop(vid, start, stop):
    # トリミングする始点と終点を確認する関数
    # 引数：動画、動画の始点、動画の終点
    # 戻値：総フレーム数、トリミングされた動画の長さ、動画の始点と終点の秒数と画像
    
    count = vid.get(cv2.CAP_PROP_FRAME_COUNT)
    print('number of video frames = ', count)
    print('trimmed video length:{}sec'.format((stop-start)/25))
    
    start_min = start/25/60
    stop_min = stop/25/60
    
    # 動画の始点と終点の読み込み
    vid.set(cv2.CAP_PROP_POS_FRAMES, start-1)
    ret, start_frame = vid.read()
    vid.set(cv2.CAP_PROP_POS_FRAMES, stop-1)
    ret, stop_frame = vid.read()
    
    # BGR->RGB変換
    start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2RGB)
    stop_frame = cv2.cvtColor(stop_frame, cv2.COLOR_BGR2RGB)

def trim_and_save_vid_as_mp4file(original_vid, trimmed_vid_save_path, start, stop):
    # 動画をstartからstopまでトリミングしてmp4ファイルで保存する関数
    # 引数：元動画、トリミングした動画保存先のパス、動画の始点と終点
    # 戻値：なし
    
    fmt = cv2.VideoWriter_fourcc('m','p','4','v')
    fps = 25
    size = (1920, 1080)
    writer = cv2.VideoWriter(trimmed_vid_save_path, fourcc=fmt, fps=fps, frameSize=size)

    original_vid.set(cv2.CAP_PROP_POS_FRAMES, start-1)
    
    for i in range(start, stop):
        ret, frame = original_vid.read()
        writer.write(frame)
    writer.release()

def read_json(file_path):
    # livedata.jsonから視線座標データ("gp")を取り出しリストにする関数
    # タイムスタンプは使用しないのでコメントアウト
    # 引数：livedata.jsonのファイルパス
    # 戻値：x方向、y方向のそれぞれの視線座標データのリスト（値は0~1）
    
    with open(file_path)as f:
        data = csv.reader(f)
        
        list_data=[]
        coord_x=[]
        coord_y=[]
        #time_stamp=[]
        
        for i in data:
            list_data.append(i)
        
        for j in range(len(list_data)):
            if len(list_data[j])>=6:
                if ("gp" in list_data[j][4]): #and("s:0" in list_data[j][1]):
                    #time_stamp.append(csv_data[j][0].replace('{"ts":',''))
                    coord_x.append(float(list_data[j][4].replace('gp:[','')))
                    coord_y.append(float(list_data[j][5].replace(']}','')))
                    
    return coord_x, coord_y

def coord_50hz_to_25hz(coord_x, coord_y):
    # 視線座標データを50Hzから25Hzへ変換する関数
    # 引数：50Hzの視線座標データのリスト
    # 戻値：25Hzの視線座標データのリスト
    
    coord_x_25hz = []
    coord_y_25hz = []
    
    for i in coord_x[::2]:
        coord_x_25hz.append(i)
    
    for i in coord_y[::2]:
        coord_y_25hz.append(i)
    
    return(coord_x_25hz, coord_y_25hz)

def coord_list_to_ndarray(coord_x, coord_y):
    # x方向、y方向の視線座標リストを1つのndarrayにまとめる関数
    # 引数：x方向の視線座標のリスト、y方向の視線座標のリスト
    # 戻値：視線座標のndarray（[x方向, y方向]）

    union_coord =[]    
    union_coord.append(coord_x)
    union_coord.append(coord_y)

    npcoord = np.array(union_coord)
    npcoord = npcoord.T

    return(npcoord)

def trim_and_save_coord_as_csvfile(original_coord, trimmed_coord_save_path, start, stop):
    # 注視点座標をstartからstopまでトリミングしてcsvファイルで保存する関数
    # 引数：注視点座標(ndarray)、トリミングした注視点座標保存先のパス、トリミングの始点と終点
    # 戻値：なし
    
    trimmed_coord = original_coord[start:stop, :]
    print(trimmed_coord)
    
    with open(trimmed_coord_save_path, 'w')as f:
        print(f)
        np.savetxt(f, trimmed_coord, delimiter=",")


def main():

    # test or train? and what number?
    case = input("test or train ? ")
    movie_number = input("input movie number ")

    # トリミングする始点・終点の指定(s)
    fps = 25
    start_frame = fps * 68
    stop_frame  = fps * 85

    row_mp4_path, row_json_path = load_row_data(case, movie_number)
    trimmed_video_mp4file_path, trimmed_coord_csvfile_path = create_trimmed_data(case, movie_number)
    
    # video処理
    original_video_mp4file = read_vid(row_mp4_path)
    check_start_stop(original_video_mp4file, start_frame, stop_frame)
    trim_and_save_vid_as_mp4file(original_video_mp4file, trimmed_video_mp4file_path, start_frame, stop_frame)

    # coord処理
    original_coordx, original_coordy = read_json(row_json_path)
    original_coordx, original_coordy = coord_50hz_to_25hz(original_coordx, original_coordy)
    original_coord = coord_list_to_ndarray(original_coordx, original_coordy)
    trim_and_save_coord_as_csvfile(original_coord, trimmed_coord_csvfile_path, start_frame, stop_frame)

if __name__ == "__main__":
    main()
