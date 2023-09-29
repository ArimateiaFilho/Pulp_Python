from pulp import *

#Problema definido
prob = LpProblem("test",const.LpMaximize)

#Quantidade de variaveis
setI=range(2)
#Quantidade de restrições
setJ=range(2)
#Custo da varias nas restrições
a=[[1,1.5],[4,3]]
# Lado direito das restrições
b=[150,360]
#Custo das variáveis na FO
c=[120,160]
#Variaveis decisivas 
x_vars=[]

for i in setI:
	x_vars.append(LpVariable("x{}".format(i+1),0,None,const.LpInteger))

#variável com valo das multiplicações de x e c
varCust = []
for i in setI: 
	varCust.append(x_vars[i] * c[i])
objective =	lpSum(varCust)

#adiciona a função objetiva ao problema
prob.setObjective(objective)

#-------------------------------------------
#Criando a parte esquerda das restrições 
varCust = []
constrain = []
for i in setI:
	#define apena um linha 
	for j in setJ:
		#Junta cada custo por var em uma lista 
		varCust.append(a[i][j]*x_vars[j])
	#Adiciona a restrição ao problema  	                     
	prob.addConstraint(
		#Cria um restrição no formato padrão do PuLP 
		LpConstraint(e = lpSum(varCust),sense = LpConstraintLE, rhs = b[i], name = 'r{}'.format(i+1))
	)
	#A var é limpara para salvar novas restrições
	varCust = []

#--------------------------------------------

print(prob)

#Resolve
prob.solve()

print(x_vars[0].value())
print(x_vars[1].value())