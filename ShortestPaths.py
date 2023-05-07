import random

class Graph:
    def __init__ (self, numVertices):
        self.numVertices = numVertices
        self.adjMatrix = [[0 for _ in range(self.numVertices)] for _ in range(self.numVertices)]
        self.root = None

    def Generate(self):
        # Create a list of vertices from 0 - numVertices
        vertices = list(range(self.numVertices))

        # Choose a random root
        self.root = random.choice(vertices)

        # Keep track of visited vertices
        visited = [self.root]

        # Keep track of the parents of each vertex
        parents = {self.root: None}

        # Keep track of edges
        edges = []

        # Visit each remaining vertex and randomly select a parent from visited vertices
        for vertex in vertices:
            if vertex != self.root:
                parent = random.choice(visited)
                parents[vertex] = parent
                edges.append((vertex, parent))
                visited.append(vertex)

        # Print the parent of each vertex to verify that it forms a tree
        for vertex in vertices:
            print(f"Vertex {vertex}: parent is {parents[vertex]}")

        for (parent, vertex) in edges:
            # adj_matrix[vertex][parent] = round(random.uniform(0.0, 1.0), 2)
            self.adjMatrix[vertex][parent] = 1
            # self.adjMatrix[parent][vertex] = 1

    def GetRoot(self):
        return self.root
        
    def Display(self):
        # Print the adjacency matrix
        for row in self.adjMatrix:
            print(row)

    def DFS(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)

                # Get the neighbors of the current vertex
                neighbors = [i for i in range(len(self.adjMatrix[vertex])) if self.adjMatrix[vertex][i] == 1]

                # Add unvisited neighbors to the stack
                for neighbor in neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)

if __name__ == "__main__":
    numVertices = 10
    randomTree = Graph(numVertices)
    randomTree.Generate()
    randomTree.Display()
    randomTree.DFS(randomTree.GetRoot())