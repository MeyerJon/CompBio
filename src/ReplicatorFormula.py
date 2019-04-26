class Population:

    def __init__(self, name, strategy, size=0):
        self.name = name
        self.strategy = strategy
        self.size = size


class Replicator:

    def __init__(self, payoff_matrix, initial_populations):
        self.payoff_matrix = payoff_matrix
        self.populations = initial_populations

    def fitness_function(self, target_pop):

        fitness = sum([pop.size * self.payoff_matrix.getOutcome(target_pop.strategy, pop.strategy)[0] for pop in self.populations])
        return fitness
        
    def calculate_one_step(self, populations):

        pop_fitnesses = list()
        for pop in populations:
            pop_fitnesses.append(self.fitness_function(pop))
        avg_fitness = sum([self.populations[i].size * pop_fitnesses[i] for i in range(len(self.populations))])

        for i in range(len(populations)):
            self.populations[i].size = self.populations[i].size * (pop_fitnesses[i] / avg_fitness)

        return populations

    def calculate_steps(self, n_steps=10):

        for i in range(n_steps):
            self.populations = self.calculate_one_step(self.populations)
            print(f"Populations at timestep {i}:")
            for pop in self.populations:
                print(f"\t -{pop.name}: {pop.size}")


if __name__ == "__main__":

    import PayoffMatrix

    matrix = dict()
    options = ['H', 'D']

    matrix[('H', 'H')] = (-1, -1)
    matrix[('H', 'D')] = (2, 0)
    matrix[('D', 'H')] = (0, 2)
    matrix[('D', 'D')] = (1, 1)

    pm = PayoffMatrix.PayoffMatrix(options, matrix)

    doves = Population("Doves", "D", size=0.8)
    hawks = Population("Hawks", "H", size=0.2)

    repl = Replicator(pm, [doves, hawks])

    repl.calculate_steps()       
        
