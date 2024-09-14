import networkx as nx
import pylab as plt
import numpy as np

G=nx.DiGraph()
List=[(1,2,2),(2,4,3),(3,2,8),(4,3,5),(4,1,7)]
# 坐标数据
# （起点，终点，权量）

G.add_nodes_from(range(1,5)) #生成节点
G.add_weighted_edges_from(List) #生成边
pos=nx.shell_layout(G)

nx.draw(G,pos,with_labels=True,font_weight='bold',node_color='y')
#设置图需

w1=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=w1)
w2=nx.to_numpy_array(G)
# 导出邻接矩阵 ，to_numpy_matrix已升级成array

print(w2)
plt.show()