# 間違い

N, M = map(int, input().split())
L_list = list(map(int, input().split()))

left = 1
right = sum(L_list)

while left < right:
    mid = (left + right) // 2
    lines = 1
    line_width = 0 
    for word_width in L_list:
        if line_width + word_width <= mid:
            line_width += word_width + 1 
        else:
            lines += 1
            line_width = word_width 
    
    if lines <= M:
        right = mid
    else:
        left = mid + 1

if M ==1:
    left += len(L_list) - 1
print(left)
