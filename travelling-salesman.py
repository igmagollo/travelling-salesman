import networkx as nx
import numpy as np

# Loading graph
A = np.loadtxt('ha30/ha30_dist.txt')
G = nx.from_numpy_matrix(A)
file = open('ha30/ha30_name.txt', 'r')
labels = {}
for node in G:
	name = file.readline()
	labels[node] = name[0:-1]
file.close()
G = nx.relabel_nodes(G, labels)

def nearest_neighbor(G, s):
	H = []
	H.append(s)
	while len(H) < len(G):
		minimo = float("Inf")
		for i in G[H[-1]].keys():
			if G[H[-1]][i]['weight'] < minimo and i not in H:
				minimo = G[H[-1]][i]['weight']
				node = i
		H.append(node)
	H.append(s)
	return H


def w(G, lista):
	first = True
	peso = 0
	for i in lista:
		if not first:
			peso = peso + G[ultimo][i]['weight']
		else:
			first = False
		ultimo = i
	return peso


def two_opt(G, s, initial):
	C = initial
	set_i = False
	i = 0
	while i < len(G) - 1:
		if set_i:
			i = 0
			C = Cij
			set_i = False
		j = i + 2
		Cij = C.copy()
		while w(G, Cij) >= w(G, C) and j < len(G):
			a = Cij.pop(j)
			Cij.insert(i+1, a)
			if w(G, Cij) < w(G, C):
				set_i = True
				i = 1
			j = j + 1
		i = i + 1
	return C


for i in range(10):
	print("Partindo de " + labels[i] + ":")
	first = nearest_neighbor(G, labels[i])
	better = two_opt(G, labels[i], first.copy())
	print(better)
	print("Peso = " + str(w(G, better)))
	print("\n")
