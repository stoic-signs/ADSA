# Kruskal's


class Graph:
    def __init__(self, vertices):
        self.N = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def Kruskal(self):
        result = []
        i = 0
        e = 0
        print(self.graph)
        #for i in range(len(self.graph)):
        #    for v in self.graph[i]:
        #        print(self.graph[i][v][1])
        self.graph1 = sorted(self.graph, key=lambda item: item[2])
        print(self.graph1)
        parent = []
        rank = []
        for node in range(self.N):
            parent.append(node)
            rank.append(0)

        while e < (self.N-1):
            for u, v, w in self.graph1:
                i = i+1
                x = self.find(parent, u)
                y = self.find(parent, v)
                if x != y:
                    e = e+1
                    result.append([u, v, w])
                    self.union(parent, rank, x, y)
        print ("Following are the edges in the constructed MST")
        for u, v, weight in result:
                # print str(u) + " -- " + str(v) + " == " + str(weight)
            print ("%d -- %d == %d" % (u, v, weight))


# Driver code
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)
# g.addEdge(3, 1, 2)

g.Kruskal()
