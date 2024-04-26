from collections import deque

# Define a simple graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}

# Breadth-First Search Function
def bfs(graph, start, goal):
    # Queue to manage the nodes to visit (FIFO)
    queue = deque([(start, [start])])
    # Set to keep track of visited nodes
    visited = set()

    while queue:
        # Get the next node to visit from the queue
        current, path = queue.popleft()  # dequeue from the front of the queue

        if current in visited:
            continue

        # Mark the current node as visited
        visited.add(current)

        # If we've reached the goal, return the path
        if current == goal:
            return path

        # Enqueue all unvisited neighbors
        for neighbor in graph[current]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # If the loop completes without finding the goal, return None or an indication of failure
    return None


# Example usage
start_node = 'A'
goal_node = 'E'
path = bfs(graph, start_node, goal_node)

print("BFS Path:", path)
