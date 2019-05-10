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

        pop1_group_fitnesses = dict()
        pop1_avg_fitness = 0
        for group in self.populations[0].groups.keys():
            pop1_group_fitnesses[group] = self.populations[0].groups[group] * self.fitness_function(0, group)
            pop1_avg_fitness += pop1_group_fitnesses[group]
        
        pop2_group_fitnesses = dict()
        pop2_avg_fitness = 0
        for group in self.populations[1].groups.keys():
            pop2_group_fitnesses[group] = self.populations[1].groups[group] * self.fitness_function(1, group)
            pop2_avg_fitness += pop2_group_fitnesses[group]

        pop1_g1 = list(self.populations[0].groups.keys())[0]
        pop1_g2 = list(self.populations[0].groups.keys())[1]
        dg1 = self.populations[0].groups[pop1_g1] * self.populations[0].groups[pop1_g2] * (pop1_group_fitnesses[pop1_g1] - pop1_group_fitnesses[pop1_g2])
        self.populations[0].groups[pop1_g1] += dg1
        self.populations[0].groups[pop1_g2] -= dg1

        pop2_g1 = list(self.populations[1].groups.keys())[0]
        pop2_g2 = list(self.populations[1].groups.keys())[1]
        dg1 = self.populations[1].groups[pop2_g1] * self.populations[1].groups[pop2_g2] * (pop2_group_fitnesses[pop2_g1] - pop2_group_fitnesses[pop2_g2])
        self.populations[1].groups[pop2_g1] += dg1
        self.populations[1].groups[pop2_g2] -= dg1

        return populations

    def calculate_steps(self, n_steps=10):

        for i in range(n_steps):
            self.populations = self.calculate_one_step(self.populations)


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
