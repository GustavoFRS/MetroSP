# Shortest Path Finder Between Metro Stations


## What does the project accomplish?

- This project uses breadth first search and depth first search to return to the user the shortest path between the two stations selected. 
A weighted graph was considered but upon research, it seems like the vast majority of metro stations in Sao Paulo are within ~2 minutes of each other, 
and a graph where all edges have the same weight is of no use.

## How it works?

- The program will ask the user for two inputs, a starting station (vertex) and a destination. 
With those inputs, the shortest path between them is calculated via bfs & dfs, then both possible answers are compared and the shortest one is returned to the user.

## Tecnologies and concepts:
### Python
	Main concepts:
- Graphs
- BFS & DFS search
- Functions
- Conditionals
