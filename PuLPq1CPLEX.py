from pulp import *

#Problema definido
prob = LpProblem("test",const.LpMaximize)

#Definindo variaveis de decisão
x_1 = LpVariable("x1",0,None,const.LpInteger)
x_2 = LpVariable("x2",0,None,const.LpInteger)

#Definindo Função Objetivo
prob += 120*x_1 + 160*x_2,"obj"

#Definindo restrições 
prob += x_1 + 1.5*x_2 <= 150, "r1"
prob += 4*x_1 + 3*x_2 <= 360, "r2"

#Printando o problema por completo
print(prob)

#Chamando o solver padrão
prob.solve(solver = CPLEX_CMD())

prob.writeLP( "PuLPq1.lp" , writeSOS = 1 , mip = 1 , max_length = 100 )
#Mostrando os valores das variaveis de decisão
print(x_1.value())
print(x_2.value())