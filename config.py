# Parameter values
B_host_mutualism_benefit = 5
b_partner_mutualism_benefit = 5
z_partner_mutualism_cost = 1
K_host_association_cost = 2
r_host_discrimination = 2
alpha = 1
beta = 1

b = b_partner_mutualism_benefit
B = B_host_mutualism_benefit
K = K_host_association_cost
z = z_partner_mutualism_cost
alpha = alpha
beta = beta
r = r_host_discrimination

# Payoff Matrix
matrix = dict()

matrix[('m', 'D')] = ((b - z), (B / (1 + r)))
matrix[('m', 'G')] = ((b - z), B)
matrix[('c', 'D')] = ((b / (1 + (alpha * r))), (-K / (1 + (beta * r))))
matrix[('c', 'G')] = (b, -K)

# Groups
m_osc = 0.45  # (beta * K * (1 + r)) / ((B * (1 + beta * r)) + (beta * K * (1 + r)))
D_osc = 0.45  # (z / b) * ((1 + alpha * r) / (alpha * r))
host_groups = {
    "D": D_osc + 0.05,
    "G": 1 - D_osc - 0.05
}

partner_groups = {
    "m": m_osc + 0.05,
    "c": 1 - m_osc - 0.05
}

# Simulation parameters
iterations = 100000
timestep = 1.0 / 1000
