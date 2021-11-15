import pytest
import kruskal

def test_kruskal(capfd):
	g=kruskal.Graph(6)
	g.addEdge(0,1,3)
	g.addEdge(1,2,1)
	g.addEdge(2,3,6)
	g.addEdge(3,4,8)
	g.addEdge(4,5,2)
	g.addEdge(4,0,6)
	g.addEdge(5,0,5)
	g.addEdge(5,1,4)
	g.addEdge(5,2,4)
	g.addEdge(5,3,5)

	g.KruskalMST()
	
	out, err = capfd.readouterr()
	
	a="Edges in the constructed MST\n1 -- 2 == 1\n4 -- 5 == 2\n0 -- 1 == 3\n5 -- 1 == 4\n5 -- 3 == 5\nMinimum Spanning Tree 15\n"    
	assert str(out) == a

def test_kruskal1(capfd):
	g = kruskal.Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)
	g.KruskalMST()
	
	out, err = capfd.readouterr()
	
	a="Edges in the constructed MST\n2 -- 3 == 4\n0 -- 3 == 5\n0 -- 1 == 10\nMinimum Spanning Tree 19\n"    
	assert str(out) == a