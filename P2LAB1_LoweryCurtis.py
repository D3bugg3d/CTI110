mpg = float(input())
cost = float(input())

gas_cost_20 = cost * (20 / mpg)
gas_cost_75 = cost * (75 / mpg)
gas_cost_500 = cost * (500 / mpg)

print(f'{gas_cost_20:.2f} {gas_cost_75:.2f} {gas_cost_500:.2f}')