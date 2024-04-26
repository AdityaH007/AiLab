import heapq

# Define a simple graph as an adjacency list
# Graph format: {node: [(neighbor, cost), (neighbor2, cost2), ...]}
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

# Uniform Cost Search Function
def uniform_cost_search(graph, start, goal):
    # Priority queue to determine which node to visit next based on the lowest cost
    # Each item in the queue is a tuple: (cost, current_node, path_so_far)
    priority_queue = []
    heapq.heappush(priority_queue, (0, start, [start]))

    # Set to keep track of visited nodes to prevent cycles
    visited = set()

    while priority_queue:
        # Get the node with the lowest cost from the priority queue
        cost, current, path = heapq.heappop(priority_queue)

        # If this node has been visited, continue to the next iteration
        if current in visited:
            continue

        # Mark the current node as visited
        visited.add(current)

        # If we've reached the goal, return the path and the total cost
        if current == goal:
            return path, cost

        # Add neighbors to the priority queue with their cumulative costs
        for neighbor, edge_cost in graph[current]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbor, path + [neighbor]))

    # If the loop completes without finding the goal, return None or a message indicating failure
    return None, float('inf')

# Example usage
start_node = 'A'
goal_node = 'E'
path, total_cost = uniform_cost_search(graph, start_node, goal_node)

print("Path:", path)
print("Total cost:", total_cost)
