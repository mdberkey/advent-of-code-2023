
# find loop
# calc dist
# get res

values = []
start = None
with open("input2.txt") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    values = []
    for line in lines:
        value_li = [char for char in line]
        values.append(value_li)
    
    for i in range(len(values)):
        for j in range(len(values[i])):
            if values[i][j] == 'S':
                start = (i, j)
                break

from collections import deque

def longest_path(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    queue = deque([(start, 0)])  # (position, steps)
    longest_path = 0

    while queue:
        print(queue)
        current_position, steps = queue.popleft()
        row, col = current_position

        # Check if the current position is within the grid and not visited
        if 0 <= row < rows and 0 <= col < cols and current_position not in visited:
            visited.add(current_position)

            # Update the longest path
            longest_path = max(longest_path, steps)

            # Explore neighbors
            neighbors = get_neighbors(grid, current_position)
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, steps + 1))

    return longest_path

def get_neighbors(grid, position):
    row, col = position
    curr = grid[row][col]
    pipe_types = {'|', '-', 'L', 'J', '7', 'F'}
    neighbors = []

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_row, new_col = row + dr, col + dc

        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] in pipe_types:
            # Check if the pipe direction allows movement in the current direction
            new_curr = grid[new_row][new_col]
            if curr == '|':
                if dr == -1 and new_curr in ['|', 'L', 'J']:
                    # down
                    neighbors.append((new_row, new_col))
                if dr == 1 and new_curr in ['|', '7', 'F']:
                    # up
                    neighbors.append((new_row, new_col))
            if curr == '-':
                if dc == -1 and new_curr in ['-', 'L', 'F']:
                    # west
                    neighbors.append((new_row, new_col))
                if dc == 1 and new_curr in ['-', 'J', '7']:
                    # east
                    neighbors.append((new_row, new_col))
            if curr == 'L':
                if dr == 1 and new_curr in ['|', '7', 'F']:
                    # up
                    neighbors.append((new_row, new_col))
                if dc == 1 and new_curr in ['-', 'J', '7']:
                    # east
                    neighbors.append((new_row, new_col))
            if curr == 'J':
                if dr == 1 and new_curr in ['|', '7', 'F']:
                    # up
                    neighbors.append((new_row, new_col))
                if dc == -1 and new_curr in ['-', 'L', 'F']:
                    # west
                    neighbors.append((new_row, new_col))
            if curr == '7':
                if dc == -1 and new_curr in ['-', 'L', 'F']:
                    # west
                    neighbors.append((new_row, new_col))
                if dr == -1 and new_curr in ['|', 'L', 'J']:
                    # down
                    neighbors.append((new_row, new_col))
            if curr == 'F':
                if dc == 1 and new_curr in ['-', 'J', '7']:
                    # east
                    neighbors.append((new_row, new_col))
                if dr == -1 and new_curr in ['|', 'L', 'J']:
                    # down
                    neighbors.append((new_row, new_col))
            if curr == 'S':
                if dr == -1 and new_curr in ['|', 'L', 'J']:
                    # down
                    neighbors.append((new_row, new_col))
                if dr == 1 and new_curr in ['|', '7', 'F']:
                    # up
                    neighbors.append((new_row, new_col))
                if dc == -1 and new_curr in ['-', 'L', 'F']:
                    # west
                    neighbors.append((new_row, new_col))
                if dc == 1 and new_curr in ['-', 'J', '7']:
                    # east
                    neighbors.append((new_row, new_col))
    
    
            
    return neighbors

result = longest_path(values, start)
print("Longest Path:", result)
