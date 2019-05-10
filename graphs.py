import matplotlib.pyplot as plt
import numpy as np
from src import ReplicatorFormula, PayoffMatrix
import config


def get_repl():
    pm = PayoffMatrix.PayoffMatrix(config.host_strategies, config.partner_strategies, config.matrix)

    host = ReplicatorFormula.Population("Host", config.host_strategy, config.host_strategies, config.host_size)
    partner = ReplicatorFormula.Population("Partner", config.partner_strategy, config.partner_strategies,
                                           config.partner_size)

    repl = ReplicatorFormula.Replicator(pm, [partner, host])

    return repl


def host_tradeoff(repl):
    """
        Displays plot for discriminator host
        x-axis: host discrimination
        y-axis: fitness values
    """

    repl.populations[1].strategy = "D"
    x = np.linspace(0, 6, 50)
    for strat in ["c", "m"]:
        y = list()
        repl.populations[0].strategy = strat
        for r in x:
            repl.payoff_matrix.matrix[('m', 'D')] = ((config.b - config.z), (config.B / (1 + r)))
            repl.payoff_matrix.matrix[('c', 'D')] = (
            (config.b / (1 + config.alpha * r)), (-config.K / (1 + config.beta * r)))
            fitness = repl.fitness_function(1)
            y.append(fitness)
        plt.plot(x, y)
    plt.legend(["c", "m"])
    plt.show()


def host_competition(repl):
    x = np.linspace(0, 1, 50)
    repl.populations[0].strategy = "m"
    for strat in ["D", "G"]:
        y = list()
        repl.populations[1].strategy = strat
        for m in x:
            repl.populations[0].size = m
            fitness = repl.fitness_function(1)
            y.append(fitness)
        plt.plot(x, y)
        plt.ylim(-config.K, config.B)
    plt.legend(["discriminator", "giver"])

    m_cross_x = (config.beta * config.K * (1 + config.r)) / ((config.B * (1 + config.beta * config.r)) + (config.beta * config.K * (1 + config.r)))
    m_cross_y = (-config.K) / (1 + (config.beta * config.r))
    plt.plot(m_cross_x, m_cross_y, '.')

    plt.show()


def partner_tradeoff(repl):
    repl.populations[1].strategy = "D"
    x = np.linspace(0, 6, 50)
    for strat in ["c", "m"]:
        y = list()
        repl.populations[0].strategy = strat
        for r in x:
            repl.payoff_matrix.matrix[('m', 'D')] = ((config.b - config.z), (config.B / (1 + r)))
            repl.payoff_matrix.matrix[('c', 'D')] = (
                (config.b / (1 + config.alpha * r)), (-config.K / (1 + config.beta * r)))
            fitness = repl.fitness_function(0)
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

    repl.populations[1].strategy = "D"
    x = np.linspace(0, 1, 50)
    for strat in ["c", "m"]:
        y = list()
        repl.populations[0].strategy = strat
        for r in x:
            repl.populations[1].size = r
            fitness = repl.fitness_function(0)
            y.append(fitness)
        plt.plot(x, y)
        plt.ylim(0, config.b)
    plt.legend(["c", "m"])
    plt.show()


if __name__ == "__main__":

    #host_tradeoff(get_repl())
    host_competition(get_repl())
    #partner_tradeoff(get_repl())
    #partner_competition(get_repl())

