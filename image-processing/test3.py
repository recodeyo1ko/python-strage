import matplotlib.pyplot as plt
import numpy as np

def create_pattern():
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_aspect('equal')

    # パラメータの設定
    n = 100  # パターンの点の数
    radius = 1.5  # 円の半径

    # パターンの座標を計算
    theta = np.linspace(0, 2 * np.pi, n, endpoint=False)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)

    # 点を描画
    ax.scatter(x, y, color='red', s=30)

    # 線を描画
    for i in range(n):
        ax.plot([0, x[i]], [0, y[i]], color='blue', linewidth=0.5)

    # グラフの設定
    ax.set_xlim(-radius, radius)
    ax.set_ylim(-radius, radius)
    ax.axis('off')

    # グラフを表示
    plt.show()

# パターンの作成と表示
create_pattern()
