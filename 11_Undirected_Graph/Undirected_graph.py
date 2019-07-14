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
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
           self.vertices[vertex.name] = vertex
        else:
            print('Something went wrong !')

    def add_edges(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.vertices[u].add_neighbours(self.vertices[v])
            self.vertices[v].add_neighbours(self.vertices[u])
        else:
            print('Vertices are not in the graph !')

    def show_graph(self):
        for i in self.vertices:
            print(self.vertices[i].name)
            for j in self.vertices[i].neighbours:
                print('\t', j.name)
            print('================')

    def __getitem__(self, name):
        if isinstance(name, slice):
            print('Slicing is not supported !')
        else:
            try:
                return self.vertices[name]
            except KeyError:
                print('No vertex found with name ', index)

    def __setitem__(self, name, value):
        if isinstance(name, slice):
            print('Slicing is not supported !')
        else:
            try:
                self.vertices[name].value = value
            except KeyError:
                print('No vertex found name ', name)
