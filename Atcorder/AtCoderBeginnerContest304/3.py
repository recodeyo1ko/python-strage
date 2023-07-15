import math
from collections import deque


def is_infected(N, D, people):
    # 全員について感染状態を格納するリスト（初めは全員未感染とする）
    infected_status = [False] * N
    infected_status[0] = True  # 最初に感染する人（人1）の感染状態をTrueに

    # 各人について感染状態を更新するためのキュー
    queue = deque([0])

    while queue:
        # 現在の感染者をキューから取り出す
        infected_person = queue.popleft()
        for i in range(N):
            if infected_status[i]:
                # すでに感染していればスキップ
                continue

                # 現在の感染者と未感染者とのユークリッド距離を計算
            distance = math.sqrt(
                (people[infected_person][0] - people[i][0]) ** 2 + (people[infected_person][1] - people[i][1]) ** 2)

            # ユークリッド距離がD以内なら感染していると判断
            if distance <= D:
                infected_status[i] = True
                # 新たに感染した人をキューに追加
                queue.append(i)

    return infected_status


def main():
    n, d = map(int, input().split())
    humans = []
    for i in range(n):
        _x, _y = map(int, input().split())
        humans.append((_x, _y))

    result = is_infected(n, d, humans)

    for i in range(n):
        print('Yes' if result[i] else 'No')


if __name__ == '__main__':
    main()