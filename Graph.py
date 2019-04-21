from Queue import *
from math import inf

class Vertex(object):
    def __init__(self, label = '', color = ''):
        self.label = label
        self.color = color

    def __repr__(self):
        return 'Vertex(%s)' %  repr(self.label)

    __str__ = __repr__

class Edge(tuple):
    def __new__(cls, v, w, directed = False):
        cls.directed = directed
        return tuple.__new__(cls, (v, w))

    def __repr__(self):
        if self.directed:
            return 'Edge(From %s to %s)' % (repr(self[0]), repr(self[1]))
        if not self.directed:
            return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

class Graph(dict):
    """Graph is a dictionary of dictionary.
    The first dictionary maps a vertex to an internal dictionary that maps
    its out neighbours to out edges connecting them"""

    def __init__(self, vs = [], es = []):
        """
        Creates a new Graph
        @Args:
            vs: list of vertices
            es: list of edges
        @Returns:
            None
        """

        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e):
        v, w = e
        if v == w:
            raise LoopError('An edge cannot exist from a vertex to itself')

        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """
        Looks for an edge from v to w and returns it.
        Returns None if there is no edge
        """

        try:
            return self[v][w]
        except:
            return None

    def remove_edge(self, e):
        v, w = e
        self[v].pop(w)
        self[w].pop(v)

    def vertices(self):
        """Returns a list of all vertices in the graph"""

        vs = []
        for v in self:
            vs.append(v)
        return vs

    def edges(self):
        """Returns a list of all edges in the graph"""

        es = []
        for v in self:
            for w in self[v]:
                e = self[v][w]
                if e not in es:
                    es.append(e)
        return es

    def out_vertices(self, v):
        """Returns a list of all out vertices of v"""

        ns = []
        for w in self[v]:
            if w not in ns:
                ns.append(w)
        return ns

    def out_edges(self, v):
        """Returns a list of all out edges of v"""

        es = []
        for w in self[v]:
            e = self[v][w]
            if e not in es:
                es.append(e)
        return es

    def degree(self, v):
        return len(self.out_edges(v))

    def traverse_breadth_first(self, s):
        """
        Does a breadth first traversal of the graph starting from s
        @Args:
            s: starting vertex
        @Returns:
            None
        """
        for v in self:
            v.color = 'white'
            v.p = None
            v.level = inf

        s.color = 'grey'
        s.level = 0
        q = Queue()
        q.enqueue(s)

        while not q.is_empty():
            u = q.dequeue()
            for w in self.out_vertices(u):
                if w.color == 'white':
                    w.color = 'grey'
                    w.level = u.level + 1
                    w.p = u
                    q.enqueue(w)

            print(u)
            u.color = 'black'

    def depth_first_visit(self, v):
        """
        Does a depth first traversal of the graph starting from v
        @Args:
            v: starting vertex
        @Returns: None
        """

        v.color = 'grey'
        for u in self.out_vertices(v):
            if u.color == 'white':
                u.p = v
                self.depth_first_visit(u)
        print(v)
        v.color = 'black'

    def traverse_depth_first(self):
        """
        Wrapper around depth_first_visit to take care of unconnected graphs
        """

        for v in self:
            v.color = 'white'
            v.p = None

        for v in self:
            if v.color == 'white':
                self.depth_first_visit(v)

class DirectedGraph(Graph):
    def __init__(self, vs = [], es = []):
        """
        Creates a new directed graph
        @Args:
            vs: list of vertices
            es: list of edges
        @Returns:
            None
        """
        self.reverse_graph = {}
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self[v] = {}
        self.reverse_graph[v] = {}

    def add_edge(self, e):
        v, w = e
        if v == w:
            raise LoopError('An edge cannot exist from a vertex to itself.')

        e.directed = True
        self[v][w] = e
        self.reverse_graph[w][v] = e

    def remove_edge(self, e):
        v, w = e
        self[v].pop(w)
        self.reverse_graph[w].pop(v)

    def in_vertices(self, v):
        """Returns a list of all in vertices of v"""

        ns = []
        for w in self.reverse_graph[v]:
            if w not in ns:
                ns.append(w)
        return ns

    def in_edges(self, v):
        """Returns a list of all in edges of v"""

        es = []
        for w in self.reverse_graph[v]:
            e = self.reverse_graph[v][w]
            if e not in es:
                es.append(e)
        return es
