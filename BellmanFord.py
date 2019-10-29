

class Graph:
	def __init__(self, vertices):
		self.N=vertices; self.graph={};
		for i in range(vertices):
			self.graph[i]=[];

	def addEdge(self, u, v, w):
		self.graph[u].append([v,w])

	def printArr(self, dist):
		print("Vertex\t\tDistance")
		for i in range(self.N):
			print("%d\t\t%0.f" %  (i, dist[i]))

	def BellmanFord(self, src):
		dist=[float("Inf")]*self.N;
		dist[src]=0

		for u in range(self.N-1):
			for [v, w] in self.graph[u]:
				if dist[u]!=float("Inf") and (dist[u] + w) < dist[v]:
					dist[v]=dist[u]+w

		for u in range(self.N-1):
			for [v, w] in self.graph[u]:
				if dist[u]!=float("Inf") and (dist[u]+w)<dist[v]:
					print ("Graph contains negative cycle")
					return

		self.printArr(dist)



g=Graph(10)
g.addEdge(0,1,-1)
g.addEdge(0,2,4)
g.addEdge(1,2,3)
g.addEdge(1,3,2)
g.addEdge(1,4,2)
g.addEdge(3,2,5)
g.addEdge(3,1,1)
g.addEdge(4,3,-3)

g.BellmanFord(0)

print(g.graph)
