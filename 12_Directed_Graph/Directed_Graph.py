class Vertex:
    def __init__(self, name, value = None):
        self.name = name
        self.value = value
        self.neighbours = []

    def add_neighbours(self, V):
        if V not in self.neighbours:
            self.neighbours.append(V)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
        else:
            print('Something went wrong !')

    def add_edges(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbours(self.vertices[v])
        else:
            print('Vertices are not in graph !')

    def show_graph(self):
        for i in self.vertices:
            print(self.vertices[i].name)
            for j in self.vertices[i].neighbours:
                print('\t', j.name)
            print('=============')

    def __getitem__(self, name):
        if isinstance(name, slice):
            print('Slicing is not supported !')
        elif name in self.vertices:
            return self.vertices[name]
        else:
            print('No vertex available with name ', name)

    def __setitem__(self, name, value):
        if isinstance(name, slice):
            print('Slicing is not available !')
        elif name in self.vertices:
            self.vertices[name] = value
        else:
            print('No vertex available with name ', name)
