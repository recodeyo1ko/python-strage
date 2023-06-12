import matplotlib.pyplot as plt

# 直線を描画
def draw_line():
    x = [1, 2, 3, 4, 5]  # x座標
    y = [2, 4, 6, 8, 10]  # y座標

    fig, ax = plt.subplots()
    ax.plot(x, y)  # 直線を描画

    ax.spines['right'].set_visible(False)  # 右側の枠線を非表示
    ax.spines['top'].set_visible(False)  # 上側の枠線を非表示
    ax.spines['left'].set_visible(False)  # 左側の枠線を非表示
    ax.spines['bottom'].set_visible(False)  # 下側の枠線を非表示

    ax.set_xticks([])  # x軸の目盛りを非表示
    ax.set_yticks([])  # y軸の目盛りを非表示

    # plt.xlabel('X-axis')  # x軸のラベル（コメントアウトまたは削除）

    #plt.title('Line Graph')  # グラフのタイトル
    plt.show()  # グラフを表示

# 円を描画
def draw_circle():
    circle = plt.Circle((0.5, 0.5), 0.2, color='blue')  # 中心座標(0.5, 0.5)、半径0.2の円を作成

    fig, ax = plt.subplots()
    ax.add_patch(circle)  # 円を描画

    ax.spines['right'].set_visible(False)  # 右側の枠線を非表示
    ax.spines['top'].set_visible(False)  # 上側の枠線を非表示
    ax.spines['left'].set_visible(False)  # 左側の枠線を非表示
    ax.spines['bottom'].set_visible(False)  # 下側の枠線を非表示

    ax.set_xticks([])  # x軸の目盛りを非表示
    ax.set_yticks([])  # y軸の目盛りを非表示

    plt.xlim(0, 1)  # x軸の範囲を指定
    plt.ylim(0, 1)  # y軸の範囲を指定
    plt.axis('equal')  # x軸とy軸のスケールを等しくする

    # plt.xlabel('X-axis')  # x軸のラベル（コメントアウトまたは削除）

    #plt.title('Circle')  # グラフのタイトル
    plt.show()  # グラフを表示

# 直線を描画する関数を呼び出す
draw_line()

# 円を描画する関数を呼び出す
draw_circle()
