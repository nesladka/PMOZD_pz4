import pulp

lp_problem = pulp.LpProblem("LP_Problem", pulp.LpMinimize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)
x3 = pulp.LpVariable("x3", lowBound=0)
x4 = pulp.LpVariable("x4", lowBound=0)
x5 = pulp.LpVariable("x5", lowBound=0)

lp_problem += 2*x1 - x2 + 3*x4 + 4, "Objective Function"

lp_problem += x1 - 2*x3 + x3 - 3*x5 == 2, "Constraint 1"
lp_problem += 2*x1 + x2 + 4*x3 + x5 == 6, "Constraint 2"
lp_problem += -x1 + 2*x2 + 3*x4 == 4, "Constraint 3"

lp_problem.solve()

print("Status:", pulp.LpStatus[lp_problem.status])
print("x1 =", x1.varValue)
print("x2 =", x2.varValue)
print("x3 =", x3.varValue)
print("x4 =", x4.varValue)
print("x5 =", x5.varValue)
print("Максимальное значение =", pulp.value(lp_problem.objective))
