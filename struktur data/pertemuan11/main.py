class Graph:
    def __init__(self, directed=False, weighted=False):
        self.directed = directed
        self.weighted = weighted
        self.adj_list = {}

    def add_vertex(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = []

    def add_edge(self, src, dst, weight=1):
        self.add_vertex(src)
        self.add_vertex(dst)

        self.adj_list[src].append((dst, weight))

        if not self.directed:
            self.adj_list[dst].append((src, weight))

    def print_adjacency_list(self):
        for v, neighbors in self.adj_list.items():
            if self.weighted:
                tampil = [f"{n}({w})" for n, w in neighbors]
            else:
                tampil = [n for n, w in neighbors]

            print(f"{v} -> {tampil}")

    def build_adjacency_matrix(self):
        names = list(self.adj_list.keys())
        index = {nm: i for i, nm in enumerate(names)}

        size = len(names)
        matrix = [[0] * size for _ in range(size)]

        for v, neighbors in self.adj_list.items():
            for n, w in neighbors:
                matrix[index[v]][index[n]] = w if self.weighted else 1

        return names, matrix

    def print_adjacency_matrix(self):
        names, matrix = self.build_adjacency_matrix()

        for i, nm in enumerate(names):
            print(i, "=", nm)

        for row in matrix:
            print(row)

peta = Graph(directed=False, weighted=True)

peta.add_edge("Kampus USU", "Perpustakaan", 2)
peta.add_edge("Kampus USU", "Rumah Sakit", 4)
peta.add_edge("Perpustakaan", "Pusat Perbelanjaan", 3)
peta.add_edge("Rumah Sakit", "Pusat Perbelanjaan", 5)
peta.add_edge("Pusat Perbelanjaan", "Terminal", 6)

print("ADJACENCY LIST")
peta.print_adjacency_list()

print("\nADJACENCY MATRIX")
peta.print_adjacency_matrix()