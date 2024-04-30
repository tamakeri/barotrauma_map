from pyvis.network import Network
import pyvis._version
import networkx as nx

nx_graph = nx.cycle_graph(10)
nx_graph.nodes[1]['title'] = 'Number 1'
nx_graph.nodes[1]['group'] = 1
nx_graph.nodes[3]['title'] = 'I belong to a different group!'
nx_graph.nodes[3]['group'] = 10
nx_graph.add_node(20, size=20, title='couple', label='2', group=2)
nx_graph.add_node(21, size=15, title='couple', group=2)

nx_graph.add_edge(20, 21, weight=5, title='7', label='5')    ## How to display the label for this edge ?

nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)
nt = Network("500px", "500px", notebook=True)
if pyvis._version.__version__ > '0.1.9':
    nt.from_nx(nx_graph, show_edge_weights=False)
else:
    nt.from_nx(nx_graph)
# nt.show_buttons(filter_=['physics'])
nt.show_buttons()
nt.show("nx.html")