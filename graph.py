from __future__ import print_function
from collections import defaultdict

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.dist = [float("Inf")] * len(graph)
        self.parent = [-1] * len(graph)

    def print_graph(self):
        for i in self.graph:
            for node in i:
                print(node, end='\t')
            print()
 
    def minDistance(self,dist,queue):
        minimum = float("Inf")
        min_index = -1
         
        for i in range(len(dist)):
            if dist[i] < minimum and i in queue:
                minimum = dist[i]
                min_index = i
        return min_index
 
    def printPath(self, j):
        if self.parent[j] == -1 :
            print("{}".format(j), end=" ")
            return
        self.printPath(self.parent[j])
        print ("{}".format(j), end=" ")
          
    def dijkstra(self, graph, src):
        row = len(graph)
        col = len(graph[0])
        self.dist[src] = 0
        queue = []
        for i in range(row):
            queue.append(i)
        while queue:
            u = self.minDistance(self.dist,queue)
            queue.remove(u)
            for i in range(col):
                if graph[u][i] and i in queue:
                    if self.dist[u] + graph[u][i] < self.dist[i]:
                        self.dist[i] = self.dist[u] + graph[u][i]
                        self.parent[i] = u

    def get_path(self, s_loc, d_loc):
        self.dijkstra(self.graph, s_loc)
        self.printPath(d_loc)

    def update_graph(self, x_c, y_c, val):
        self.graph[x_c][y_c] = val


def get_graph():
    graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
        ]
    g = Graph(graph)
    return g

if __name__ == '__main__':
    gp = get_graph()
    gp.get_path(0, 4)