from typing import List
import sys 

class DijkstrasAlgorithm:

    def __init__(self, adjacency_matrix: List[List[int]], start_vertex: int) -> None:
        self.adjacency_matrix = adjacency_matrix
        self.start_vertex = start_vertex
        self.v = len(adjacency_matrix)
        self.visited = [False for _ in range(len(adjacency_matrix))]
        self.distances = [float('inf') for _ in range(len(adjacency_matrix))]
        self.labels = [chr(97 + i) for i in range(len(adjacency_matrix))]
        self.distances[start_vertex] = 0 

    def get_min_vertex(self): 
        '''gets the minimum vertex distance.'''
        min_vertex_value = sys.maxsize
        min_vertex_index = 0 

        # Linear search in O(n) this is why to use heap data structure instead - O(log*N)
        for index in range(self.v):
            if (not self.visited[index] and self.distances[index] < min_vertex_value):
                min_vertex_value = self.distances[index] 
                min_vertex_index = index 

        return min_vertex_index
    
    def calculate(self):
        '''calculates the shortest path using Dijkstra's algorithm'''
        for vertex in range(self.v):
            actual_vertex = self.get_min_vertex() 
            print('Considering vertex %s' % self.labels[actual_vertex]) 
            self.visited[actual_vertex] = True 

            # it has O(V) running time 
            for other_vertex in range (self.v): 
                # if there is a connection between the two nodes 
                if (self.adjacency_matrix[actual_vertex][other_vertex] > 0):
                    # is there a shorter path to the other_vertex from the actual vertex
                    if (self.distances[actual_vertex] + 
                        self.adjacency_matrix[actual_vertex][other_vertex] < 
                        self.distances[other_vertex]):
                        self.distances[other_vertex] = self.distances[actual_vertex] + \
                        self.adjacency_matrix[actual_vertex][other_vertex]

    def print_distances(self):
        '''prints the shortest path distances'''
        print(self.distances)
        print(self.labels)

if __name__ == '__main__': 
    print("Dijkstra's Algorithm with the help of adjacency matrix")

    graph = [
        [0, 7, 5, 2, 0, 0],
        [7, 0, 0, 0, 3, 0],
        [5, 0, 0, 10, 4, 0],
        [2, 0, 10, 0, 0, 2],
        [0, 3, 4, 0, 0, 6],
        [0, 8, 0, 2, 6, 0],
    ]

    algorithm = DijkstrasAlgorithm(graph, 2) 
    algorithm.calculate() 
    algorithm.print_distances()