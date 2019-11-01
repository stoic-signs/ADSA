# BFS


class Graph:
    def __init__(self, vertices):
        self.graph = {}
        for i in range(vertices):
            self.graph[i] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, v):
        visited = [False]*(len(self.graph))
        queue = []
        queue.append(v)
        visited[v] = True
        while queue:
            v = queue.pop(0)
            print(v, end=' ')
            for i in self.graph[v]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Following is Breadth First Traversal"
       " (starting from vertex 2)")
g.BFS(2)
