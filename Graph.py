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
    def __new__(cls, v, w):
        return tuple.__new__(cls, (v, w))

    def __repr__(self):
        return 'Edge(%s, %s)' % (repr(self[0]), repr(self[1]))

    __str__ = __repr__

class Graph(dict):
    def __init__(self, vs = [], es = []):
        for v in vs:
            self.add_vertex(v)

        for e in es:
            self.add_edge(e)

    def add_vertex(self, v):
        self[v] = {}

    def add_edge(self, e):
        v, w = e
        self[v][w] = e
        self[w][v] = e

    def get_edge(self, v, w):
        """Looks for an edge between `v` and `w` and returns it.
        Returns `None` if there is no edge"""

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
        """Returns a list of all vertices connected to `v` by an edge"""

        ns = []
        for w in self[v]:
            if w not in ns:
                ns.append(w)
        return ns

    def out_edges(self, v):
        """Returns a list of all edges that connect `v` to other vertices"""

        es = []
        for w in self[v]:
            e = self[v][w]
            if e not in es:
                es.append(e)
        return es

    def degree(self, v):
        return len(self.out_edges(v))

    def traverse_breadth_first(self, s):
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
        v.color = 'grey'
        for u in self.out_vertices(v):
            if u.color == 'white':
                u.p = v
                self.depth_first_visit(u)
        print(v)
        v.color = 'black'

    def traverse_depth_first(self):
        for v in self:
            v.color = 'white'
            v.p = None

        for v in self:
            if v.color == 'white':
                self.depth_first_visit(v)
