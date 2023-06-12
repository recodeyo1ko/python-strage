import matplotlib.pyplot as plt

LINES = 20

j = LINES
for i in range(0, LINES + 1, 1):
    plt.plot([i, 0], [0, j])
    j -= 1
      # 左下に表示
    plt.plot([i, 0], [0, j])
    # 左上に表示
    plt.plot([0, i], [i, LINES])
    # 右下に表示
    plt.plot([LINES, j], [j, 0])
    # 右上に表示
    plt.plot([i, LINES], [LINES, j])

plt.show()

