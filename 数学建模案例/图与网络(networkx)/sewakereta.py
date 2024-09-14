# hold car at least 1 year max 3 years
# 5 year period

import networkx as nx
import pylab as plt

G=nx.DiGraph()

Rep_cost=[(1,2,4000),(1,3,5400),(1,4,9800),(2,3,4300),(2,4,6200),(2,5,8700),
          (3,4,4800),(3,5,7100),(4,5,4900)]

G.add_nodes_from(range(1,5))
G.add_weighted_edges_from(Rep_cost)

path=nx.shortest_path(G,1,weight='weight')
d=nx.shortest_path_length(G,1,weight='weight')

print('The shortest path towards different nodes: ',path)
print('\nThe shortest length towards different nodes: ',d)

pos=nx.shell_layout(G)
nx.draw(G,pos,with_labels=True,font_weight='bold',node_color='y')
w1=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w1)
plt.show()