import random
from queue import PriorityQueue

class Graph:
    def __init__ (self, numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[0 for _ in range(self.numVertices)] for _ in range(self.numVertices)]
        self.root = None
        self.edges = []
        self.leaves = []

    # Returns the root / source of the tree
    def GetRoot(self):
        return self.root
    
    # Returns a list of all the leaf nodes
    def GetLeaves(self):
        return self.leaves
        
    # Prints the adjacency matrix
    def Display(self):
        for row in self.adjMatrix:
            print(row)

    # Generates an undirected graph with no cycles
    def GenerateTree(self):
        # Create a list of vertices from [0, numVertices)
        vertices = list(range(self.numVertices))

        # Choose a random vertex as the root
        self.root = random.choice(vertices)

        # Keep track of visited vertices
        visited = [self.root]

        # Keep track of the parents of each vertex
        parents = {self.root: None}

        # Assign each remaining vertex
        for vertex in vertices:
            if vertex != self.root:
                # Connect the vertex to another randomly chosen vertex that is already in the tree
                connect = random.choice(visited)
                parents[vertex] = connect

                # Create edge
                self.edges.append((vertex, connect))

                # Vertex has now been visited
                visited.append(vertex)

        parentNodes = []

        # Find all nodes that are a parent
        for vertex in vertices:
            if parents[vertex] not in parentNodes and parents[vertex] != None:
                parentNodes.append(parents[vertex])

        # parentNodes.sort()
        # print(parentNodes)

        # Find all leaf nodes (nodes that aren't a parent)
        for vertex in vertices:
            if vertex not in parentNodes:
                self.leaves.append(vertex)
        
        # self.leaves.sort()
        # print(self.leaves)

        # Update the adjacency matrix
        for (vertex, parent) in self.edges:
            # Generate random weight from [1, 10]
            weight = random.randint(1, 10)
            self.adjMatrix[vertex][parent] = weight
            self.adjMatrix[parent][vertex] = weight

            # self.adjMatrix[vertex][parent] = 1
            # self.adjMatrix[parent][vertex] = 1
    
    # Depth First Search graph traversal
    def DepthFirstSearch(self, start, visited=None):
        # Keep track of visited vertices
        if visited is None:
            visited = set()

        # Visit current vertex
        visited.add(start)

        # Print current vertex
        print(start, end=' ')

        # Check neighbors
        for neighbor in range(self.numVertices):
            # Check if edge exists and if neighbor has already been visited
            if self.adjMatrix[start][neighbor] > 0 and neighbor not in visited:
                # Recursively visit neighbors
                self.DepthFirstSearch(neighbor, visited) 

    # Depth First Search
    def DFS(self, start, target, currentPath=[]):
        # Add node to path
        currentPath = currentPath + [start]

        # If target node is found
        if start == target:
            return currentPath
        
        # Search for neighbors of current node
        for neighbor in range(self.numVertices):
            # Check for edge and if neighbor hasn't been visited yet
            if self.adjMatrix[start][neighbor] > 0 and neighbor not in currentPath:
                # Recursively search neighbor
                newPath = self.DFS(neighbor, target, currentPath)

                # New path didn't return None which means target was found
                if newPath != None:
                    return newPath
        
        # If target node isn't found, return None
        return None

    # Best First Search
    def BFS(self, start, target):
        # Keep track of visited nodes
        visited = [False] * self.numVertices

        # Create priority queue and add start node
        nodeQueue = PriorityQueue()
        nodeQueue.put((start, 0))
        visited[start] = True

        # Keep track of parent nodes to remember the path
        parents = {start: None}
        
        while not nodeQueue.empty():
            # Get and dequeue the node with lowest cost from the queue
            node = nodeQueue.get()[0]
            # print(node, end=" ")

            # Target node found
            if node == target:
                path = []

                # Get the path by backtracking from target node
                while node is not None:
                    path.append(node)
                    node = parents[node]
                
                path.reverse()
                return path
            
            # Search for neighbors of current node
            for neighbor in range(self.numVertices):
                # Check for edge and if node has been visited
                if self.adjMatrix[node][neighbor] > 0 and not visited[neighbor]:
                    # Add node to queue with its cost
                    nodeQueue.put((neighbor, self.adjMatrix[node][neighbor]))
                    visited[neighbor] = True
                    parents[neighbor] = node 
        
        # If target node isn't found, return None
        return None

if __name__ == "__main__":
    # Generate a random tree
    numVertices = 1000
    randomTree = Graph(numVertices)
    randomTree.GenerateTree()
    # randomTree.Display()

    source = randomTree.GetRoot()

    # Choose 3 random leaf nodes as the target nodes
    targets = random.sample(randomTree.GetLeaves(), 3)
    print("Root node: ", source)
    print("Target nodes: ", end=" ")
    print(*targets, sep=", ")

    # print("\nDepth First Search Traversal: ")
    # randomTree.DepthFirstSearch(source)

    print("\nDepth First Search: ")
    for i in range(len(targets)):
        print(targets[i], ": ", randomTree.DFS(source, targets[i]))

    print("\nBest First Search: ")
    for i in range(len(targets)):
        print(targets[i], ": ", randomTree.BFS(source, targets[i]))