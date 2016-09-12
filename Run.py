# -*- coding: UTF-8 -*-

from Graph import Graph
from Computations import CoreDecomposition, MCD
from NodeInsertion import NodeInsertion
from NodeRemoval import NodeRemoval
from EdgeInsertion import EdgeInsertion
from EdgeRemoval import EdgeRemoval

if __name__ == '__main__':
	# Network G
	G = Graph()
	core = {}
	kOrder = []
	kOrder.append([])
	# TODO kOrder also changes during NodeInsertion
	G, core, kOrder = NodeInsertion(G, 2, core, kOrder)
	G, core, kOrder = NodeInsertion(G, 1, core, kOrder)
	G, core, kOrder = NodeInsertion(G, 3, core, kOrder)
	G, core, kOrder = NodeInsertion(G, 4, core, kOrder)
	
	core, kOrder = CoreDecomposition(G)
	mcd = MCD(G, core)
	
	G, core, kOrder = NodeRemoval(G, 3, core, kOrder, mcd)
	
	G, core, kOrder = EdgeInsertion(G, 1, 4, core, kOrder)
	G, core, kOrder = EdgeInsertion(G, 1, 2, core, kOrder)
	
	G, core, kOrder, mcd = EdgeRemoval(G, 1, 4, core, kOrder, mcd)
	
	G, core, kOrder = NodeInsertion(G, 3, core, kOrder)
	
	G, core, kOrder = EdgeInsertion(G, 1, 3, core, kOrder)
	G, core, kOrder = EdgeInsertion(G, 2, 3, core, kOrder)
	
	G, core, kOrder = NodeInsertion(G, 5, core, kOrder)
	
	G, core, kOrder = EdgeInsertion(G, 5, 4, core, kOrder)
	G, core, kOrder = EdgeInsertion(G, 3, 4, core, kOrder)
	print core	
	
	print ""
	#mcd = MCD(G, core)
	#G, core, kOrder, mcd = EdgeRemoval(G, 1, 3, core, kOrder, mcd)
	core, kOrder = CoreDecomposition(G)
	print core, kOrder
	print G
	print "Finished"
	
	# TODO update core, mcd, ... - delete removed nodes