from cmath import inf
def floyd_warshall(G):
    n = len(G)
    distance = list(map(lambda i: list(map(lambda j:j, i)), G))
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k]+distance[k][j])
    print_solution(distance)
    
def print_solution(distance):
    n = len(distance)
    for i in range(n):
        for j in range(n):
            if(distance[i][j] == inf):
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")
        
G = [[0, 3, 7, inf],
        [8, 0, 2, inf],
        [5, inf, 0, 1],
        [2, inf, inf, 0]]
floyd_warshall(G)