from dimacs import *

def union(x, y, p):
	a = find(x, p)
	b = find(y, p)

	if(a!=b):
		p[a] = b

def find(x, p):
	if(p[x] != x):
		v = p[x]
		p[x]=find(v, p)
		return p[x]
	else:
		return x

def run(V, L):
	L_s = [(c, x, y) for (x,y,c) in L]
	L_s.sort(reverse=True)

	s = 1
	t = 2

	p = {i:i for i in range(1, V+1)}

	m = -1
	for (c, x, y) in L_s:

		union(x, y, p)
		
		if(find(s, p) == find(t, p)):
			m=c
			break

	return m

(V, L) = loadWeightedGraph("clique5")
res = run(V, L)
print(res)