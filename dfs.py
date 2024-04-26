# Define a simple graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Recursive Depth-First Search
def dfs_recursive(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    # Mark the start node as visited
    visited.add(start)
    # Add the current node to the path
    path.append(start)

    # If the goal node is reached, return the path
    if start == goal:
        return path

    # Recursively visit each neighbor
    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs_recursive(graph, neighbor, goal, path.copy(), visited.copy())
            if result:
                return result

    return None

# Iterative Depth-First Search using a stack
def dfs_iterative(graph, start, goal):
    # Stack to manage the nodes to visit
    stack = [(start, [start])]
    visited = set()

    while stack:
        current, path = stack.pop()  # Pop from the stack
        if current in visited:
            continue

        visited.add(current)

        # If we've reached the goal, return the path
        if current == goal:
            return path

        # Push all unvisited neighbors onto the stack
        for neighbor in graph[current]:
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None


# Example usage
start_node = 'A'
goal_node = 'E'

# Using the recursive approach
path_recursive = dfs_recursive(graph, start_node, goal_node)
print("DFS Recursive Path:", path_recursive)

# Using the iterative approach
path_iterative = dfs_iterative(graph, start_node, goal_node)
print("DFS Iterative Path:", path_iterative)
