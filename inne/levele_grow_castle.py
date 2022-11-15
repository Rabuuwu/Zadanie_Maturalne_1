cost = 1000
times = 847
x = 0
starting_upgrade_cost = 1153000
overall = 0

for x in range(times):
    x+=1
    starting_upgrade_cost+=cost
    overall+=starting_upgrade_cost
    print(x,starting_upgrade_cost, overall)
