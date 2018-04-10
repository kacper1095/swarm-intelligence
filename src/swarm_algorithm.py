class SwarmIntelligence:
    def __init__(self, population_size, constraints):
        self.population_size = population_size
        self.global_best_solution = None
        self.local_best_solutions = None
        self.population = None
        self.constraints = constraints

        self.populate_swarm()

    def populate_swarm(self):
        raise NotImplementedError

    def get_new_positions(self, step):
        raise NotImplementedError

    def update_positions(self, new_positions, step):
        raise NotImplementedError
