import networkx as nx
import pylab as plt
import numpy as np

G=nx.Graph()
List=[(0,1,2),(0,2,1),(0,3,8),(1,3,6),(1,4,1),
      (2,3,7),(2,6,9),(3,4,5),(3,5,1),(3,6,2),
      (4,5,3),(4,7,9),(5,6,4),(5,7,6),(6,7,3)]
# 数据
G.add_nodes_from(range(0,7))
G.add_weighted_edges_from(List)
path=nx.shortest_path(G,0,weight='weight')
# 从0点开始
d=nx.shortest_path_length(G,0,weight='weight')
for i in range(0,8):
    print(f"顶点0到顶点{i}的最短路径为：{path[i]}")

# 图
G2=nx.Graph()
List2=[(0,1,2),(0,2,1),(1,4,1),(3,5,1),(3,6,2),(4,5,3),(4,7,9)]
G2.add_nodes_from(range(0,7)) #生成节点
G2.add_weighted_edges_from(List2) #生成边
pos=nx.shell_layout(G2)
nx.draw(G2,pos,with_labels=True,font_weight='bold',node_color='y')
w1=nx.get_edge_attributes(G2,'weight')
nx.draw_networkx_edge_labels(G2,pos,edge_labels=w1)
plt.show()