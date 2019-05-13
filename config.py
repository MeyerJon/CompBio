# Parameter values
B_host_mutualism_benefit = 5
b_partner_mutualism_benefit = 5
z_partner_mutualism_cost = 2
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
host_groups = {
                "D": 0.5,
                "G": 0.5
              }

partner_groups = {
                    "m": 0.5,
                    "c": 0.5
                 }


# Simulation parameters
iterations = 10000
timestep = 1.0 / 500.0