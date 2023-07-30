S_A = [] 
inputs_S = [] 
inputs_A = [] 

N = int(input())

for _ in range(N):
    input_S_A = input()
    split_input = input_S_A.split()
    S_A.append(split_input)
    inputs_S.append(split_input[0]) 
    inputs_A.append(int(split_input[1])) 

start_index = inputs_A.index(min(inputs_A))

for i in range(N):
    name = inputs_S[(start_index + i) % N]
    print(name)