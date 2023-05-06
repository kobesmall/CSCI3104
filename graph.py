



class Graph():

    def __init__(self, adjacency_matrix):
        """ 
        Graph initialized with a weighted adjacency matrix 
        
        Attributes
        ----------
        adjacency_matrix : 2D array
            non-negative integers where adjacency_matrix[i][j] is the weight of the edge i to j,
            with 0 representing no edge

        """

        self.adjacency_matrix = adjacency_matrix

        # Add more class variables below as needed, such as n:
        self.N = len(adjacency_matrix)
        #self.tGraph = [[0 for col in range (self.N)] for row in range (self.N)]

    
    def Prim(self):
        """
        Use Prim-Jarnik's algorithm to find the length of the minimum spanning tree starting from node 0

        Returns
        -------
        int
            Weighted length of tree

        """
        k = [float('inf')] * self.N
        tree = [None] * self.N
        k[0] = 0
        track = [False] * self.N
        tree[0] = -1

        for e in range (self.N):
            minV = self.minVrt(k,track)


            track[minV] = True

            for n in range(self.N):
                if self.adjacency_matrix[minV][n] > 0 and track[n] == False and k[n] > self.adjacency_matrix[minV][n]:
                    k[n] = self.adjacency_matrix[minV][n]
                    tree[n] = n
            
            ans = 0
            for i in range(len(k)):
                ans += k[i]
        

        #print(k)
        #print(tree)
        #print(track)
        #print(self.adjacency_matrix)

        return ans

    def minVrt(self, k, track):
        min = float('inf')
        minI = 0 

        for x in range(self.N):
            if k[x] < min and track[x] == False:
                min = k[x]
                minI = x

        return minI

#  Example use case:

#G = Graph([[0, 10, 11, 33, 60],
#         [10, 0, 22, 14, 57],
#          [11, 22, 0, 11, 17],
#           [33, 14, 11, 0, 9],
#           [60, 57, 17, 9, 0]])
#print("tt")
#Tr = Graph([[0,3,3],[3,0,3],[3,3,0]])
#assert Tr.Prim() == 6
#print(Tr.Prim())

#print(G.Prim())
#assert G.Prim() == 41