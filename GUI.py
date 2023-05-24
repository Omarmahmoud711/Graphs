import tkinter as tk
from BackEnd import MatrixEditorBackend


class MatrixEditor(tk.Tk):
    def __init__(self, Vn):
        super().__init__()
        self.title("Matrix Editor")
        self.Vn = Vn
        self.matrix = [[0 for j in range(Vn)] for i in range(Vn)]
        self.Directed_matrix = [[0 for j in range(Vn)] for i in range(Vn)]
        self.mst_matrix = [[0 for j in range(self.Vn)] for i in range(self.Vn)]
        self.entries = []
        self.create_widgets()

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
            for j in range(i + 1, self.Vn):
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

    def create_widgets(self):
        # Create labels for row and column headers
        for i in range(self.Vn):
            row_label = tk.Label(self, text=str(i), width=5)
            row_label.grid(row=i + 1, column=0)
            col_label = tk.Label(self, text=str(i), width=5)
            col_label.grid(row=0, column=i + 1)

        # Create matrix entries
        for i in range(self.Vn):
            row = []
            for j in range(self.Vn):
                entry = tk.Entry(self, width=5)
                entry.grid(row=i + 1, column=j + 1)
                entry.insert(tk.END, str(self.matrix[i][j]))
                row.append(entry)
            self.entries.append(row)

        # Create save button
        save_button = tk.Button(self, text="Save", command=self.save_matrix)
        save_button.grid(row=self.Vn + 1, column=self.Vn + 1)

    def save_matrix(self):
        # Update matrix with values from entries
        for i in range(self.Vn):
            for j in range(self.Vn):
                self.matrix[i][j] = int(self.entries[i][j].get())
                self.Directed_matrix[i][j] = int(self.entries[i][j].get())

        # Create undirected matrix
        self.matrix_undirected = [[0 for j in range(self.Vn)] for i in range(self.Vn)]
        for i in range(self.Vn):
            for j in range(self.Vn):
                if self.matrix[i][j] != 0:
                    self.matrix_undirected[i][j] = self.matrix[i][j]
                    self.matrix_undirected[j][i] = self.matrix[i][j]

        # Remove loops in the matrix
        for i in range(self.Vn):
            for j in range(self.Vn):
                if i == j:
                    self.matrix_undirected[i][j] = 0

        MatrixEditorBackend.show_graph(self, self.Directed_matrix, "DIRECTED MATRIX")
        MatrixEditorBackend.show_undirected_graph(self, self.matrix_undirected, "UNDIRECTED MATRIX")
        MatrixEditorBackend.mst_calculate(self)

    def show_graph(self, mat, strg):
        MatrixEditorBackend.show_graph(self, mat, strg)

    def show_undirected_graph(self, matrix, stg):
        MatrixEditorBackend.show_undirected_graph(self, matrix, stg)


    def dijkstra(self):
        MatrixEditorBackend.dijkstra(self)
