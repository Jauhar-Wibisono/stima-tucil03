from Graph import *

g = Graph()
g.addNode(("0", 0,0))
g.addNode(("1", 0,1))
g.addNode(("2", 0,2))
g.addNode(("3", 0,3))
g.addNode(("4", 1,0))
g.addNode(("5", 1,1))
g.addNode(("6", 1,2))
g.addNode(("7", 1,3))
g.addNode(("8", 2,0))
g.addNode(("9", 2,1))
g.addNode(("10", 2,2))
g.addNode(("11", 2,3))
g.addNode(("12", 3,0))
g.addNode(("13", 3,1))
g.addNode(("14", 3,2))
g.addNode(("15", 3,3))

g.addEdgebyID(0,8)
g.addEdgebyID(1,11)
g.addEdgebyID(7,2)
g.addEdgebyID(0,14)
g.addEdgebyID(14,7)
g.addEdgebyID(2,12)
g.addEdgebyID(12,15)
g.addEdge("13","15")
g.addEdgebyID(6,8)
g.addEdgebyID(13,6)
g.addEdgebyID(3,0)
g.addEdgebyID(3,11)
print(g.adjacencyList())
print(g.edgeList())
print(g.AstarbyID(0,15,True)["distance"])
print(g.AstarbyID(0,9,False))