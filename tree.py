import networkx as nx
from matplotlib import pyplot as plt, animation

fig = plt.figure()
from networkx.drawing.nx_pydot import graphviz_layout

G = nx.DiGraph()
i = int(0)

nodes = [
    ["repeat","repeat"],                #0
    ["id","x"],                         #1
    [":=",":="],                        #2
    ["id","y"],                         #3
    [";",";"],                          #4
    ["until","until"],                  #5
    ["id","z"],                         #6
    ["factor","factor"],                #7
    ["assign-stmt","assign-stmt"],      #8
    ["statement","statement"],          #9
    ["smt-seq","semt-seq"],             #10
    ["repeat-stmt","repeat-stmt"],      #11
    ["statement","statement"],          #12
    ["stmt-seq","stmt-seq"],            #13
    ["stmt-seq'","stmt-seq'"]           #14
]
""""
[1, [0], [], ['repeat', 'identifier', ':=', 'identifier', ';', 'until', 'identifier', '$'], 's5']
[2, [0, 5], ['repeat'], ['identifier', ':=', 'identifier', ';', 'until', 'identifier', '$'], 's6']
[3, [0, 5, 6], ['repeat', 'identifier'], [':=', 'identifier', ';', 'until', 'identifier', '$'], 's9']
[4, [0, 5, 6, 9], ['repeat', 'identifier', ':='], ['identifier', ';', 'until', 'identifier', '$'], 's12']
[5, [0, 5, 6, 9, 12], ['repeat', 'identifier', ':=', 'identifier'], [';', 'until', 'identifier', '$'], 'r8']
[6, [0, 5, 6, 9, 11], ['repeat', 'identifier', ':=', 'factor'], [';', 'until', 'identifier', '$'], 's15']
[7, [0, 5, 6, 9, 11, 15], ['repeat', 'identifier', ':=', 'factor', ';'], ['until', 'identifier', '$'], 'r7']
[8, [0, 5, 4], ['repeat', 'assign-stmt'], ['until', 'identifier', '$'], 'r5']
[9, [0, 5, 2], ['repeat', 'statement'], ['until', 'identifier', '$'], 'r3']
[10, [0, 5, 8], ['repeat', 'stmt-seq'], ['until', 'identifier', '$'], 's10']
[11, [0, 5, 8, 10], ['repeat', 'stmt-seq', 'until'], ['identifier', '$'], 's14']
[12, [0, 5, 8, 10, 14], ['repeat', 'stmt-seq', 'until', 'identifier'], ['$'], 'r6']
[13, [0, 3], ['repeat-stmt'], ['$'], 'r4']
[14, [0, 2], ['statement'], ['$'], 'r3']
[15, [0, 1], ['stmt-seq'], ['$'], 'acc']
"""
root_node = 0
def tree_root(root):
    global root_node
    #G.add_node(root,label = nodes[root][1])
    root_node = root


def tree_add(children,parent):
    G.add_node(parent,label = nodes[parent][1], ordering = "out")

    for child in children:
        G.add_node(child, label = nodes[child][1])
        G.add_edge(parent,child)        #see if reversing this makes a difference



def draw():
    positions = graphviz_layout(G, prog="dot", root=root_node)
    nx.draw(G, pos=positions,labels = nx.get_node_attributes(G,"label"), with_labels=True, node_color="White",
            node_size = 1000,node_shape='s',edgecolors=None,arrowstyle='-')


tree_add([3], 7)
tree_add([1, 2, 7, 4], 8)
tree_add([8], 9)
tree_add([9], 10)
tree_add([0, 10, 5, 6], 11)
tree_add([11], 12)
tree_add([12], 13)

# after accept
tree_add([13], 14)
tree_root(14)

draw()
figmanager = plt.get_current_fig_manager()
figmanager.window.showMaximized()
fig.canvas.manager.set_window_title("Parse Tree")
plt.show()