import matplotlib.pyplot as plt
from src import ReplicatorFormula, PayoffMatrix
import config


def host_tradeoff(repl):
    """
        Displays plot for discriminator host
        x-axis: host discrimination
        y-axis: fitness values
    """

    repl.populations[1].strategy = "D"
    x = range(0, 6)
    for strat in ["c", "m"]:
        y = list()
        repl.populations[0].strategy = strat
        for r in x:
            repl.payoff_matrix.matrix[('m', 'D')] = ((config.b - config.z), (config.B / (1 + r)))
            repl.payoff_matrix.matrix[('c', 'D')] = ((config.b / (1 + config.alpha * r)), (-config.K / (1 + config.beta * r)))
            fitness = repl.fitness_function(1)
            y.append(fitness)
        plt.plot(x, y)
    plt.legend(["c", "m"])
    plt.show()


def host_competition(replicator):
    pass


def partner_tradeoff(replicator):
    repl.populations[1].strategy = "D"
    x = range(0, 6)
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


def partner_competition(replicator):
    pass


if __name__ == "__main__":
    pm = PayoffMatrix.PayoffMatrix(config.host_strategies, config.partner_strategies, config.matrix)

    host = ReplicatorFormula.Population("Host", config.host_strategy, config.host_strategies, config.host_size)
    partner = ReplicatorFormula.Population("Partner", config.partner_strategy, config.partner_strategies,
                                           config.partner_size)

    repl = ReplicatorFormula.Replicator(pm, [partner, host])

    host_tradeoff(repl)
