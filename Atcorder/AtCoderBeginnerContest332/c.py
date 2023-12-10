def calculate_shirt_needs(N, M, S):
    shirt_muji = M
    shirt_logo = 0
    additional_logo_shirts_needed = 0

    for day in S:
        if day == '0':
            # 予定なし：全てのTを洗濯
            shirt_muji = M
            shirt_logo = additional_logo_shirts_needed
        elif day == '1':
            # 食事の予定：無地Tを使用 or ロゴ入りTを使用
            if shirt_muji > 0:
                shirt_muji -= 1
            else:
                if shirt_logo > 0:
                    shirt_logo -= 1
                else:
                    additional_logo_shirts_needed += 1 
        elif day == '2':
            # 競プロイベント：ロゴ入りTを使用
            if shirt_logo > 0:
                shirt_logo -= 1
            else:
                additional_logo_shirts_needed += 1

    return additional_logo_shirts_needed

N, M = map(int, input().split())
S = input()
print(calculate_shirt_needs(N, M, S))