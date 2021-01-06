import networkx as nx
import matplotlib.pyplot as plt

import read_data

bands_d = read_data.read_bands()
band_members_df = read_data.read_members()

band_nodes = bands_df['musical_group'].tolist()
band_member_nodes = band_members_df['human'].tolist()

G = nx.Graph()

G.add_nodes_from(band_nodes, node_class='band', color='green')
G.add_nodes_from(band_member_nodes, node_class='band_member', color='red')

edges = []
edges.extend([(row['human'], row['member_of']) for _, row in band_members_df.iterrows()])
edges.extend([(row['musical_group'], row['has_part']) for _, row in bands_df.iterrows()])

G.add_edges_from(edges)

color_map = []

for node in list(G.nodes(data='color')):
    if node[1] is not None:
        color_map.append(node[1])
    else:
        color_map.append('black')

nx.write_graphml(G, '/Users/jordanmiles/Desktop/musicians.graphml')
# options = {
#     'node_size': 25,
#     'width': 3,
#     'node_color': color_map
# }
# plt.subplot(121)
# nx.draw(G, **options)
# plt.show()

