from collections import deque


def bfs(maze, start, goal):
    queue = deque([start])
    came_from = {start: None}

    while queue:
        current = queue.popleft()

        if current == goal:
            break

        x, y = current
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze.grid[0]) and 0 <= new_y < len(maze.grid):
                if maze.grid[new_y][new_x] == 0 and (new_x, new_y) not in came_from:
                    queue.append((new_x, new_y))
                    came_from[(new_x, new_y)] = (x, y)

    path = []
    while goal != start:
        path.append(goal)
        goal = came_from[goal]
    path.reverse()
    return path


def a_star(maze, start, goal):

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = [(heuristic(start, goal), 0, start)]
    came_from = {start: None}
    cost_so_far = {start: 0}

    while open_list:
        _, current_cost, current = open_list.pop(0)

        if current == goal:
            break

        x, y = current
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(maze.grid[0]) and 0 <= new_y < len(maze.grid):
                if maze.grid[new_y][new_x] == 0:
                    new_cost = current_cost + 1
                    next_node = (new_x, new_y)
                    if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                        cost_so_far[next_node] = new_cost
                        priority = new_cost + heuristic(goal, next_node)
                        open_list.append((priority, new_cost, next_node))
                        came_from[next_node] = current

    path = []
    while goal != start:
        path.append(goal)
        goal = came_from[goal]
    path.reverse()
    return path
