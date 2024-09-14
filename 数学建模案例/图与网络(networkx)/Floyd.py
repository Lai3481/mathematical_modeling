import networkx as nx
import pylab as plt
import numpy as np

G=nx.Graph()
List=[(0,1,2),(0,2,1),(0,3,8),(1,3,6),(1,4,1),
      (2,3,7),(2,6,9),(3,4,5),(3,5,1),(3,6,2),
      (4,5,3),(4,7,9),(5,6,4),(5,7,6),(6,7,3)]
G.add_nodes_from(range(0,7))
G.add_weighted_edges_from(List)

d=nx.floyd_warshall_numpy(G) #矩阵
# floyd算法
print(f"最短距离矩阵为：\n{d}")
path=nx.shortest_path(G,weight='weight',method='bellman-ford') #路径
for i in range(0,len(d)):
    for j in range(i+1,len(d)):
        print(f"顶点{i}到顶点{j}的最短路径为：{path[i][j]}")