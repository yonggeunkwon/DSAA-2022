
def get_maze_answer(maze : dict) -> list:
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
    Returns:
        maze_solution (list) : `maze` 데이터를 바탕으로 최적의 이동 솔루션을 list 타입으로 출력한다.
                                list의 값은 공간 위치에 대한 정보를 포함한다.
    Example:
        >>> solution = get_maze_answer(maze)
        >>> solution
            [(3, 3), (3, 2), (2, 2), (2, 1), (1, 1)]
    """
    miro_finder = []
    temp = []
    start = list(maze.keys())[-1]
    maze_value_list = list(maze[start].values())
    east, west, north, south = maze_value_list
    y, x = start
    miro_finder.append(start)
    while (y, x) != (1, 1):
        if east == 1: # E 가 1인 경우
            x += 1
            temp.append((y, x))
            x -= 1
        if west == 1: # W 가 1인 경우
            x -= 1
            temp.append((y, x))
            x += 1
        if north == 1: # N이 1인 경우
            y -= 1
            temp.append((y, x))
            y += 1
            # a = temp.pop()
            # miro_finder.append(a)
        if south == 1: # S가 1인 경우
            y += 1
            temp.append((y, x))
            y -= 1
        # start = y, x
        print('temp =', temp)
    
    return miro_finder

maze = {(1, 1): {'E': 1, 'W': 0, 'N': 0, 'S': 0}, (2, 1): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, (3, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (4, 1): {'E': 0, 'W': 0, 'N': 1, 'S': 1}, (5, 1): {'E': 1, 'W': 0, 'N': 1, 'S': 0},
        (1, 2): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (2, 2): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (3, 2): {'E': 1, 'W': 0, 'N': 0, 'S': 1}, (4, 2): {'E': 1, 'W': 0, 'N': 1, 'S': 0}, (5, 2): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
        (1, 3): {'E': 1, 'W': 0, 'N': 0, 'S': 0}, (2, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (3, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (4, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (5, 3): {'E': 1, 'W': 1, 'N': 0, 'S': 0},
        (1, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (2, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (3, 4): {'E': 1, 'W': 1, 'N': 0, 'S': 0}, (4, 4): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (5, 4): {'E': 1, 'W': 1, 'N': 1, 'S': 0}, 
        (1, 5): {'E': 0, 'W': 1, 'N': 0, 'S': 1}, (2, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 1}, (3, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 0}, (4, 5): {'E': 0, 'W': 0, 'N': 0, 'S': 1}, (5, 5): {'E': 0, 'W': 1, 'N': 1, 'S': 0}}

print(get_maze_answer(maze))

