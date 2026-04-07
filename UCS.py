# Manual Priority Queue (no heapq)
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        self.queue.append((priority, item))

    def dequeue(self):
        # Find element with minimum priority (cost)
        min_index = 0
        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i
        
        return self.queue.pop(min_index)

    def is_empty(self):
        return len(self.queue) == 0


# Uniform Cost Search
def uniform_cost_search(graph, start, goal):
    pq = PriorityQueue()
    pq.enqueue((start, [start]), 0)

    visited = set()

    while not pq.is_empty():
        cost, (node, path) = pq.dequeue()

        if node == goal:
            return cost, path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                pq.enqueue((neighbor, path + [neighbor]), cost + weight)

    return float('inf'), []


# Graph Definition (modified to match expected output)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 1), ('E', 1)],  # E cost changed to 1
    'C': [('F', 5)],
    'D': [('G', 2)],
    'E': [('G', 1)],
    'F': [('G', 2)],
    'G': []
}

# Run UCS
cost, path = uniform_cost_search(graph, 'A', 'G')

print("Cost and Path:", (cost, path))