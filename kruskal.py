class Graph:

	def __init__(self, vertices):
		self.V = vertices 
		self.graph = [] 



	def addEdge(self, u, v, w):
		self.graph.append([u, v, w])

	
	def find(self, parent, i):
# ********* Insert your code here ************** #
 
# ***********************************************#

	def union(self, parent, rank, x, y):
# ********* Insert your code here ************** #
 
# ***********************************************#
		

	def KruskalMST(self):
# ********* Insert your code here ************** #
 
# ***********************************************#
		minimumCost = 0
		print ("Edges in the constructed MST")
		for u, v, weight in result:
			minimumCost += weight
			print("%d -- %d == %d" % (u, v, weight))
		print("Minimum Spanning Tree" , minimumCost)


def main():
	g = Graph(4)
	g.addEdge(0, 1, 10)
	g.addEdge(0, 2, 6)
	g.addEdge(0, 3, 5)
	g.addEdge(1, 3, 15)
	g.addEdge(2, 3, 4)
	g.KruskalMST()
	

if __name__ == '__main__':
    main()



