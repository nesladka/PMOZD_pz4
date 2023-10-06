import pulp

model = pulp.LpProblem("Linear_Programming_Problem", pulp.LpMaximize)

x1 = pulp.LpVariable("x1", lowBound=0)
x2 = pulp.LpVariable("x2", lowBound=0)

z = x1 - 2 * x2
model += z

model += x1 - 2 * x2 <= 4
model += -x1 + 2 * x2 <= 4
model += x1 + 2 * x2 <= 6

model.solve()

print("Результат:")
print(f"x1 = {x1.varValue}")
print(f"x2 = {x2.varValue}")
print(f"Максимальное значение z = {pulp.value(model.objective)}")
