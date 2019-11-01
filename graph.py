
def link(G, x, y):


if x not in G:
G[x] = {}
(G[x])[y] = 1
if y not in G:
G[y] = {}
(G[y])[x] = 1
return G


def rec_dfs(G, node, traverse):


traverse[node] = True
print(node)
for neighours in G[node]:
if neighours not in traverse:
rec_dfs(G, neighours, traverse)


def start(G):


traverse = {}
for node in G.keys():
if node not in traverse:
rec_dfs(G, node, traverse)
if __name__ == "__main__":
n = int(input("Enter the number of edges: "))
G = {}
x = []
y = []
for _ in range(n):
print("Enter the vertices making an edge u,v: ")
varx = input("Enter u: ")
x.append(varx)
vary = input("Enter v: ")
y.append(vary)
for i in range(n):
link(G, x[i], y[i])
# print(x)
# print(y)
print(G)
start(G)


def link(G, x, y):


if x not in G:
G[x] = {}
(G[x])[y] = 1
if y not in G:
G[y] = {}
(G[y])[x] = 1
return G


def bfs_connected_components(graph, start):


explored = []
queue = [start]
while queue:
node = queue.pop(0)
if node not in explored:
explored.append(node)
neighbours = graph[node]
for neighbour in neighbours:
queue.append(neighbour)
return explored
if __name__ == "__main__":
n = int(input("Enter the number of edges: "))
G = {}
x = []
y = []
for _ in range(n):
print("Enter the vertices making an edge u,v: ")
varx = input("Enter u: ")
x.append(varx)
vary = input("Enter v: ")
y.append(vary)
for i in range(n):
link(G, x[i], y[i])
# print(x)
# print(y)
print("Graph: ", G)
print("\n", bfs_connected_components(G, next(iter(G))))
