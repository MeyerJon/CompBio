from src import PayoffMatrix, ReplicatorFormula
import graphs
import config

if __name__ == "__main__":

    # Payoff matrix as given in Bever, J.
    # Row = Host; Column = Partner

    pm = PayoffMatrix.PayoffMatrix(config.host_population.keys(), config.partner_population.keys(), config.matrix)

    host = ReplicatorFormula.Population("Host", config.host_population)
    partner = ReplicatorFormula.Population("Partner", config.partner_population)

    repl = ReplicatorFormula.Replicator(pm, [partner, host])


    # Runs a simulation and plots for the example configuration
    graphs.population_dynamic(repl)
    

