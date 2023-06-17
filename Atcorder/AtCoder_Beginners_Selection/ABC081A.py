number = input()
# digits = [int(x) for x in number]
digits = []
for x in number:
    print(x)
    digits.append(int(x))

print(sum(digits))