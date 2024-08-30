# Dijkstra Pathfinding Visualization

This project provides a visualization of Dijkstra's algorithm on a map of a city, specifically Beersheba. It allows users to input source and destination addresses and either visualize the entire shortest path immediately or observe how Dijkstra's algorithm traverses the nodes step by step.

## Project Overview

- **Visualize Shortest Path:** See the shortest path between two addresses in its final form.
- **Observe Dijkstra's Algorithm:** Watch as Dijkstra's algorithm works its way through the graph, exploring different paths until it finds the shortest route.

## Requirements

- Python 3.x+
- Required Python packages (install using `pip install -r requirements.txt`):
  - `osmnx`
  - `networkx`
  - `matplotlib`

## Setup Instructions

### 1. Clone the Project

First, clone this repository to your local machine:

### 2. Download Your Desired Map
Before running the visualization scripts, you need to download the desired map in the form of a .graphml file. You can do this using the download_map.py script.

Run the following command to download the map of your chosen location:

```python download_map.py```

This will download the map and save it as beersheba.graphml in the project directory by default. If you need a different location, modify the script to download the specific area you need.

### 3. Choose Visualization Mode
You have two main options for visualizing the paths:

3.1 Visualize the Shortest Path (Final Form)
To see the shortest path between two addresses immediately, run:

```python dijkstra_path.py```


This will prompt you to enter the source and destination addresses, and then it will calculate and display the shortest path on the map.

3.2 Observe Dijkstra's Algorithm in Action
To watch how Dijkstra's algorithm works step by step, run:

```python main.py```

This script will prompt you to enter the source and destination addresses and then visualize how the algorithm explores different paths until it finds the shortest one.
