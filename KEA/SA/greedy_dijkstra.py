import heapq # 우선순위 큐 구현

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph} # 각 노드까리의 거리를 초기화해서(infinity) 저장
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_destination = heapq.heappop(queue)

        # 기존 거리보다 길다면, 비교 x 다른 노드 탐색
        if distances[current_destination] < current_distance:
            continue

        for new_destination, new_distance in graph[current_destination].items():
            distance = current_distance + new_distance

            # 저장되어있는 거리보다 작으면 갱신에서 반영
            if distance < distances[new_destination]:
                distances[new_destination] = distance
                heapq.heappush(queue, [distance, new_destination]) # 큐에 삽입

    return distances

def shortest_path(graph, start, end):
    distances = dijkstra(graph, start) # 그래프 내의 모든 노드에 대한 최단거리 계산
    route = [end] # 최단경로 정보 저장. 역추적
    while end != start:
        for node, distance in graph.items():
            if end in distance:
                if distances[end] == distances[node] + distance[end]:
                    route.append(node)
                    end = node
                    break
    route.reverse() # 역추적된 경로를 다시 원래대로 복귀시킴
    return "->".join(route)

stations = {
    'A': {'B': 3, 'C': 2},
    'B': {'A': 3, 'D': 7, 'E': 8},
    'C': {'A': 2, 'D': 4, 'E': 1},
    'D': {'B': 7, 'C': 4},
    'E': {'B': 8, 'C': 1}
}

print(shortest_path(stations, 'E', 'A'), "\n\"Completed\"")
