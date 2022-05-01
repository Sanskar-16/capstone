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
        # color_list = ["black","black","black","black",]
        color_list = ["blue", "red", "red", "red", "blue"]
        nx.draw_networkx(G, node_color=color_list, node_size=400, alpha=0.9, with_labels=True,
                         font_color='white')
        plt.show()


# Driver code
G = GraphVisualization()
G.addEdge('A', 'C')
G.addEdge('A', 'D')
G.addEdge('A', 'E')
G.addEdge('B', 'C')
G.addEdge('B', 'D')
G.addEdge('B', 'E')



G.visualize()
