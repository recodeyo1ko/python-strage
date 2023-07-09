def is_palindrome(s):
    return s == s[::-1]

def check_palindrome_combination(strings):
    for i in range(len(strings)):
        for j in range(i+1, len(strings)):
            concat = strings[i] + strings[j]
            if is_palindrome(concat):
                return "Yes"
    return "No"

N = int(input())
strings = []
for _ in range(N):
    s = input()
    strings.append(s)

print(check_palindrome_combination(strings))
