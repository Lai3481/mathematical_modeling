import networkx as nx
import pylab as plt

# # 无向图
# G=nx.graph()
# # 有向图
# G=nx.DiGraph()
# # 多重无向图
# G=nx.MultiGraph()
# # 多重有向图
# G=nx.MultiDiGraph()

# 随机图
ER=nx.random_graphs.erdos_renyi_graph(10,0.3) #10个节点以0.3概率连接
pos=nx.shell_layout(ER) 
# pos为字典=坐标数据
# shell_layout在多个同心圆分布
# circular_layout 在一个圆环
# random_layout 随机

s=[str(i) for i in range(1,11)]
s=dict(zip(range(10),s))
nx.draw(ER,pos,labels=s);plt.show()

