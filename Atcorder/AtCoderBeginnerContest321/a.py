def check_digit_order(num):
    num_str = str(num)
    
    if len(num_str) < 2:
        return "Yes" 
    
    for i in range(1, len(num_str)):
        if int(num_str[i]) >= int(num_str[i-1]):
            return "No"
    
    return "Yes"

N =int(input())
result = check_digit_order(N)
print(result)
