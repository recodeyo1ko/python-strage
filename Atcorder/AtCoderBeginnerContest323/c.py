#わからず

N, M = map(int, input().split())
A_list = list(map(int, input().split()))

S_list = []
for i in range(N):
    S_score = 0
    S = input()
    for j in range(M):
        if S[j] == 'o':
            S_score += A_list[j]

    S_score += (i + 1)
    S_list.append((S, S_score))

for i in range(N):
    top_score = 0
    current_score = S_list[i][1]  # 現在の参加者のスコア
    better_than_others = True

    # 他の参加者と比較
    for j in range(N):
        if i != j:  # 自分自身との比較を避ける
            if S_list[j][1] >= current_score:
                better_than_others = False
                top_score = S_list[j][1]
                break

    if better_than_others:
        print(0)
    else:
        count = 0
        # 他の人のスコアよりも低い場合、あと何問正解すればいいかを計算して出力
        frag = True
        while frag:
            if not A_list:  # A_listが空の場合
                break  # ループを終了する
            max_score = max(A_list)
            m = A_list.index(max_score)

            # S_list[i][m] が 'x' かどうかを確認
            if S_list[i][0][m] == 'x':
                S_list[i] = (S_list[i][0][:m] + 'o' + S_list[i][0][m + 1:], S_list[i][1])
                current_score += A_list[m]
                count += 1  # 問題を解いた回数を増やす

                # top_scoreと比較
                if current_score > top_score:
                    print(count)
                    frag = False
                    break
            else:
                A_list.pop(m)  # 問題を解く必要がないので、A_listから要素を削除
