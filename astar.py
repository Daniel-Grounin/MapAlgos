import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from heapq import heappush, heappop

def heuristic(G, n1, n2):
    x1, y1 = G.nodes[n1]['x'], G.nodes[n1]['y']
    x2, y2 = G.nodes[n2]['x'], G.nodes[n2]['y']
    return ox.distance.great_circle(y1, x1, y2, x2)

# A* algorithm implementation with path visualization frames
def a_star_algorithm(G, orig, dest):
    open_set = []
    heappush(open_set, (0, orig))
    g_cost = {orig: 0}
    came_from = {orig: None}
    frames = []

    while open_set:
        current = heappop(open_set)[1]

        if current == dest:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            frames.append(path[::-1])
            return path[::-1], frames

        for neighbor in G.neighbors(current):
            tentative_g_score = g_cost[current] + G.edges[current, neighbor, 0]['length']
            if neighbor not in g_cost or tentative_g_score < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(G, neighbor, dest)
                heappush(open_set, (f_score, neighbor))
                came_from[neighbor] = current

        frames.append(list(came_from.keys()))

    return None, frames

def update(num, G, path_data, line):
    line.set_data([G.nodes[node]['x'] for node in path_data[num]],
                  [G.nodes[node]['y'] for node in path_data[num]])
    return line,

def main():
    G = ox.graph_from_place('Beersheba, Israel', network_type='drive')

    source_address = input("Enter the source address (e.g., 'David Tuviyahu St 6, Beersheba, Israel'): ")
    destination_address = input("Enter the destination address (e.g., 'Ben Gurion St 36, Beersheba, Israel'): ")

    orig_point = ox.geocode(source_address)
    dest_point = ox.geocode(destination_address)

    orig_node = ox.distance.nearest_nodes(G, X=orig_point[1], Y=orig_point[0])
    dest_node = ox.distance.nearest_nodes(G, X=dest_point[1], Y=dest_point[0])

    path, frames = a_star_algorithm(G, orig_node, dest_node)

    fig, ax = ox.plot_graph(
        G,
        bgcolor='white',
        node_color='black',
        edge_color='black',
        node_size=0,
        edge_linewidth=0.5,
        show=False, close=False
    )
    line, = ax.plot([], [], lw=2, color='yellow')

    ani = animation.FuncAnimation(fig, update, frames=len(frames), fargs=(G, frames, line),
                                  interval=200, blit=True)

    ani.save('a_star_pathfinding.mp4', writer='ffmpeg', fps=10)

    plt.show()

if __name__ == "__main__":
    main()
