from pulp import *

#Problema definido
prob = LpProblem("test",const.LpMaximize)

#Quantidade de variaveis
setI=range(17)
#formatação da matriz pra vetor
# Lado direito das restrições
#x12 x13 x23 x24 x26 x32 x35 x36 x46 x47 x53 x56 x57 x63 x64 x65 x67
b=[10,10,1,8,6,1,12,4,3,7,12,2,8,4,3,2,2]
#Variaveis decisivas 

x_vars=[]
F=LpVariable("F",0,None,const.LpInteger)

for i in setI:
	x_vars.append(LpVariable("x{}".format(i+1),0,None,const.LpInteger))

objective =	lpSum(F)

#adiciona a função objetiva ao problema
prob.setObjective(objective)

#-------------------------------------------
#Criando a parte esquerda das restrições 

#Restrição Peso das Arestas

for i in setI:
	#Adiciona a restrição ao problema  	                     
	prob.addConstraint(
		#Cria um restrição no formato padrão do PuLP 
		LpConstraint(e = lpSum(x_vars[i]),sense = LpConstraintLE, rhs = b[i], name = 'r{}'.format(i+1))
	)

#--------------------------------------------

#Restrição de conservação de flux_varso
prob+=-F+x_vars[0]+x_vars[1]==0,"rr1"
prob+=-x_vars[0]+x_vars[3]+x_vars[4]+x_vars[2]-x_vars[5]==0,"rr2"
prob+=-x_vars[1]+x_vars[5]+x_vars[7]+x_vars[6]-x_vars[2]-x_vars[13]-x_vars[10]==0,"rr3"
prob+=-x_vars[3]-x_vars[14]+x_vars[9]+x_vars[8]==0,"rr4"
prob+=-x_vars[6]-x_vars[15]+x_vars[10]+x_vars[11]+x_vars[12]==0,"rr5"
prob+=-x_vars[4]-x_vars[8]-x_vars[7]-x_vars[11]+x_vars[14]+x_vars[15]+x_vars[13]+x_vars[16]==0,"rr6"
prob+=-x_vars[9]-x_vars[16]-x_vars[12]+F==0,"rr7"

print(prob)

#Resolve
prob.solve()

nomes=['x12', 'x13' ,'x23', 'x24', 'x26' ,'x32', 'x35' ,'x36' ,'x46', 'x47', 'x53' ,'x56', 'x57' ,'x63' ,'x64' ,'x65' ,'x67']

for i in setI:
	print(nomes[i]+" -> {}".format(x_vars[i].value()))
