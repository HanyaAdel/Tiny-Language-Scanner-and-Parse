import networkx as nx
import matplotlib.pyplot as plt

node = 'A'

s1 = 'repeat until'

G = nx.DiGraph()

positions = {
    'A': [0, 0],
    'B': [20, 0],
    'C': [40, 0],
    'D': [60, 0],
    'E': [80, 0],
    'F': [100, 0],
    'G': [120, 0],
}


def add_node():
    global node
    G.add_node(node)
    node = chr(ord(node) + 1)


def add_edge(a, b, c):
    G.add_edge(a, b, relation=c)


def draw_graph():
    pos = nx.spectral_layout(G)
    nx.draw_networkx(G, pos, with_labels=True, node_size=300, node_color='cyan')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'relation'), font_size=10)
    plt.show()


for i in range(len(s1)):
    add_node()

temp = 'A'

for i in range(len(s1)):
    add_edge(temp, chr(ord(temp) + 1), s1[i])
    temp = chr(ord(temp) + 1)

draw_graph()
