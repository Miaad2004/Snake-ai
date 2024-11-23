from Algorithm import Algorithm
from heapq import heappush, heappop

class UCS(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def run_algorithm(self, snake):
        self.frontier = []
        self.explored_set = []
        self.path = []

        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        initialstate.cost_from_start = 0

        heappush(self.frontier, (initialstate.cost_from_start, initialstate))

        while len(self.frontier) > 0:
            # Get the lowest cost node
            current_cost, current_node = heappop(self.frontier)

            if current_node in self.explored_set:
                continue

            self.explored_set.append(current_node)

            # Check if we reached the goal
            if current_node.equal(goalstate):
                return self.get_path(current_node)

            # Get neighbors
            neighbors = self.get_neighbors(current_node)

            for neighbor in neighbors:
                # Skip invalid nodes
                if self.inside_body(snake, neighbor) or self.outside_boundary(neighbor):
                    continue

                cost = current_cost + 1  

                if neighbor not in self.explored_set or cost < neighbor.cost_from_start:
                    neighbor.cost_from_start = cost
                    neighbor.parent = current_node
                    heappush(self.frontier, (neighbor.cost_from_start, neighbor))

        return None