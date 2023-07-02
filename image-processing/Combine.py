# import modules
import cv2
import os
import numpy as np

def path(case):
    # get current directory path
    current_dir= os.getcwd()
    current_dir_path = os.path.dirname(current_dir)

    # get trimmed_row_dir path
    trimmed_row_path = os.path.join(current_dir_path, "trimmed_row", case)

    # create combined_data path
    combined_data_mp4_path = os.path.join(current_dir_path, "combined_data", case,"fullstream.mp4" )
    combined_data_csv_path = os.path.join(current_dir_path, "combined_data", case, "livedata.csv")

    return trimmed_row_path, combined_data_mp4_path, combined_data_csv_path


def combine_movie(count, trimmed_row_path, combined_data_mp4_path):
    # 入力用の動画キャプチャを準備
    caps = []
    for i in range(count):
        mp4_file_path = os.path.join(trimmed_row_path, str(i + 1) , "fullstream.mp4")
        cap = cv2.VideoCapture(mp4_file_path)
        caps.append(cap)

    # get video info from first video
    fps = caps[0].get(cv2.CAP_PROP_FPS)
    frame_width = int(caps[0].get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(caps[0].get(cv2.CAP_PROP_FRAME_HEIGHT))

    # create combined video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(combined_data_mp4_path, fourcc, fps, (frame_width, frame_height))

    # 動画を順番に読み込んで結合し、出力用の動画に書き込む
    for i , cap in enumerate(caps):
        while True:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break

        print(f"{i+1} / {count} 完了しました。")

    # メモリを解放
    for cap in caps:
        cap.release()
    out.release()



def combine_csv(count, trimmed_row_path, combined_data_csv_path):
    # csv 結合

    # 結合するデータを格納するための空のリストを作成
    merged_data = []

    # CSVファイルを順番に読み込んでデータを結合
    for i in range(1, count+1):
        file_path = os.path.join(trimmed_row_path, str(i), "livedata.csv")
        data = np.loadtxt(file_path, delimiter=",")
        merged_data.append(data)

    # リスト内の配列を結合
    merged_data = np.concatenate(merged_data, axis=0)

    # 結合したデータを新しいCSVファイルに保存
    np.savetxt(combined_data_csv_path, merged_data, delimiter=",")


def main():

    # test or train ? and what number ?
    case = input("test or train ? ")
    count = int(input("データ数: "))

    # get path
    trimmed_row_path, combined_data_mp4_path, combined_data_csv_path = path(case)

    # combine movie
    combine_movie(count, trimmed_row_path, combined_data_mp4_path)

    # combine csv
    combine_csv(count, trimmed_row_path, combined_data_csv_path)


if __name__ == "__main__":
    main()