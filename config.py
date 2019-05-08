# Parameter values
B_host_mutualism_benefit = 1
b_partner_mutualism_benefit = 1
z_partner_mutualism_cost = 1
K_host_association_cost = 1
r_host_discrimination = 1
alpha = 1
beta = 1

b = b_partner_mutualism_benefit
B = B_host_mutualism_benefit
z = z_partner_mutualism_cost
alpha = alpha
beta = beta
r = r_host_discrimination
K = K_host_association_cost

# Payoff Matrix
matrix = dict()

host_strategies = ["D", "G"]
partner_strategies = ["m", "c"]

matrix[('m', 'D')] = ((b - z), (B / (1 + r)))
matrix[('m', 'G')] = ((b - z), B)
matrix[('c', 'D')] = ((b / (1 + alpha * r)), (-K / (1 + beta * r)))
matrix[('c', 'G')] = (b, -K)