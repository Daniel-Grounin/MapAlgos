import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = ox.load_graphml('maps/beersheba.graphml')

source_address = input("Enter the source address: ")
destination_address = input("Enter the destination address: ")

orig_point = ox.geocode(source_address)
dest_point = ox.geocode(destination_address)

orig_node = ox.distance.nearest_nodes(G, X=orig_point[1], Y=orig_point[0])
dest_node = ox.distance.nearest_nodes(G, X=dest_point[1], Y=dest_point[0])

fig, ax = plt.subplots(figsize=(10, 10))
ox.plot_graph(G, ax=ax, node_size=0, edge_color='#333333', show=False, close=False, bgcolor='black')
lines = []

dijkstra_paths = []
for path in nx.single_source_dijkstra_path(G, orig_node, weight='length').values():
    dijkstra_paths.append(path)
    if path[-1] == dest_node:
        break


def init():
    return lines


def update(frame):
    current_path = dijkstra_paths[frame]
    x = [G.nodes[node]['x'] for node in current_path]
    y = [G.nodes[node]['y'] for node in current_path]
    line, = ax.plot(x, y, lw=2, color='red', alpha=0.6)
    lines.append(line)
    return lines


ani = animation.FuncAnimation(fig, update, frames=len(dijkstra_paths),
                              init_func=init, blit=True, interval=200, repeat=False)

# Save the animation as a GIF
ani.save('dijkstra_animation.gif', writer='imagemagick', fps=5)
# Save the animation as a video
# ani.save('dijkstra_animation.mp4', writer='ffmpeg', fps=5)

plt.show()
