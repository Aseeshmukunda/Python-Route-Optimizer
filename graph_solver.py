import math

class Graph:
    """Represents a set of locations and distances between them."""
    def __init__(self, nodes):
        # nodes is a dictionary: {id: (latitude, longitude)}
        self.nodes = nodes
        # adj is an adjacency list: {node_id: {neighbor_id: distance}}
        self.adj = {node_id: {} for node_id in nodes}
        self._build_edges()

    def _haversine_distance(self, coord1, coord2):
        """Calculates the distance between two points on the Earth (Haversine formula)."""
        R = 6371  # Earth radius in kilometers
        lat1, lon1 = math.radians(coord1[0]), math.radians(coord1[1])
        lat2, lon2 = math.radians(coord2[0]), math.radians(coord2[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        distance = R * c
        return distance

    def _build_edges(self):
        """Builds all edges (distances) between every pair of nodes."""
        node_ids = list(self.nodes.keys())
        for i in range(len(node_ids)):
            for j in range(i + 1, len(node_ids)):
                id1 = node_ids[i]
                id2 = node_ids[j]
                
                # Calculate distance (we are mocking a Map API distance with Haversine)
                distance = self._haversine_distance(self.nodes[id1], self.nodes[id2])
                
                # Add edges to the adjacency list (undirected graph)
                self.adj[id1][id2] = distance
                self.adj[id2][id1] = distance

    def nearest_neighbor_tsp(self, start_node_id):
        """
        Implements the Nearest Neighbor heuristic for the Traveling Salesperson Problem.
        This is a greedy, sub-optimal but fast approach (O(N^2)).
        """
        if start_node_id not in self.nodes:
            raise ValueError("Start node ID not found in graph.")

        current_node = start_node_id
        unvisited_nodes = set(self.nodes.keys())
        unvisited_nodes.remove(start_node_id)
        
        route = [start_node_id]
        total_distance = 0.0

        while unvisited_nodes:
            nearest_neighbor = None
            min_dist = float('inf')

            # Find the unvisited neighbor closest to the current node
            for neighbor, distance in self.adj[current_node].items():
                if neighbor in unvisited_nodes:
                    if distance < min_dist:
                        min_dist = distance
                        nearest_neighbor = neighbor

            if nearest_neighbor is None:
                # Should not happen in a complete graph, but handles errors
                break 

            # Move to the nearest neighbor
            route.append(nearest_neighbor)
            unvisited_nodes.remove(nearest_neighbor)
            total_distance += min_dist
            current_node = nearest_neighbor

        # Final step: return to the starting node
        if route and start_node_id in self.adj[route[-1]]:
            return_dist = self.adj[route[-1]][start_node_id]
            route.append(start_node_id)
            total_distance += return_dist
        
        return route, total_distance
