from math import sqrt

def heuristic_distance(origin, destination):
    x_distance = origin[0] - destination[0]
    y_distance = origin[1] - destination[1]
    return sqrt(x_distance ** 2 + y_distance ** 2)

def shortest_path(M,start,goal):
    g_scores = {}  # Cost from start to each position
    f_scores = {}  # Estimated total cost from start to goal through this position

    g_scores[start] = 0
    f_scores[start] = heuristic_distance(M.intersections[start], M.intersections[goal])

    closed_set = set() # Positions already evaluated
    open_set = set([start]) # Positions to be evaluated
    came_from = {} # Parent position of each position

    while open_set:
        # Get the position in open_set with the lowest f_score
        current = min(open_set, key=lambda node: f_scores[node])

        # If the current position is the goal, return the path
        if current == goal:
            path = [current]
            while current in came_from:
                current = came_from[current]
                path.append(current)
            path.reverse()
            return path
        
        open_set.remove(current)
        closed_set.add(current)

        for neighbor in M.roads[current]:
            # Ignore neighbors already evaluated
            if neighbor in closed_set:
                continue

            # Calculate the distance from start to neighbor through current
            tentative_g = g_scores[current] + heuristic_distance(M.intersections[current], M.intersections[neighbor])

            if neighbor not in open_set or tentative_g < g_scores[neighbor]:
                came_from[neighbor] = current
                g_scores[neighbor] = tentative_g
                h_score = heuristic_distance(M.intersections[neighbor], M.intersections[goal])
                f_scores[neighbor] = g_scores[neighbor] + h_score
                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None  # No valid path found