import random

def generate_grid(N):
    grid = [[random.choice([0, 1]) for _ in range(N)] for _ in range(N)]
    return grid

def get_random_empty_cell(grid, N):
    while True:
        x, y = random.randint(0, N-1), random.randint(0, N-1)
        if grid[x][y] == 1:
            return (x, y)

def dfs(grid, source, goal, N):
    stack = [source]
    parent = {source: None}
    visited = set()
    topological_order = []
    
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        
        visited.add(node)
        topological_order.append(node)
        
        if node == goal:
            break
        
        x, y = node
        neighbors = [(x+dx, y+dy) for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]]
        random.shuffle(neighbors)  # Shuffle to add randomness to DFS
        
        for nx, ny in neighbors:
            if 0 <= nx < N and 0 <= ny < N and grid[nx][ny] == 1 and (nx, ny) not in visited:
                stack.append((nx, ny))
                parent[(nx, ny)] = node
    
    path = []
    if goal in visited:
        node = goal
        while node is not None:
            path.append(node)
            node = parent[node]
        path.reverse()
    
    return path, topological_order

def print_grid(grid, source, goal, path):
    N = len(grid)
    for i in range(N):
        for j in range(N):
            if (i, j) == source:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif (i, j) in path:
                print("*", end=" ")
            else:
                print("1" if grid[i][j] == 1 else "0", end=" ")
        print()

def main():
    N = random.randint(4, 7)
    grid = generate_grid(N)
    source = get_random_empty_cell(grid, N)
    goal = get_random_empty_cell(grid, N)
    
    while source == goal:
        goal = get_random_empty_cell(grid, N)
    
    path, topological_order = dfs(grid, source, goal, N)
    
    print("Generated Grid:")
    print_grid(grid, source, goal, path)
    print("\nSource:", source)
    print("Goal:", goal)
    print("DFS Path:", path if path else "No path found")
    print("Topological Order of Traversal:", topological_order)

if __name__ == "__main__":
    main()
