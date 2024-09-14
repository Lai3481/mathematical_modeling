import numpy as np
import pylab as plt
import networkx as nx

L=[('s','v1',8),('s','v3',7),('v1','v2',9),('v1','v3',5),
   ('v2','t',5),('v2','v3',2),('v3','v4',9),('v4','v2',6),
   ('v4','t',10)]

G=nx.DiGraph()
node=['s']+['v'+str(i) for i in range(1,5)]+['t']

G.add_nodes_from(node);n=len(node)
G.add_weighted_edges_from(L)
value,flow_dir=nx.maximum_flow(G,'s','t',capacity='weight')

pos=nx.shell_layout(G)
nx.draw(G,pos,with_labels=True,font_weight='bold',node_color='y')
w1=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w1)
plt.show()

print(value);print(flow_dir)
A=np.zeros((n,n))

for i,adj in flow_dir.items():
    for j,f in adj.items():
        A[node.index(i),node.index(j)]=f

print(A) #最大流邻接矩阵