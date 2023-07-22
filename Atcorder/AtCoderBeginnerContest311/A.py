def find_first_occurrence(S):
    count = {"A": 0, "B": 0, "C": 0}
    result = 0
    for i in range(len(S)):
        current_char = S[i]
        if current_char in count:
            count[current_char] += 1
        if all(count[char] >= 1 for char in count):
            result = i + 1
            break
    return result

N = int(input())
S = input()


first_occurrence = find_first_occurrence(S)
print(first_occurrence)