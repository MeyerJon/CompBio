import src as src
import config

if __name__ == "__main__":

    # Payoff matrix as given in Bever, J.
    # Row = Host; Column = Partner
    matrix = dict()
    strategies = ["A", "B"]

    b = config.b_partner_mutualism_benefit
    B = config.B_host_mutualism_benefit
    z = config.z_partner_mutualism_cost
    alpha = config.alpha
    beta = config.beta
    r = config.r_host_discrimination
    K = config.K_host_association_cost

    matrix[('A', 'A')] = ((b - z), (B / (1 + r)))
    matrix[('A', 'B')] = ((b - z), B)
    matrix[('B', 'A')] = ((b / (1 + alpha * r)), (-K / (1 + beta * r)))
    matrix[('B', 'B')] = (b, -K)

    pm = src.PayoffMatrix.PayoffMatrix(strategies, matrix)

    

