from src import PayoffMatrix, ReplicatorFormula
import config

if __name__ == "__main__":

    # Payoff matrix as given in Bever, J.
    # Row = Host; Column = Partner

    pm = PayoffMatrix.PayoffMatrix(config.host_strategies, config.partner_strategies, config.matrix)

    host = ReplicatorFormula.Population("Host", config.host_strategy, config.host_strategies, config.host_size)
    partner = ReplicatorFormula.Population("Partner", config.partner_strategy, config.partner_strategies, config.partner_size)

    repl = ReplicatorFormula.Replicator(pm, [partner, host])

    print("Partner fitness: {}".format(repl.fitness_function(1)))
    print("Host fitness: {}".format(repl.fitness_function(0)))  
    

