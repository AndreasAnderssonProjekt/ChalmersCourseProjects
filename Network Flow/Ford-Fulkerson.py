import math

class Network_Flow:
    def __init__(self, network, s, t):
        assert self.is_valid_network(network, s, t)
        self.network = network  # Residual Network.
        self.source = s
        self.sink = t

    # Make sure there are no incoming edges to source node and no outgoing edges from sink.
    def is_valid_network(self, network, s, t):
        n = len(network)
        for i in range(len(network)):
            if network[i][s] != 0:
                return False

            if network[t][i] != 0:
                return False
        return True


    def Ford_Fulkerson(self):
        path = []
        max_flow = 0

        while self.BFS(path):
            b = self.bottleneck(path)
            for i in range(len(path) - 1):
                u = path[i]
                v = path[i + 1]
                # Update Residual graph.
                self.network[u][v] -= b  # Remaining capacity from node u to v decreases by b flow units.
                self.network[v][u] += b  # An additional b flow units can be pushed back from node u.

                if u == self.source:  # Increase max_flow when we push b units from the source node.
                    max_flow += b

                if v == self.source:  # Decrease max_flow when we push b units back to the source node.
                    max_flow -= b
            path = []

        return max_flow


    def bottleneck(self, path):
        b = math.inf
        for i in range(len(path)-1):
            u = path[i]
            v = path[i+1]
            if self.network[u][v] < b:
                b = self.network[u][v]
        return b



    # Return False if there is no simple s-t path in the network, else return one s-t path.
    def BFS(self, path):
        n = len(self.network)
        queue = [self.source]
        visited = [False for i in range(n)]
        visited[self.source] = True
        prev = [None for i in range(n)]
        while queue:
            v = queue.pop(0)
            for u in range(n):
                if self.network[v][u] != 0 and not visited[u]:
                    queue.append(u)
                    visited[u] = True
                    prev[u] = v

        if not visited[-1]:
            return False


        curr = self.sink
        while True:
            path.append(curr)
            if curr == self.source:
                break
            curr = prev[curr]

        path.reverse()
        return True


network = [[0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]]

n = Network_Flow(network, s = 0, t = len(network)-1)
print(n.Ford_Fulkerson()
