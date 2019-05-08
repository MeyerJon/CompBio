class Population:

    def __init__(self, name, strategy, options, size=0):
        self.name = name
        self.strategy = strategy
        self.options = options
        self.size = size


class Replicator:

    def __init__(self, payoff_matrix, initial_populations):
        self.payoff_matrix = payoff_matrix
        self.populations = initial_populations

    def fitness_function(self, target_pop_ix):
        """
            Fitness function as given in Bever (2014).
            Returns the fitness of the target population (given by index) in the current model.
        """

        target_pop = self.populations[target_pop_ix]
        other_pop = self.populations[not target_pop_ix]

        other_strat = other_pop.options[0] if other_pop.options[0] != other_pop.strategy else other_pop.options[1]

        fitness = other_pop.size * self.payoff_matrix.getOutcome(target_pop.strategy, other_pop.strategy)[target_pop_ix] + \
                  (1 - other_pop.size) * self.payoff_matrix.getOutcome(target_pop.strategy, other_strat)[target_pop_ix]


        return fitness
        
    def calculate_one_step(self, populations):

        pop_fitnesses = list()
        for pop_ix in range(len(populations)):
            pop_fitnesses.append(self.fitness_function(pop_ix))
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
    options1 = ['A1', 'B1']
    options2 = ['A2', 'B2']

    matrix[('A1', 'A2')] = (2, 2)
    matrix[('A1', 'B2')] = (1, 2)
    matrix[('B1', 'A2')] = (2, 1)
    matrix[('B1', 'B2')] = (2, 2)

    pm = PayoffMatrix.PayoffMatrix(options1, options2, matrix)

    doves = Population("Doves", "A1", options1, size=0.8)
    hawks = Population("Hawks", "B2", options2, size=0.2)

    repl = Replicator(pm, [doves, hawks])

    repl.calculate_steps(n_steps=100)
