class Population:

    def __init__(self, name, groups):
        self.name = name
        self.groups = groups


class Replicator:

    def __init__(self, payoff_matrix, initial_populations):
        self.payoff_matrix = payoff_matrix
        self.populations = initial_populations

    def fitness_function(self, target_pop_ix, target_pop_strat):
        """
            Fitness function as given in Bever (2014).
            Returns the fitness of the target population (given by index) in the current model.
        """

        other_pop = self.populations[not target_pop_ix]
        fitness = 0
        for group in other_pop.groups.keys():
            fitness += other_pop.groups[group] * self.payoff_matrix.getOutcome(target_pop_strat, group)[target_pop_ix]

        return fitness
        
    def calculate_one_step(self, populations):

        

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

    doves = Population("Animals", {"Hawks": 0.2, "Doves": 0.8})

    repl = Replicator(pm, [doves])

    repl.calculate_steps(n_steps=100)
