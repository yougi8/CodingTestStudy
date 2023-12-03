# find 연산
def find(parent, x):
    if parent[x] == x:
        return x
    return find(parent, parent[x])

# union 연산
def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else :
        parent[a] = b

def kruskal(graph, vertices):
    result =[]
    x, e = 0, 0
    graph = sorted(graph, key=lambda item: item[0])
    parent = {station: station for station in vertices}

    while e < len(vertices) -1 :
        w, u, v = graph[x]
        x = x + 1
        a = find(parent, u) # 부모노드 찾기
        b = find(parent ,v) # 부모노드 찾기

        # 부모노드가 같지 않다면, 싸이클 발생하지 않으니까 Union연산으로 트리에 포함
        if a != b:
            e = e + 1
            result.append((w, u, v))
            union(parent, a, b)

    return result

stations = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = [
    (7, 'A', 'B'),
    (15, 'A', 'C'), 
    (8, 'B', 'C'), 
    (9, 'B', 'D'), 
    (8, 'C', 'D'), 
    (11, 'D', 'E'), 
    (6, 'D', 'F'), 
    (8, 'E', 'F'), 
    (4, 'E', 'G'), 
    (7, 'F', 'G')
]

result = kruskal(edges, stations)

for w, u, v in result:
    print((w, u, v))
