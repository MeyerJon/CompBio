import src as src
import config

if __name__ == "__main__":

    # Payoff matrix as given in Bever, J.
    # Row = Host; Column = Partner

    pm = src.PayoffMatrix.PayoffMatrix(config.host_strategies, config.partner_strategies, config.matrix)

    

