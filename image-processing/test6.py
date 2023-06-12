import matplotlib.pyplot as plt
import random

# 原点を(0, 0)に設定
x, y = 0, 0

# 計算したx座標とy座標を格納するリストを生成
X_list = []
Y_list = []

# X_listとY_listに原点の座標を追加しておく
X_list.append(0)
Y_list.append(0)

# 100000回繰り返す
for i in range(100000):
    #1から100までの乱数を発生させる
    s = random.randint(1, 100)
    if s <=1:      # 1%の確率でこれが起きる
        X = 0.0
        Y = 0.16*y

    elif 2 <= s <= 8:      # 7%の確率でこれが起きる
        X = 0.2*x - 0.26*y
        Y = 0.23*x + 0.22*y + 1.6

    elif 9 <= s <= 15:      # 7%の確率でこれが起きる
        X = -0.15*x + 0.28*y
        Y = 0.26*x + 0.24*y + 0.44

    else:      # 85%の確率でこれが起きる
        X = 0.85*x + 0.04*y
        Y = -0.04*x + 0.85*y + 1.6

    X_list.append(X)      # X_listにXの値を追加
    Y_list.append(Y)      # Y_listにYの値を追加
    x = X
    y = Y

plt.scatter(X_list, Y_list, s=0.01, c='green')      # X_listとY_listに入っている値を散布図として描画(サイズは0.01、色は緑)
plt.xlim(-5, 5)      # 散布図のx座標の範囲を設定
plt.ylim(0, 10)      # 散布図のy座標の範囲を設定
plt.show()      # 描画した図を表示