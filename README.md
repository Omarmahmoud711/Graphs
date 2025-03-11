# Graph Algorithm Visualizer

## Overview
This project provides a graphical interface to visualize graph algorithms, specifically **Dijkstra's Algorithm** and **Prim's Minimum Spanning Tree (MST) Algorithm**. The user can input an adjacency matrix, visualize the graph, and run these algorithms to see their outputs.

## How It Works
When you run `GUI.py`, you will be prompted to enter the number of vertices in the graph. A GUI will open, allowing you to enter an adjacency matrix which is the cost of the paths between nodes.

---
## Understanding the Algorithms
### 1.Dijkstra's Algorithm (Shortest Path)
Dijkstra's Algorithm is used to find the shortest path from a starting node to all other nodes in a graph with non-negative edge weights. It uses a priority queue to always expand the least costly path first.

#### Steps:
1. Assign a tentative distance of `∞` (except the start node, which is `0`).
2. Pick the unvisited node with the smallest distance.
3. Update the distances to its neighbors if a shorter path is found.
4. Repeat until all nodes have been visited.

---

### 2.Prim’s Algorithm (Minimum Spanning Tree)
Prim’s Algorithm is used to find a subset of edges that form a tree covering all nodes with the minimum possible total edge weight.

#### Steps:
1. Start with an arbitrary node.
2. Pick the smallest edge that connects a visited node to an unvisited node.
3. Repeat until all nodes are included in the MST.

---

## Example Run
1. **Run** `python main.py`.
2. **Enter the number of vertices** (e.g., `4`).
3. **Fill the adjacency matrix** with values like:
   ```
   0  10  15  0
   10  0  5  20
   15  5  0  30
   0  20  30  0
   ```
#### Directed Graph:
_Images/Directed_Matrix.png_

#### UnDirected Graph:
_(Insert your Dijkstra result images here)_

#### Prims output:
_(Insert your MST result images here)_

#### Dijkstra's output:
_(Insert your MST result images here)_

---

## Notes
- Ensure valid integer inputs for the adjacency matrix.
- The matrix should represent a **weighted graph** with non-negative values.
- The diagonal should be `0` (no self-loops).

---
Enjoy exploring graphs! 🚀

