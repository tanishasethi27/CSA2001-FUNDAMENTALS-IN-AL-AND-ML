import heapq
from utils.heuristics import manhattan

def expected_cost(p, penalty=5):
    return (1 - p)*1 + p*(1 + penalty)

def astar(grid, traffic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    cost_so_far = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy

            if 0 <= nx < 20 and 0 <= ny < 20 and grid[nx][ny] == 0:
                new_cost = cost_so_far[current] + expected_cost(traffic[nx][ny])

                if (nx, ny) not in cost_so_far or new_cost < cost_so_far[(nx, ny)]:
                    cost_so_far[(nx, ny)] = new_cost
                    priority = new_cost + manhattan((nx, ny), goal)
                    heapq.heappush(open_list, (priority, (nx, ny)))
                    came_from[(nx, ny)] = current

    path = []
    curr = goal
    while curr != start:
        path.append(curr)
        curr = came_from.get(curr, start)
    path.append(start)
    path.reverse()

    return path
