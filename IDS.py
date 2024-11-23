from Algorithm import Algorithm
import time

class IDS(Algorithm):
    def __init__(self, grid, max_depth=1000, timeout=5):
        super().__init__(grid)
        self.max_depth = max_depth
        self.timeout = timeout

    def depth_limited_DFS(self, snake, goalstate, currentstate, limit):
        if currentstate.equal(goalstate):
            return self.get_path(currentstate)
        
        if limit == 0:
            return None
        
        if currentstate in self.explored_set:
            return None

        self.explored_set.add(currentstate)
        neighbors_nodes = self.get_neighbors(currentstate)

        for neighbor in neighbors_nodes:
            if not self.inside_body(snake, neighbor) and\
               not self.outside_boundary(neighbor) and neighbor not in self.explored_set:
                   
                neighbor.parent = currentstate
                path = self.depth_limited_DFS(snake, goalstate, neighbor, limit - 1)
                
                if path is not None:
                    return path
        return None

    def run_algorithm(self, snake):
        initialstate, goalstate = self.get_initstate_and_goalstate(snake)
        depth = 0
        start_time = time.time()

        while depth <= self.max_depth:
            if time.time() - start_time > self.timeout:
                print("Timeout reached")
                return None

            self.explored_set = set()
            path = self.depth_limited_DFS(snake, goalstate, initialstate, depth)
            
            if path is not None:
                return path
            
            depth += 1

        print("Maximum depth reached")
        return None