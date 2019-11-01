# DFS


class Graph:
    def __init__(self, vertices):
        self.graph = {}
        for i in range(vertices):
            self.graph[i] = []

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def DFS(self, v):
        visited = [False]*(len(self.graph))
        self.DFSUtil(v, visited)


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print ("Graph: ")
for i in g.graph.items():
    print(i)
print("Following is DFS from (starting from vertex 2)")
g.DFS(2)
