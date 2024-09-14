import numpy as np
import pylab as plt
import networkx as nx

# (起点，终点，容量，费用)
L=[('vs','v1',5,5),('vs','v2',4,2),('vs','v3',3,2),('v1','v4',5,2),
   ('v1','v5',3,3),('v2','v5',3,1),('v2','v6',2,2),('v3','v6',2,2),
   ('v4','vt',4,2),('v5','vt',3,3),('v4','vt',5,4)]

G=nx.DiGraph()
node=['vs']+['v'+str(i) for i in range(1,7)]+['vt']

G.add_nodes_from(node);n=len(node)
for k in range(len(L)):
    G.add_edge(L[k][0],L[k][1],capacity=L[k][2],weight=L[k][3])

pos=nx.shell_layout(G)
nx.draw(G,pos,with_labels=True,font_weight='bold',node_color='y')
w1=nx.get_edge_attributes(G,'capacity')
w2=nx.get_edge_attributes(G,'weight')

w1_list=list(w1.values())
w2_list=list(w2.values())
key_list=list(w1)

for i in range(len(w1_list)):
    w1_list[i]=str(w1_list[i])+','+str(w2_list[i])

for i in range(len(w1_list)):
    w1[key_list[i]]=w1_list[i]

nx.draw_networkx_edge_labels(G,pos,edge_labels=w1)
plt.show()

mincost_flow=nx.max_flow_min_cost(G,'vs','vt')
print('maxflow = ',mincost_flow)
min_cost=nx.cost_of_flow(G,mincost_flow)
print('mincost = ',min_cost)

flow_mat=np.zeros((n,n))
for i,adj in mincost_flow.items():
    for j,f in adj.items():
        flow_mat[node.index(i),node.index(j)]=f

print('maxflow capacity = ',sum(flow_mat[:,-1]))
print('mincost maxflow = \n',flow_mat)