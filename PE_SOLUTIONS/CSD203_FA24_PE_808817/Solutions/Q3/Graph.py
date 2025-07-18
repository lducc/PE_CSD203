import math
from Stack import *
from MyQueue import *
class Graph:
    def __init__(self,data):
        self.a = data
    def display(self):
        for i in range(len(self.a)):
            for j in range(len(self.a[i])):
                print(self.a[i][j], end =" ")
            print("")
        print("")
    def deg(self, x):
        count =0
        for i in range(len(self.a)):
            count += self.a[x][i]
        return count      
    # end
    
          
    def f1(self,start):  # start is a character       
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 1 ========
        vertex_map = {chr(65 + i): i for i in range(len(self.a))}  
        start_index = vertex_map[start]

        visited = [False] * len(self.a)
        queue = MyQueue()
        queue.EnQueue(start_index)
        visited[start_index] = True

        degrees = []
        traversal_order = []
        odd_degree_vertices = []

        while not queue.isEmpty():
            v = queue.DeQueue()
            vertex_char = chr(65 + v)

            traversal_order.append(vertex_char)

            degree = self.deg(v)
            degrees.append(str(degree))

            if degree % 2 != 0:
                odd_degree_vertices.append(f"{vertex_char}({degree})")
            else:
                odd_degree_vertices.append(vertex_char)

            for i in range(len(self.a)):
                if self.a[v][i] != 0 and not visited[i]:
                    queue.EnQueue(i)
                    visited[i] = True

        print(" ".join(degrees))  
        print(" ".join(traversal_order))  
        print(" ".join(odd_degree_vertices))
    #------------------------------
    
    
    
    def f2(self, fro, to): # fro and to are characters
        # ===YOU CAN EDIT OR EVEN ADD NEW FUNCTIONS IN THE FOLLOWING PART 2 ========
        vertex_map = {chr(65 + i): i for i in range(len(self.a))} 

        start_index = vertex_map[fro]
        end_index = vertex_map[to]

        num_vertices = len(self.a)

        dist = [math.inf] * num_vertices
        dist[start_index] = 0
        prev = [None] * num_vertices
        visited = [False] * num_vertices

        for _ in range(num_vertices):
            min_dist = math.inf
            u = -1
            for i in range(num_vertices):
                if not visited[i] and dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i

            if u == -1:
                break 
            visited[u] = True

            for v in range(num_vertices):
                if self.a[u][v] != 0 and self.a[u][v] != 999: 
                    alt = dist[u] + self.a[u][v]
                    if alt < dist[v]:
                        dist[v] = alt
                        prev[v] = u

        path = []
        u = end_index
        while u is not None:
            path.append(chr(65 + u))  
            u = prev[u]

        print("-".join(path[::-1]))  


        path_with_odd_distances = []

        for vertex in path[::-1]:
            vertex_idx = vertex_map[vertex]

            if dist[vertex_idx] % 2 != 0:
                path_with_odd_distances.append(f"{vertex}{{{dist[vertex_idx]}}}")
            else:
                path_with_odd_distances.append(vertex)

        print("-".join(path_with_odd_distances))

           
    
               
                                     
