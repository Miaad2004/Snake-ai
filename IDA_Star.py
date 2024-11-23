from Algorithm import Algorithm

class IDAStar(Algorithm):
    def __init__(self, grid):
        super().__init__(grid)

    def heuristic(self, state1, state2):
        # Manhattan distance
        return abs(state1.x - state2.x) + abs(state1.y - state2.y)
    
    def depth_limited_A_star(self, snake, goalstate, currentstate, g, threshold):
        f = g + self.heuristic(currentstate, goalstate)
        
        if f > threshold:
            return f, None
        
        if currentstate.equal(goalstate):
            return f, self.get_path(currentstate)
        
        if currentstate in self.explored_set:
            return float('inf'), None

        self.explored_set.add(currentstate)
        neighbors_nodes = self.get_neighbors(currentstate)
        min_threshold = float('inf')

        for neighbor in neighbors_nodes:
            if not self.inside_body(snake, neighbor) and not self.outside_boundary(neighbor) and neighbor not in self.explored_set:
                neighbor.parent = currentstate
                t, path = self.depth_limited_A_star(snake, goalstate, neighbor, g + 1, threshold)
                
                if path is not None:
                    return t, path
                
                if t < min_threshold:
                    min_threshold = t
                    
        return min_threshold, None

    def run_algorithm(self, snake):
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        threshold = self.heuristic(initialstate, goalstate)

        while True:
            self.explored_set = set()
            t, path = self.depth_limited_A_star(snake, goalstate, initialstate, 0, threshold)
            
            if path is not None:
                return path
            
            if t == float('inf'):
                print("No solution found")
                return None
            
            threshold = t