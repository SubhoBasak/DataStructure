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
            print('Something went wrong !')

    def add_edges(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.edges[self.indx[u]][self.indx[v]] = 1
            self.edges[self.indx[v]][self.indx[u]] = 1
        else:
            print('Vertices are not in graph !')

    def show_graph(self):
        for i in self.indx:
            print(i)
            for j, k in enumerate(self.edges[self.indx[i]]):
                if k == 1:
                    print('\t', self.vertices[self.rev_indx[j]].name)
            print('=============')

    def __getitem__(self, name):
        if isinstance(name, slice):
            print('Slicing is not supported !')
        elif name in self.vertices:
            return self.vertices[name]
        else:
            print('No vertex is available with name ', name)

    def __setitem__(self, name, value):
        if isinstance(name, slice):
            print('Slicing is not supported !')
        elif name in self.vertices:
            self.vertices[name].value = value
        else:
            print('No vertices available with name ', name)
