from src import PayoffMatrix, ReplicatorFormula
import config

if __name__ == "__main__":

    # Payoff matrix as given in Bever, J.
    # Row = Host; Column = Partner

    pm = PayoffMatrix.PayoffMatrix(config.host_groups.keys(), config.partner_groups.keys(), config.matrix)

    host = ReplicatorFormula.Population("Host", config.host_groups)
    partner = ReplicatorFormula.Population("Partner", config.partner_groups)

    repl = ReplicatorFormula.Replicator(pm, [partner, host])

    repl.calculate_steps(config.timesteps)

    print("Partner: {}".format(repl.populations[0].groups))
    print("Host: {}".format(repl.populations[1].groups))  
    

