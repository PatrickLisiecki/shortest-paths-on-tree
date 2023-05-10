import random
from queue import PriorityQueue

class Graph:
    def __init__ (self, numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[0 for _ in range(self.numVertices)] for _ in range(self.numVertices)]
        self.root = None
        self.edges = []

    # Returns the root of the tree
    def GetRoot(self):
        return self.root
        
    # Prints the adjacency matrix
    def Display(self):
        for row in self.adjMatrix:
            print(row)

    # Generates an undirected graph with no cycles
    def GenerateTree(self):
        # Create a list of vertices from [0 - numVertices)
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
                # Choose a random parent for the vertex
                parent = random.choice(visited)
                parents[vertex] = parent

                # Create edge
                self.edges.append((vertex, parent))

                # Vertex has now been visited
                visited.append(vertex)

        # Print the parent of each vertex to verify that it forms a tree
        for vertex in vertices:
            print(f"Vertex {vertex}: parent is {parents[vertex]}")

        # Update the adjacency matrix
        for (vertex, parent) in self.edges:
            # Generate random weight from 1 - 10
            weight = random.randint(1, 10)
            self.adjMatrix[vertex][parent] = weight
            self.adjMatrix[parent][vertex] = weight

            # self.adjMatrix[vertex][parent] = 1
            # self.adjMatrix[parent][vertex] = 1
    
    # Depth First Search graph traversal
    def DFS(self, start, visited=None):
        # Keep track of visited vertices
        if visited is None:
            visited = set()

        # Visit current vertex
        visited.add(start)

        # Print current vertex
        print(start, end=' ')

        # Check neighbors
        for neighbor in range(len(self.adjMatrix[start])):
            # Check if edge exists and if neighbor has already been visited
            if self.adjMatrix[start][neighbor] > 0 and neighbor not in visited:
                # Recursively visit neighbors
                self.DFS(neighbor, visited) 

    def DFS2(self, start, end, path=[]):
        path = path + [start] # add the current vertex to the path
        if start == end:
            return path # if we have found the end node, return the path
        for neighbor in range(len(self.adjMatrix[start])):
            if self.adjMatrix[start][neighbor] > 0 and neighbor not in path:
                # if the neighbor is adjacent and not already in the path
                new_path = self.DFS2(neighbor, end, path) # recursively search from the neighbor
                if new_path:
                    return new_path # if the neighbor path contains the end node, return it
        return None # if we have not found the end node, return None

    def BestFirstSearch(self, start_node, goal_node):
        num_nodes = self.numVertices
        visited = [False] * num_nodes
        pq = PriorityQueue()
        pq.put((0, start_node))  # Enqueue the starting node with priority 0
        visited[start_node] = True
        
        while not pq.empty():
            node = pq.get()[1]  # Dequeue the node with the highest priority
            print(node, end=" ")
            if node == goal_node:
                break  # Goal node found
            
            for neighbor in range(num_nodes):
                if self.adjMatrix[node][neighbor] > 0 and not visited[neighbor]:
                    # Enqueue the unvisited neighbor with its priority based on its distance from the goal node
                    pq.put((self.adjMatrix[node][neighbor], neighbor))
                    visited[neighbor] = True

if __name__ == "__main__":
    numVertices = 20
    randomTree = Graph(numVertices)
    randomTree.GenerateTree()
    randomTree.Display()

    print("\nDFS: ")
    randomTree.DFS(randomTree.GetRoot())

    print("\nDFS2: ")
    print(randomTree.DFS2(randomTree.GetRoot(), 15))

    print("BFS: ")
    randomTree.BestFirstSearch(randomTree.GetRoot(), 15)