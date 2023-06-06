class State:
    def __init__(self, jug1, jug2, cost):
        self.jug1 = jug1
        self.jug2 = jug2
        self.cost = cost

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def __hash__(self):
        return hash((self.jug1, self.jug2))

def bfs(start, goal, max1, max2):
    queue = [(start, [start])]
    visited = set()
    while queue:
        (node, path) = queue.pop(0)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)
        jug1, jug2 = node.jug1, node.jug2
        cost = node.cost
        # pour jug1 into jug2
        if jug1 + jug2 <= max2:
            queue.append((State(0, jug1 + jug2, cost + jug1), path + [State(0, jug1 + jug2, cost + jug1)]))
        else:
            queue.append((State(jug1 - (max2 - jug2), max2, cost + max2 - jug2), path + [State(jug1 - (max2 - jug2), max2, cost + max2 - jug2)]))
        # pour jug2 into jug1
        if jug1 + jug2 <= max1:
            queue.append((State(jug1 + jug2, 0, cost + jug2), path + [State(jug1 + jug2, 0, cost + jug2)]))
        else:
            queue.append((State(max1, jug2 - (max1 - jug1), cost + max1 - jug1), path + [State(max1, jug2 - (max1 - jug1), cost + max1 - jug1)]))
        # fill jug1
        queue.append((State(max1, jug2, cost + max1 - jug1), path + [State(max1, jug2, cost + max1 - jug1)]))
        # fill jug2
        queue.append((State(jug1, max2, cost + max2 - jug2), path + [State(jug1, max2, cost + max2 - jug2)]))
        # empty jug1
        queue.append((State(0, jug2, cost + jug1), path + [State(0, jug2, cost + jug1)]))
        # empty jug2
        queue.append((State(jug1, 0, cost + jug2), path + [State(jug1, 0, cost + jug2)]))
    return None

start = State(0, 0, 0)
goal = State(5, 0, 0)
max1, max2 = 7, 3
result = bfs(start, goal, max1, max2)
if result:
    for i in result:
        print(f"{i.jug1} {i.jug2} {i.cost}")
else:
    print("No solution found")
