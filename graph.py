import networkx as nx
from matplotlib import pyplot as plt, animation

fig = plt.figure()
node_dict = {
    "start": 0,
    "inrepeat": 1,
    "inid": 2,
    "inassign": 3,
    "finishedassign": 4,
    "finishedstatement": 5,
    "inuntil": 6,
    "infirstoperand": 7,
    "incomp": 8,
    "finished": 9,
    "error": 10
}
positions = {
    "start": [0, 100],
    "inrepeat": [1, 90],
    "inid": [2.5, 85],
    "inassign": [4, 80],
    "finished\nassign": [5, 70],
    "finished\nstatement": [5.5, 55],
    "inuntil": [6, 40],
    "infirst\noperand": [7, 30],
    "incomp": [8, 20],
    "finished": [9, 10],
    "dead": [7, 100]
}
G = nx.DiGraph()
G.add_nodes_from(
    ["start", "inrepeat", "inid", "inassign", "finished\nassign", "finished\nstatement", "inuntil", "infirst\noperand",
     "incomp", "finished", "dead"])

G.add_edge("start", "inrepeat", label="repeat")
G.add_edge("inrepeat", "inid", label="ID")
G.add_edge("inrepeat", "inuntil", label="until")
G.add_edge("inid", "inassign", label=":=")
G.add_edge("inassign", "finished\nassign", label="ID,NUM")
G.add_edge("finished\nassign", "finished\nstatement", label=";")
G.add_edge("finished\nstatement", "inid", label="ID")
G.add_edge("finished\nstatement", "inuntil", label="until")
G.add_edge("inuntil", "infirst\noperand", label="ID,NUM")
G.add_edge("infirst\noperand", "incomp", label="COMP")
G.add_edge("incomp", "finished", label="ID,NUM")
G.add_edge("start", "dead", label="other")
G.add_edge("inrepeat", "dead", label="other")
G.add_edge("inid", "dead", label="other")
G.add_edge("inassign", "dead", label="other")
G.add_edge("finished\nassign", "dead", label="other")
G.add_edge("finished\nstatement", "dead", label="other")
G.add_edge("inuntil", "dead", label="other")
G.add_edge("infirst\noperand", "dead", label="other")
G.add_edge("incomp", "dead", label="other")
G.add_edge("finished", "dead", label="other")

i = int(-1)
s = []
ani = 0
color_map = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', '#34eb40', 'white']


def animate(frame):
    global i
    global s
    color_map = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', '#34eb40', 'white']
    fig.clear()
    color_map[node_dict[s[i]]] = 'red'
    i += 1

    nx.draw(G, positions, node_size=4000, with_labels=True, node_color=color_map, edgecolors="black")
    nx.draw_networkx_edge_labels(G, positions, edge_labels=nx.get_edge_attributes(G, 'label'), font_size=10,
                                 rotate=False)


class Graph:

    def __init__(self, state):
        global s, ani, color_map, fig,i
        i = int(-1)
        s = state
        print(s)
        nx.draw(G, positions, node_size=4000, with_labels=True, node_color=color_map, edgecolors="black")
        ani = animation.FuncAnimation(fig, animate, frames=len(s), interval=700, repeat=False)
        nx.draw_networkx_edge_labels(G, positions, edge_labels=nx.get_edge_attributes(G, 'label'), font_size=10,
                                     rotate=False)

        figmanager = plt.get_current_fig_manager()
        figmanager.window.showMaximized()
        fig.canvas.manager.set_window_title("DFA")
        plt.show()
