distances = {
    ('A', 'B'): 3,
    ('B', 'C'): 1,
    ('C', 'D'): 4,
    ('D', 'E'): 1,
    ('E', 'F'): 5,
    ('F', 'G'): 9
}

def calculate_distance(p, q):
    if p == q:
        return 0
    
    distance = distances.get((p, q))
    
    if distance is None:
        intermediate_points = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        p_index = intermediate_points.index(p)
        q_index = intermediate_points.index(q)
        if p_index < q_index:
            distance = 0
            for i in range(p_index, q_index):
                distance += distances[(intermediate_points[i], intermediate_points[i+1])]
        else:
            distance = 0
            for i in range(q_index, p_index):
                distance += distances[(intermediate_points[i], intermediate_points[i+1])]
    
    return distance

p, q = input().split()

distance = calculate_distance(p, q)

print(distance)