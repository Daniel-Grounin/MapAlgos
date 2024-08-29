import os

import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
from concurrent.futures import ThreadPoolExecutor

G = ox.load_graphml('beersheba.graphml')

source_address = input("Enter the source address: ")
destination_address = input("Enter the destination address: ")

orig_point = ox.geocode(source_address)
dest_point = ox.geocode(destination_address)

orig_node = ox.distance.nearest_nodes(G, X=orig_point[1], Y=orig_point[0])
dest_node = ox.distance.nearest_nodes(G, X=dest_point[1], Y=dest_point[0])

def calculate_shortest_path():
    return nx.shortest_path(G, orig_node, dest_node, weight='length')

with ThreadPoolExecutor() as executor:
    future = executor.submit(calculate_shortest_path)
    shortest_path = future.result()

fig, ax = plt.subplots(figsize=(10, 10))
ox.plot_graph(G, ax=ax, node_size=0, edge_color='#333333', show=False, close=False, bgcolor='black')

x = [G.nodes[node]['x'] for node in shortest_path]
y = [G.nodes[node]['y'] for node in shortest_path]
ax.plot(x, y, lw=3, color='cyan', alpha=0.8)

ax.scatter([orig_point[1]], [orig_point[0]], s=100, c='yellow', edgecolor='black', zorder=5)
ax.scatter([dest_point[1]], [dest_point[0]], s=100, c='yellow', edgecolor='black', zorder=5)

# save in a directory, if it doesn't exist, create it
if not os.path.exists('images'):
    os.makedirs('images')

plt.savefig(f'images/{source_address}_{destination_address}.png', bbox_inches='tight', pad_inches=0.1)

plt.show()
