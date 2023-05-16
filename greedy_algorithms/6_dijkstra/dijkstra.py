"""
Compute shortest path of all the nodes/vertices of a graph from a particular node/vertex

Initial Step:
- Maintain an array of distances D[v] where v = number of vertices
- Mantain an array of the visited vertices v[]
- Select a vertex. This will be the starting vertex
- Initialize the distance array with the maximum possible value
- Update the distance of the selected vertex from 0
- Update the distances of its neighbors according to their respective edge costs

Repeating step:
- Select the neighbor with the shortes path from the current vertex
- Update current vertex
- Add the previous vertex to the visited array v[]
- For all the neighbors of the current vertex, check wheter D[current_vertex] + cost[current_vertex, neighbour] < D[neighbor]. This is the relaxation step
- Repeat untill all vertices are visited.
"""
print('Dijkstra')