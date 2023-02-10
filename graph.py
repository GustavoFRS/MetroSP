from lines import *

graph = {}

def add_vertex(vertex):
    if vertex not in graph:
        graph[vertex] = []

def add_edge(vertex1, vertex2):
    if vertex1 in graph and vertex2 in graph:
        if vertex2 not in graph[vertex1]:
            graph[vertex1].append(vertex2)
 
# Adding vertexes
for line in lines:
    for station in lines[line]:
        add_vertex(station)

# Adding Edges
for line in lines:
    for station in lines[line]:
        # Deal with extremities first
        if lines[line].index(station) == 0:
            add_edge(station, lines[line][1])
        elif lines[line].index(station) == len(lines[line]) - 1:
            add_edge(station, lines[line][len(lines[line]) - 2])
        # Every other vertex will have at least two neighbors
        else:
            add_edge(station, lines[line][lines[line].index(station) - 1])
            add_edge(station, lines[line][lines[line].index(station) + 1])



#print(graph)