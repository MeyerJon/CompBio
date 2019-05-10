import matplotlib.pyplot as plt
import numpy as np
from src import ReplicatorFormula, PayoffMatrix
import config, copy


def get_repl():
    pm = PayoffMatrix.PayoffMatrix(config.host_groups.keys(), config.partner_groups.keys(), copy.deepcopy(config.matrix))

    host = ReplicatorFormula.Population("Host", copy.deepcopy(config.host_groups))
    partner = ReplicatorFormula.Population("Partner", copy.deepcopy(config.partner_groups))

    repl = ReplicatorFormula.Replicator(pm, [partner, host])

    return repl


def host_tradeoff(repl):
    """
        Displays plot for discriminator host
        x-axis: host discrimination
        y-axis: fitness values
    """

    repl.populations[1].groups["D"] = 1.0
    repl.populations[0].groups["G"] = 0.0
    x = np.linspace(0, 6, 50)
    groups = [{"c": 1.0, "m": 0.0}, {"c": 0.0, "m": 1.0}]
    for group in groups:
        y = list()
        repl.populations[0].groups = group
        for r in x:
            repl.payoff_matrix.matrix[('m', 'D')] = ((config.b - config.z), (config.B / (1 + r)))
            repl.payoff_matrix.matrix[('c', 'D')] = (
            (config.b / (1 + config.alpha * r)), (-config.K / (1 + config.beta * r)))
            fitness = repl.fitness_function(1, "D")
            y.append(fitness)
        plt.plot(x, y)
    plt.legend(["c", "m"])
    plt.show()


def host_competition(repl):
    """
        Fitness of host over varying mutualist size
    """
    x = np.linspace(0, 1, 50)
    for strat in ["D", "G"]:
        y = list()
        for m in x:
            repl.populations[0].groups["m"] = m
            repl.populations[0].groups["c"] = 1 - m
            fitness = repl.fitness_function(1, strat)
            y.append(fitness)
        plt.plot(x, y)
        plt.ylim(-config.K, config.B)
    plt.legend(["discriminator", "giver"])

    m_cross_x = (config.beta * config.K * (1 + config.r)) / ((config.B * (1 + config.beta * config.r)) + (config.beta * config.K * (1 + config.r)))
    repl.populations[0].groups["m"] = m_cross_x
    repl.populations[0].groups["c"] = 1 - m_cross_x
    m_cross_y = repl.fitness_function(1, "D")
    plt.plot(m_cross_x, m_cross_y, '.')

    plt.show()


def partner_tradeoff(repl):
    """
        Fitness of partner over varying discrimination
    """
    x = np.linspace(0, 6, 50)
    repl.populations[1].groups["D"] = 1.0
    repl.populations[1].groups["G"] = 0.0
    for strat in ["c", "m"]:
        y = list()
        for r in x:
            repl.payoff_matrix.matrix[('m', 'D')] = ((config.b - config.z), (config.B / (1 + r)))
            repl.payoff_matrix.matrix[('c', 'D')] = (
                (config.b / (1 + config.alpha * r)), (-config.K / (1 + config.beta * r)))
            fitness = repl.fitness_function(0, strat)
            y.append(fitness)
        plt.plot(x, y)
    plt.legend(["c", "m"])
    plt.show()


def partner_competition(repl):
    """
        Displays plot for discriminator host
        x-axis: host discrimination
        y-axis: fitness values
    """
    x = np.linspace(0, 1, 50)
    for strat in ["c", "m"]:
        y = list()
        repl.populations[0].strategy = strat
        for D in x:
            repl.populations[1].groups["D"] = D
            repl.populations[1].groups["G"] = 1 - D
            fitness = repl.fitness_function(0, strat)
            y.append(fitness)
        plt.plot(x, y)
        plt.ylim(0, config.b)
    plt.legend(["c", "m"])
    plt.show()


def population_dynamic(repl):
    """
        Plots discriminators vs cheaters over time
    """

    x = range(0, config.timesteps)
    y_c = [repl.populations[0].groups["c"]]
    y_D = [repl.populations[1].groups["D"]]
    for _ in range(config.timesteps-1):
        repl.populations = repl.calculate_one_step(repl.populations)
        y_c.append(repl.populations[0].groups["c"])
        y_D.append(repl.populations[1].groups["D"])
    
    plt.plot(x, y_c, x, y_D)
    plt.legend(["Cheaters", "Discriminators"])
    #plt.show()
    plt.savefig("pop_dynamic.svg")


if __name__ == "__main__":

    #host_tradeoff(get_repl())
    #host_competition(get_repl())
    #partner_tradeoff(get_repl())
    #partner_competition(get_repl())
    population_dynamic(get_repl())

