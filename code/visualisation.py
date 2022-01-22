import networkx as nx
import matplotlib.pyplot as plt


class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # function inputs the vertices of an edge
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        color_list = ["white", "black", "white", "black", "white"]
        nx.draw_networkx(G, node_color=color_list, with_labels=True, font_color='limegreen')
        plt.show()


# Driver code
G = GraphVisualization()
G.addEdge('D', 'B')
G.addEdge('B', 'E')
G.addEdge('A', 'E')
G.addEdge('A', 'C')
G.addEdge('C', 'B')

G.visualize()
