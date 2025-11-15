from graph_solver import Graph

# --- Mock Data to simulate real-world locations ---
# NOTE: In a real-world app, these distances would be fetched from a Map API,
# but using Haversine distance here showcases the core algorithm.

LOCATIONS = {
    'A': (40.7128, -74.0060),  # New York
    'B': (34.0522, -118.2437), # Los Angeles
    'C': (41.8781, -87.6298),  # Chicago
    'D': (29.7604, -95.3698),  # Houston
    'E': (39.9526, -75.1652)   # Philadelphia
}
START_NODE = 'A'

def run_optimization():
    """
    Initializes the Graph, runs the Nearest Neighbor algorithm, 
    and prints the optimized route.
    """
    print(f"--- Route Optimization Solver ---")
    print(f"Locations to visit: {list(LOCATIONS.keys())}")
    print(f"Starting point: {START_NODE}\n")

    # 1. Initialize the graph and calculate all distances
    try:
        delivery_graph = Graph(LOCATIONS)
    except Exception as e:
        print(f"Error initializing graph: {e}")
        return

    # 2. Run the Nearest Neighbor Heuristic
    optimized_route, total_distance = delivery_graph.nearest_neighbor_tsp(START_NODE)

    # 3. Output Results
    route_display = " -> ".join(optimized_route)
    
    print("Optimization Complete:")
    print(f"Optimized Route: {route_display}")
    print(f"Total Distance: {total_distance:.2f} km")
    print("\n---------------------------------")
    print("Note: Uses Nearest Neighbor Heuristic (Greedy approach).")
    print("Distance is calculated via Haversine (straight-line distance).")


if __name__ == "__main__":
    run_optimization()
