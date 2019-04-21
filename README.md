# CS202 Assignment
 
BFS and DFS, primarily.
----

### How to get it running?
0. Clone the repository. `cd` into it.
1. Open a python interactive shell and import the `Graph` module. `from Graph
   import *`.
2. ???
3. Profit!

#### Usage Instructions
Creating a new graph:

```
    >>> g = Graph()
```  

for directed graphs:

```
    >>> g = DirectedGraph()
```  

this initializes an empty graph, which is quite boring. Let's add some
vertices! 

Create a couple of new vertices first:

```
    >>> v = Vertex('v')
    >>> w = Vertex('w')
    >>> x = Vertex('x')
```

Create some edges between the vertices:

```
    >>> e1 = Edge(v, w)
    >>> e2 = Edge(v, x)
```
For a directed graph these would create edges that go from `Vertex('v')` to
`Vertex('w')` and from `Vertex('v')` to `Vertex('w')` respectively.

Add the vertices and edges to the graph:

```
    >>> g.add_vertex(v)
    >>> g.add_vertex(w)
    >>> g.add_vertex(x)
    >>> g.add_edge(e1)
    >>> g.add_edge(e2)
```

or just initialize a new graph with the created vertices and edges:

```
    >>> udh = Graph([v, w, x], [e1, e2])
    >>> dh = DirectedGraph([v, w, x], [e1, e2])
```

Detailed information for each Graph method is in docstrings where the methods
are defined in the code.
