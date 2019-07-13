class Vertex:
    def __init__(self, name, value = None):
        self.name = name
        self.value = value

class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []
        self.indx = {}
        self.rev_indx = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            for row in self.edges:
                row.append(0)
            self.edges.append([0]*(len(self.edges)+1))
            self.indx[vertex.name] = len(self.indx)
            self.rev_indx[len(self.rev_indx)] = vertex.name
        else:
            print('Something wents wrong !')

    def add_edges(self, u, v, weight):
        if u in self.vertices and v in self.vertices:
            self.edges[self.indx[u]][self.indx[v]] = weight
        else:
            print('Vertices are not in graph !')

    def show_graph(self):
        for i in self.vertices:
            print(self.vertices[i].name)
            for j, k in enumerate(self.edges[self.indx[i]]):
                if k > 0:
                    print('\t', self.vertices[self.rev_indx[j]].name, k)
            print('============')
