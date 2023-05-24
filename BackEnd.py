import networkx as nx
import matplotlib.pyplot as plt
import sys
import heapq


class MatrixEditorBackend:
    def __init__(self, Vn):
        self.Vn = Vn

    def show_graph(self, mat, strg):
        labels = [str(i) for i in range(self.Vn)]
        # Create graph from matrix
        G = nx.DiGraph()
        for i in range(self.Vn):
            for j in range(self.Vn):
                if mat[i][j] != 0:
                    G.add_edge(labels[i], labels[j], weight=mat[i][j])

        # Define positions for nodes
        pos = nx.spring_layout(G)

        # Draw nodes and edges
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)}
        )
        nx.draw_networkx_labels(G, pos)

        # Show plot
        plt.axis("off")
        plt.title(strg)
        plt.show()

    def show_undirected_graph(self,matrix, stg):

        labels = [str(i) for i in range(self.Vn)]
        # Create graph from undirected matrix
        G = nx.Graph()
        for i in range(self.Vn):
            for j in range( self.Vn):
                if matrix[i][j] != 0:
                    G.add_edge(labels[i], labels[j], weight=matrix[i][j])

        # Define positions for nodes
        pos = nx.spring_layout(G)

        # Draw nodes and edges
        nx.draw_networkx_nodes(G, pos)
        nx.draw_networkx_edges(G, pos)
        nx.draw_networkx_edge_labels(
            G, pos, edge_labels={(u, v): d["weight"] for u, v, d in G.edges(data=True)})
        nx.draw_networkx_labels(G, pos)

        # Show plot
        plt.axis("off")
        plt.title(stg)
        plt.show()
        print("hiiii")

    def mst_calculate(self):
        cost = 0
        self.S = int(input("Enter the value of the node: "))
        # got the matrix for ex:
        #  0   1   2   3
        # 0[0   5   7   9]
        # 1[0  0    3   0]
        # 2[0  0    0   1]
        # 3[0  0    0   0]
        #chose s=0 for example
        if self.S > (self.Vn) - 1 or self.S < 0:
            print("Enter a valid node number")
            self.mst_calculate(self)#check if u entered a valid node

        print(self.matrix_undirected)
        # Create a list to store visited nodes and initialize with False
        visited = [False] * self.Vn#=[F F F F]

        # Create a list to store minimum spanning tree edges
        mst = []

        # Mark the starting node as visited
        visited[self.S] = True
        #[T F F F]

        # Repeat until all nodes are visited
        while False in visited:
            min_edge = float('inf')
            min_edge_from = None
            min_edge_to = None
            for i in range(self.Vn):
                if visited[i]:#0 i visited...1 is visited..2is visited
                    for j in range(self.Vn):
                        if not visited[j] and 0 < self.matrix_undirected[i][j] < min_edge:#0 is visited , 1 is not visited,2 not visited but 7>5 false,3 not visited 9>5 false....0,1 are visited ,2 not visited and <inf,3not visited but it's equal 0 .... all is visited except 3
                            min_edge = self.matrix_undirected[i][j]#min edge =5,min edge=3,min edge=1
                            min_edge_from = i#i=0,i=1,i=2
                            min_edge_to = j#j=1,j=2,j=3
            visited[min_edge_to] = True#1 is visited..2 is visited..3 is visited
            mst.append((min_edge_from, min_edge_to))#mst=(0,1)..mst=(0,1),(1,2)..mst=(2,3)
            cost = cost + self.matrix_undirected[min_edge_from][min_edge_to]#cost=5...cost=8...cost=9...finished

        # Return the minimum spanning tree
        print(mst)
        self.matrix = [[0 for j in range(self.Vn)] for i in range(self.Vn)]
        for i, j in mst:
            self.matrix[i][j] = self.matrix_undirected[i][j]
        print(self.matrix)
        self.show_undirected_graph(self.matrix, "Using Prim's Algorithm")
        print(self.Directed_matrix)
        print("\n Total cost of the path = ", cost)

        self.dijkstra()

    def dijkstra(self):

        graph = self.Directed_matrix
        #got the matrix for ex:
        #  0   1   2   3
        #0[0   5   7   9]
        #1[0  0    3   0]
        #2[0  0    0   1]
        #3[0  0    0   0]

        start = int(input("Enter the Start node for Dijkstra's algorithm:"))
        #let  the start node be zero


        # from the start node to all other nodes,all of them are equal sys.maxsize which is the largest integer a system can handle
        dist = {i: sys.maxsize for i in range(len(graph))}
        #dist={(0:inf),(1,inf),(2,inf),(3,inf)}

        dist[start] = 0
        #since we visited the start then it's distance to itself =0
        #dist={(0,0),(1,inf),(2,inf),(3,inf)}

        # Create a priority queue to store nodes and their distances
        priority_queue = [(0, start)]
        #pq=[(0.0)]

        while priority_queue:#loop untill queue is empty

            # Get the node with the smallest distance from the start node
            current_dist, current_node = heapq.heappop(priority_queue)
            #current_dist=0,current_node=0

            #if the current node has already been visited, meaning that a shorter path to that node has already been found.
            if current_dist > dist[current_node]:
                continue

            # Update the distances of the adjacent nodes
            for neighbor, cost in enumerate(graph[current_node]):#1stloop: neighbor =0 so nothing happends
                #2ndloop:neighbor=1,cost=inf
                if cost != 0:
                    new_cost = dist[current_node] + cost#increasing the cost by the cost of path and cost of node
                    if new_cost < dist[neighbor]:#if the new cost is less than the cost of the node then relax it
                        dist[neighbor] = new_cost
                        heapq.heappush(priority_queue, (new_cost, neighbor))#then add it to the queue so that the queue isn't empty untill we check all nodes not visited

        dijkstra_matrix = [[0 for j in range(self.Vn)] for i in range(self.Vn)]#create the matrix to show it in the graph
        print(dist)
        for i in dist:
            dijkstra_matrix[start][i] = dist[i]
        print(dijkstra_matrix)
        self.show_graph(dijkstra_matrix, "Dijkstra's Graph:")


