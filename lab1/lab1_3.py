from dimacs import *
import heapq

def run(V, L):
	L_s = [(c, x, y) for (x,y,c) in L]
	L_s.sort(reverse=True)

	neighbor_list = [[] for i in range(V+1)]

	q = []

	heapq.heapify(q)

	for (x,y,c) in L:
		neighbor_list[x].append((y, c))
		neighbor_list[y].append((x, c))


	s = 1
	t = 2

	d = [-1000000000 for i in range(V+1)]

	d[s] = 100000000000

	heapq.heappush(q, (-d[s], s))

	while(len(q) != 0):
		p = heapq.heappop(q)

		p, v = p
		p = -p

		for (i, c) in neighbor_list[v]:
			if d[i] < min(c, p):
				d[i] = min(c, p)
				heapq.heappush(q, (-d[i], i))

	return d[t]

(V, L) = loadWeightedGraph("clique5")
res = run(V, L)
print(res)
