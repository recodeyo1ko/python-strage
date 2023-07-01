# Si = list(map(int, input().split()))

# is_ascending = all(Si[i] < Si[i+1] and 100 <= Si[i] <= 675 and Si[i] % 25 == 0 for i in range(len(Si) - 1))

# if is_ascending:
#     print("Yes")
# else:
#     print("No")



def check_sequence(sequence):
    if any(sequence[i] > sequence[i+1] for i in range(len(sequence)-1)):
        return "No"

    if any(num < 100 or num > 675 for num in sequence):
        return "No"

    if any(num % 25 != 0 for num in sequence):
        return "No"

    return "Yes"


input_sequence = list(map(int, input().split()))
result = check_sequence(input_sequence)
print(result)
