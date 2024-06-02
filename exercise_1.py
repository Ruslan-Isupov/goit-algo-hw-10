import pulp

model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)


lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')  
fruit_juice = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Integer')  


model += lemonade + fruit_juice , "Profit"

model += (2 * lemonade + 1 * fruit_juice <= 100, "Water")
model += (1 * lemonade <= 50, "Sugar")
model += (1 * lemonade <= 30, "Lemon_juice")
model += (2 * fruit_juice <= 40, "Fruit_puree")


model.solve()

print(f"Status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {pulp.value(lemonade)} units")
print(f"Fruit_juice: {pulp.value(fruit_juice)} units")
print(f"Profit: {pulp.value(model.objective)} units")