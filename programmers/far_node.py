# from collections import deque

# def solution(n, edge):

#     adj = [[] for _ in range(n+1)]
#     visit = [0] * (n+1)
#     for a, b in edge:
#         adj[a].append(b)
#         adj[b].append(a)

#     visit[1] = 1
#     q = deque([1])

#     while q:
#         x = q.popleft()
#         for next in adj[x]:
#             if not visit[next]:
#                 visit[next] = visit[x] + 1
#                 q.append(next)

#     max_v = max(visit)
#     cnt = visit.count(max_v)

#     return cnt if cnt > 0 else 1


def solution(n, edge):
    graph =[  [] for _ in range(n + 1) ]
    print(graph)
    # [[], [], [], [], [], [], []]
    distances = [ 0 for _ in range(n) ]
    print(distances)
    # [0, 0, 0, 0, 0, 0]
    is_visit = [False for _ in range(n)]
    print(is_visit)
    # [False, False, False, False, False, False]
    queue = [0]
    is_visit[0] = True
    print(is_visit)
    [True, False, False, False, False, False]
    for (a, b) in edge:
        print((a,b))
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    print(graph)
    # [[2, 1], [2, 0, 3, 4], [5, 3, 1, 0], [2, 1], [1], [2], []]
    while queue:
        i = queue.pop(0)

        for j in graph[i]:
            if is_visit[j] == False:
                is_visit[j] = True
                queue.append(j)
                distances[j] = distances[i] + 1

    distances.sort(reverse=True)
    answer = distances.count(distances[0])

    return answer


##############################

from collections import defaultdict


def bfs(graph, start, distances):
    q = [start]
    visited = set([start])

    while len(q) > 0:
        current = q.pop(0)
        for neighbor in graph[current]:
            if neighbor not in visited:
                print("neighbor = ", neighbor)
                visited.add(neighbor)
                q.append(neighbor)
                distances[neighbor] = distances[current] + 1
                print("distances = ",distances)

                # neighbor =  3
                # distances =  [0, 0, 0, 1, 0, 0, 0]
                # neighbor =  2
                # distances =  [0, 0, 1, 1, 0, 0, 0]
                # neighbor =  6
                # distances =  [0, 0, 1, 1, 0, 0, 2]
                # neighbor =  4
                # distances =  [0, 0, 1, 1, 2, 0, 2]
                # neighbor =  5
                # distances =  [0, 0, 1, 1, 2, 2, 2]

def solution(n, edge):
    # 그래프 만들기
    graph = defaultdict(list)

    for e in edge:
        print(e)
        # [3, 6]
        # [4, 3]
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])
        # defaultdict(<class 'list'>, {3: [6], 6: [3]})
        # defaultdict(<class 'list'>, {3: [6, 4], 6: [3], 4: [3]})

    print(graph)
    # defaultdict(<class 'list'>, {3: [6, 4, 2, 1], 6: [3], 4: [3, 2], 2: [3, 1, 4, 5], 1: [3, 2], 5: [2]})

    # bfs 탐색 (최단 거리를 구해야 하므로.)
    distances = [0]*(n+1)
    bfs(graph, 1, distances)

    max_distance = max(distances)
    answer = 0

    for distance in distances:
        if distance == max_distance:
            answer += 1

    return answer






n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))