# Function to find the minimum key value node from the set of nodes
def minKey(key, mstSet, V):
    # Initialize minimum value
    min_val = float("inf")
    min_index = -1

    for v in range(V):
        if mstSet[v] == False and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index

# Recursive function to find the minimum spanning tree of a graph


def prim(graph, parent, key, mstSet, V, count):
    # Base case: terminate recursion when all vertices are included in MST
    if count == V:
        return

    # Find the minimum key value node from the set of nodes
    u = minKey(key, mstSet, V)

    # Mark the minimum key value node as visited
    mstSet[u] = True

    # Update the parent and key arrays
    for v in range(V):
        if graph[u][v] > 0 and mstSet[v] == False and graph[u][v] < key[v]:
            key[v] = graph[u][v]
            parent[v] = u

    # Recursively call the prim function with updated parent, key, and mstSet arrays
    prim(graph, parent, key, mstSet, V, count + 1)

# Function to print the minimum spanning tree


def printMST(parent, graph, V):
    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])


# Driver code to test the above functions
graph = [[0, 2, 0, 1, 0],
         [2, 0, 3, 8, 5],
         [0, 3, 0, 0, 7],
         [6, 8, 0, 0, 9],
         [0, 5, 7, 9, 0]]

V = len(graph)
parent = [None] * V
key = [float("inf")] * V
mstSet = [False] * V
key[0] = 0
parent[0] = -1

prim(graph, parent, key, mstSet, V, 0)
printMST(parent, graph, V)
