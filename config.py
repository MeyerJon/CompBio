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

host_strategies = ["D", "G"]
partner_strategies = ["m", "c"]

matrix[('m', 'D')] = ((b - z), (B / (1 + r)))
matrix[('m', 'G')] = ((b - z), B)
matrix[('c', 'D')] = ((b / (1 + alpha * r)), (-K / (1 + beta * r)))
matrix[('c', 'G')] = (b, -K)


# Parameters
host_strategy = "G"
partner_strategy = "c"
host_size = 1
partner_size = 1