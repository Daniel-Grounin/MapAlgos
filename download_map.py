import os
import osmnx as ox

G = ox.graph_from_place('Beersheba, Israel', network_type='drive')

# save the map in maps folder, if map folder doesn't exist, create it
if not os.path.exists('maps'):
    os.makedirs('maps')

ox.save_graphml(G, filepath='maps/beersheba.graphml')

print("Map data downloaded and saved as beersheba.graphml")
