
from os import sep
from queue import *
from collections import OrderedDict


class graph:
    def __init__(self, nodes, is_direct=False):
        self.nodes = nodes
        self.adj_list = {}
        self.is_direct = is_direct

        for node in self.nodes:
            self.adj_list[node] = []
        # print(self.adj_list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        if not self.is_direct:

            self.adj_list[v].append(u)  # dont use this line for directed graph

    def print_graph(self):
        return (self.adj_list)

    def dfs(self, rand, adj, colors, parents, out):
        colors[rand] = "g"
        out.append(rand)

        for i in adj[rand]:
            if colors[i] == "w":
                parents[i] = rand
                self.dfs(i, adj, colors, parents, out)
        colors[i] = "b"
        return (out)

    def bfs(self, rand, visited, level, bfs_output, q, parent, k):
        self.rand = rand
        self.visited = visited
        self.level = level
        self.bfs_output = bfs_output
        self.q = q
        self.parent = parent
        self.k = k
        for i in self.k.keys():
            visited[i] = False
            level[i] = -1
            parent[i] = None
        visited[self.rand] = True
        level[self.rand] = 0
        self.q.put(self.rand)
        # print(self.visited)
        # print(self.level)
        while not self.q.empty():
            u = self.q.get()
            self.bfs_output.append(u)
            for v in self.k[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.parent[v] = u
                    self.level[v] = self.level[u]+1
                    self.q.put(v)
        # print(self.parent)  ## to find the parent of each node
        #  print(self.level)  ## to check the distance of any node from the source node
        return (self.bfs_output)

    def shortest_distance_from_node(self, rand, visited, level, bfs_output, q, parent, find_distance):
        self.rand = rand
        self.visited = visited
        self.level = level
        self.bfs_output = bfs_output
        self.q = q
        self.parent = parent
        self.find_distance = find_distance
        for i in self.adj_list.keys():
            visited[i] = False
            level[i] = -1
            parent[i] = None
        visited[self.rand] = True
        level[self.rand] = 0
        self.q.put(self.rand)
        # print(self.visited)
        # print(self.level)
        while not self.q.empty():
            u = self.q.get()
            self.bfs_output.append(u)
            for v in self.adj_list[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.parent[v] = u
                    self.level[v] = self.level[u]+1
                    self.q.put(v)

        # to know the distance of a specific vertex
        return (self.level[self.find_distance])
        # return (self.level)                        # if we want to know the distance of all vertexes from source node

    def shortest_path(self, rand, visited, level, bfs_output, q, parent, path, find_path):
        self.rand = rand
        self.visited = visited
        self.level = level
        self.bfs_output = bfs_output
        self.q = q
        self.parent = parent
        self.path = path
        self.find_path = find_path
        for i in self.adj_list.keys():
            visited[i] = False
            level[i] = -1
            parent[i] = None
        visited[self.rand] = True
        level[self.rand] = 0
        self.q.put(self.rand)
        # print(self.visited)
        # print(self.level)
        # print(self.parent)
        while not self.q.empty():
            u = self.q.get()
            self.bfs_output.append(u)
            for v in self.adj_list[u]:
                if not self.visited[v]:
                    self.visited[v] = True
                    self.parent[v] = u
                    self.level[v] = self.level[u]+1
                    self.q.put(v)
        print(self.parent)
        # print(self.parent[self.find_path])
        while self.find_path != None:
            self.path.append(self.find_path)
            # print(self.path)
            self.find_path = self.parent[self.find_path]
        self.path.reverse()

        return (self.path)

    def primsAlgo(gra, vertices):
        slected = [0]*vertices
        no_edge = 0
        slected[0] = True
        inf = 999999999
        print("Edge : Weight    (Prim's Algorithem)")
        while (no_edge < vertices - 1):

            minimum = inf
            a = 0
            b = 0
            for m in range(vertices):
                if slected[m]:
                    for n in range(vertices):
                        if ((not slected[n]) and gra[m][n] and n != m):
                            # not in selected and there is an edge
                            if minimum > gra[m][n]:
                                minimum = gra[m][n]
                                a = m
                                b = n
            print(str(a) + "-" + str(b) + ":" + str(gra[a][b]))
            slected[b] = True
            no_edge += 1

    def kruskalsAlgo(gra, vertices):
        p = {}
        o = []
        # sorted_values={}
        for i in range(vertices):
            for j in range(vertices):
                if gra[i][j] == 0:
                    pass
                else:
                    if i == j:
                        pass
                    else:
                        p[i, j] = [int(gra[i][j])]

        sorted_values = sorted(
            p.items(), key=lambda x: x[1])  # Sort the values
        for i in range(len(sorted_values)):

            pass
        # sorted_dict = {}

        # for i in sorted_values:
        #     for k in p.keys():
        #         if p[k] == i:
        #             sorted_dict[k] = p[k]

        # for i in sorted_dict.keys():
        #     if i[0]==0:
        #         print("no edge")
        #     elif sorted_dict[i]
        print(p)
        print(sorted_values)
        print(type(sorted_values))

    def find_cycle_dfs(self, rand, adj, colour, parent, out):
        self.rand = rand
        self.adj = adj
        self.colour = colour
        self.parent = parent
        self.out = out
        self.colour[self.rand] = "g"
        for v in self.adj[self.rand]:
            # and self.parent[v]!=self.rand: -> Do this for undirected graph
            if self.colour[v] == "w":
                c = self.find_cycle_dfs(
                    v, self.adj, self.colour, self.parent, self.out)
                if c == True:
                    return (True)
            elif self.colour[v] != "w":
                # print(f"cycle present from {self.rand} to {v}")
                return (True)

        self.colour[self.rand] = "b"
        return (False)


nodes = ["a", "b", "c", "d", "e"]  # making a graph, the inputs of it
# g=graph(nodes,is_direct=True)
g = graph(nodes)
edges = [("a", "b"), ("a", "e"), ("b", "c"),
         ("b", "e"), ("c", "d"), ("d", "e")]
for u, v in edges:
    g.add_edge(u, v)
k = g.print_graph()
print(k)  # end of the input section


# nodes = ["a", "b", "c", "d", "e"]  # DFS input start
# gr = graph(nodes)
# # edges=[("a","b"),("a","c"),("b","d"),("b","e"),("e","f"),("c","f")]
# edges = [("a", "b"), ("a", "e"), ("b", "c"),
#          ("b", "e"), ("c", "d"), ("d", "e")]
# for u, v in edges:
#     gr.add_edge(u, v)
# k = gr.print_graph()
# # print(k)
# colors = {}
# parents = {}
# time = {}
# for i in k.keys():
#     colors[i] = "w"
#     parents[i] = None
#     # time[i]=[-1,-1]    ##no need of time##
# # print(colors)
# # print(parents)
# # print(time)
# out = []
# o = gr.dfs("a", k, colors, parents, out)
# print(o)  # DFS input end


# nodes = ["a", "b", "c", "d", "e", "f"]  # BFS input start
# gr = graph(nodes)
# edges = [("a", "b"), ("a", "c"), ("b", "d"),
#          ("b", "e"), ("e", "f"), ("c", "f")]
# # edges=[("a","b"),("a","e"),("b","c"),("b","e"),("c","d"),("d","e")]
# for u, v in edges:
#     gr.add_edge(u, v)
# k = gr.print_graph()  # here k is the adjecency list
# visited = {}
# level = {}
# parent = {}
# bfs_output = []
# q = Queue()
# o = gr.bfs("f", visited, level, bfs_output, q, parent, k)
# print(o)                             # end of BFS input


# # find the distance of all vertex input start
# nodes = ["a", "b", "c", "d", "e", "f"]
# gr = graph(nodes)
# edges = [("a", "b"), ("a", "c"), ("b", "d"),
#          ("b", "e"), ("e", "f"), ("c", "f")]
# # edges=[("a","b"),("a","e"),("b","c"),("b","e"),("c","d"),("d","e")]
# for u, v in edges:
#     gr.add_edge(u, v)
# k = gr.print_graph()
# visited = {}
# level = {}
# parent = {}
# bfs_output = []
# q = Queue()
# find_distance = "a"
# # here "f" is considered to be source node
# o = gr.shortest_distance_from_node(
#     "f", visited, level, bfs_output, q, parent, find_distance)
# print(o)  # end of find the distance of all vertex input


# nodes = ["a", "b", "c", "h", "e", "f", "g", "d"]  # shortest path input start
# gr = graph(nodes)
# # edges=[("a","b"),("a","c"),("b","d"),("b","e"),("e","f"),("c","f")]
# # edges=[("a","b"),("a","e"),("b","c"),("b","e"),("c","d"),("d","e")]
# edges = [('a', 'b'), ('a', 'd'), ('b', 'c'), ('d', 'e'), ('d', 'f'),
#          ('e', 'f'), ('e', 'g'), ('f', 'h'), ('g', 'h')]
# for u, v in edges:
#     gr.add_edge(u, v)
# k = gr.print_graph()
# # print(k)
# visited = {}
# level = {}
# parent = {}
# bfs_output = []
# q = Queue()
# path = []
# find_path = "g"
# o = gr.shortest_path("a", visited, level, bfs_output,
#                      q, parent, path, find_path)
# print(o)  # end of shortest path input


# find cycle in directed and undirected graph
# nodes = ["a", "b", "c", "d", "e"]
# edges = [("a", "b"), ("b", "d"), ("d", "a"), ("a", "c"), ("d", "e")]
# # nodes = ["a", "b", "c", "d", "e", "f"]
# # edges = [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("b", "f")]
# gr = graph(nodes, is_direct=True)
# for u, v in edges:
#     gr.add_edge(u, v)
# k = gr.print_graph()
# colors = {}
# parents = {}
# time = {}
# o = False
# for i in k.keys():
#     colors[i] = "w"
#     parents[i] = None
# out = []
# o = gr.find_cycle_dfs("a", k, colors, parents, out)
# if o == True:
#     print("The graph is Cyclic")
# else:
#     # end of finding cycle in directed and undirected graph
#     print("the graph is not cyclic")


# gra=[[0, 19, 5, 0, 0],    ##prims Algorithem input start
#      [19, 0, 5, 9, 2],
#      [5, 5, 1, 1, 6],
#      [0, 9, 1, 19, 1],
#      [0, 2, 6, 1, 0]]
# vertices=5
# gr=graph.primsAlgo(gra,vertices)  ##prims algorithem input ends


# gra=[[0, 19, 5, 0, 0],    ##kruskals Algorithem input start
#      [19, 0, 5, 9, 2],
#      [5, 5, 1, 1, 6],
#      [0, 9, 1, 19, 1],
#      [0, 2, 6, 1, 0]]
# vertices=5
# gr=graph.kruskalsAlgo(gra,vertices)  ##kruskals algorithem input ends
