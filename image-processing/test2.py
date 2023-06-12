import numpy as np
import matplotlib.pyplot as plt

def draw_geometric_pattern(num_sides, num_layers):
    center = np.array([0, 0])  # 中心点の座標
    radius = 1.0  # 正多角形の外接円の半径

    angles = np.linspace(0, 2*np.pi, num_sides, endpoint=False)  # 角度の配列

    fig, ax = plt.subplots()
    ax.set_aspect('equal')  # アスペクト比を等しくする

    for layer in range(num_layers):
        r = radius * (layer + 1)  # 外接円の半径を増加させる

        vertices = []  # 頂点座標を格納するリスト

        for angle in angles:
            x = center[0] + r * np.cos(angle)
            y = center[1] + r * np.sin(angle)

            vertices.append([x, y])

        polygon = plt.Polygon(vertices, closed=True, facecolor='none', edgecolor='blue')
        ax.add_patch(polygon)

    ax.set_xlim(-radius*num_layers, radius*num_layers)
    ax.set_ylim(-radius*num_layers, radius*num_layers)

    ax.set_xticks([])  # x軸の目盛りを非表示
    ax.set_yticks([])  # y軸の目盛りを非表示

    # plt.title('Geometric Pattern')
    plt.show()

# 正六角形を2層重ねて描画
draw_geometric_pattern(num_sides=6, num_layers=2)
