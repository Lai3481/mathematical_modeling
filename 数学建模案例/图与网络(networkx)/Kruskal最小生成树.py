import networkx as nx
import pylab as plt
import numpy as np

G=nx.Graph()
List=[(0,1,2),(0,2,1),(0,3,8),(1,3,6),(1,4,1),
      (2,3,7),(2,6,9),(3,4,5),(3,5,1),(3,6,2),
      (4,5,3),(4,7,9),(5,6,4),(5,7,6),(6,7,3)]

G.add_weighted_edges_from(List)

T=nx.minimum_spanning_tree(G,algorithm="kruskal")
c=nx.to_numpy_array(T) #返回邻接矩阵
print("邻接矩阵：\n",c)

w1=c.sum()/2 #权重
print("最小生成树权重：",w1)

pos=nx.circular_layout(G)
key=range(8);s=['v'+ str(i) for i in key]
s=dict(zip(key,s))
# 顶点字符字典

nx.draw(T,pos,labels=s,font_weight='bold')
w2=nx.get_edge_attributes(T,'weight')
nx.draw_networkx_edge_labels(T,pos,edge_labels=w2)
plt.show()
