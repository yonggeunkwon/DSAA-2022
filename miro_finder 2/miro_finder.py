from collections import deque

def get_maze_answer(maze : dict, end_point=(1,1)) -> list:
    """ 미로에 대한 정보를 dict 타입으로 입력 받아서 해당 미로의 답을 반환한다.
    Args:
        maze (dict) : 미로에 대한 정보를 포함하고 있으며, 해당 정보는 위치 정보와 이동 가능한 방향에 대한 정보를 포함한다.
    Example:
        maze = {(1, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1},
                (2, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
                (3, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (1, 2): {'E': 1, 'W': 0, 'N': 0, 'S': 0},
                (2, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (3, 2): {'E': 1, 'W': 1, 'N': 1, 'S': 0},
                (1, 3): {'E': 0, 'W': 1, 'N': 0, 'S': 1},
                (2, 3): {'E': 0, 'W': 0, 'N': 1, 'S': 1},
                (3, 3): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}
    Returns:            else:
                                check_cross_south = cross[-1]
                            
                            if check_cross_east in visited and check_cross_west in visited and check_cross_north in visited and check_cross_south in visited:
                                cross.pop()
                                continue
                except:
                    pass

            if nx < 0 or nx > start[0] or ny < 0 or ny > start[1]:  # 나가면 안 됨
                continue

            if maze_value_list[i] == 0:  # 벽을 만난 경우
                continue

            if maze_value_list[i] == 1 and (nx, ny) not in visited:  # 방문한 곳을 제외하고 갈 곳이 있는 경우   
                stack.append((nx, ny))
        maze_solution (list) : `maze` 데이터를 바탕으로 최적의 이동 솔루션을 list 타입으로 출력한다.
                                list의 값은 공간 위치에 대한 정보를 포함한다.
    Example:
        >>> solution = get_maze_answer(maze)
        >>> solution
            [(3, 3), (3, 2), (2, 2), (2, 1), (1, 1)]
    """
    miro_finder = []
    visited = []
    start = list(maze.keys())[-1]  # 시작 지점
    miro_finder.append(start)
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    while miro_finder:
        x, y = miro_finder[-1]
        if miro_finder[-1] == end_point:  # 도착했을 때, 방문하지 않은 경로는 삭제
            visited.append(end_point)
            for route in miro_finder:
                if route not in visited:
                    miro_finder.remove(route)
            break
        if miro_finder[-1] not in visited: 
            visited.append((x, y))
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                maze_value_list = list(maze[(x, y)].values())

                if nx < 0 or nx > start[0] or ny < 0 or ny > start[1]:  # 나가면 안 됨
                    continue

                if maze_value_list[i] == 0:  # 벽을 만난 경우
                    continue

                if maze_value_list[i] == 1 and (nx, ny) not in visited:  # 갈 곳이 있음
                    miro_finder.append((nx, ny))
        else:
            miro_finder.pop()
        
    return miro_finder    