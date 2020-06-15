# Author Zhicheng Zhu
# Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu

# solve extensive form model using Pyomo
# 
#Input(in function create_files()):
#	1. file_name: put the full path of ef.dat here.
#	2. number of componetns. I;
#	3. planning horizon, T, {0,1,...,T}
#	4. Extensive planning horizon T_ex, we can just set it to T*2.
#	5. setup cost, d.
#	6. initial age. see code "f.write("param ps := " + str(2)+";\n\n")", here means current ages for all components are 2.
#	7. max_iteration (outside function create_files()). Set this variable to run multiple test cases with different parameter settings. 
#		Usually set this to 1.
#	8. number of scenario.  W (not in function create_files()).
#Output:
#	1. Optimal solution for each iteration (experiment), 	"print("x["+str(i)+"]="+str(round(ef_insts[0].x[i](), 4)))"
#	2. Optimal objective value for each iteration (experiment), "print ("objective value=%f" %ef_insts[0].objCost())"
#	3. Average CPU time for all iteration, "print ("avg time=%d" %((end_time1 - start_time1)/100.0));"
#	4. Average objective values "print ("average cost"); print (np.average(cost))"
#	5. Objective values for all itertaions "print ("cost", cost)". 



from pyutilib.misc import import_file
from pyomo.environ import *
from pyomo.opt import SolverFactory
from pyomo.opt.base import SolverFactory
from pyomo.opt.parallel import SolverManagerFactory
from pyomo.opt.parallel.manager import solve_all_instances
import time
import numpy as np

def create_files(iter,W):

	file_name = "path of this file\\ef.dat"	#input: ./ef.dat path
	f = open(file_name,"w")


	#W = 140;
	I = 2;				#input: number of components
	T = 49;				#input: planning horizon. starts from 0
	T_ex = 100;			#input:	extensive planning horizon. NormallyT*2 would be enough
	d = 5;				#input: setup cost
	f.write("param NUMSCEN := " + str(W)+";\n\n")
	
	f.write("param prob := " + str(1.0/W)+";\n\n")	
	
	f.write("param pI := " + str(I)+";\n\n")

	f.write("param pT := " + str(T)+";\n\n")

	f.write("param pT_ex := " + str(T_ex)+";\n\n")

	f.write("param ps := " + str(2)+";\n\n")

	f.write("param pR := " + str(T+2)+";\n\n")

	f.write("param pd := " + str(d)+";\n\n")
	
	f.write("param iter := " + str(iter)+";\n\n")

	f.close()

cost = [];
start_time1 = time.clock()
max_iteration = 1;				#input: it is used for a seed control purpose, or run instances with different sets of lifetimes.

for iter in range(max_iteration):
	print ("================")
	print ("iter="+str(iter));
	W = 1;						#input: number of scenarios.
	create_files(iter,W);
	
	# initialize the instances.
	ef_mdl = import_file("ef.py").model
	ef_insts=[]
	ef_insts.append(ef_mdl.create_instance(name="ef_instance", filename="ef.dat"))
	solver_manager = SolverManagerFactory("serial")
	solve_all_instances(solver_manager, 'cplex', ef_insts)
	#print ("solving time = ",str(end_time1-start_time1))
	"""
	for i in ef_insts[0].sI:
		for t in ef_insts[0].sT:
			print ("")
			for r in ef_insts[0].sR:
				print ("(%d,%d,%d)=(%d,%d)" %(i,t,r,ef_insts[0].u[i,t,r,1](),ef_insts[0].v[i,t,r,1]())),
	"""			
	#for i in ef_insts[0].sI:
	#	for w in ef_insts[0].Scen:
	#		tmp = [];
	#		for r in ef_insts[0].sR:
	#			tmp.append(ef_insts[0].pLT[i,r,w]);
	#		print (tmp)

	for i in ef_insts[0].sI:
		#print("w_shape["+str(i)+"]="+str(round(ef_insts[0].w_shape[i], 4)))
		#print("w_scale["+str(i)+"]="+str(round(ef_insts[0].w_scale[i], 4)))
		#print("cCR["+str(i)+"]="+str(round(ef_insts[0].pCCR[i], 4)))	
		#print("LT["+str(i)+"]="+str(round(ef_insts[0].pLT[i,:,:], 4)))			
		print("x["+str(i)+"]="+str(round(ef_insts[0].x[i](), 4)))
		for t in ef_insts[0].sT:
			#print ("-----t------",t)
			tmpU = [];
			tmpV = [];
			tmpWs = [];
			tmpZs = [];
			tmpXs = [];
			for r in ef_insts[0].sR:
				#print ("-----r------",r)
				#print("LT", ef_insts[0].pLT[i,r,1])
				for s in ef_insts[0].Scen:
					#tmpU.append(ef_insts[0].u[i,t,r,s]());
					#tmpV.append(ef_insts[0].v[i,t,r,s]());
					tmpWs.append(ef_insts[0].ws[i,t,r,s]());
					#tmpXs.append(ef_insts[0].xs[i,t,r,s]());
					#tmpZs.append(ef_insts[0].zs[t,s]());
			#print("u",tmpU);
			#print("v",tmpV);
			#if sum(tmpWs) > 0:
				#print("t",t+1);
			#print("xs",tmpXs);
			#print("zs",tmpZs);
	print ("objective value=%f" %ef_insts[0].objCost())
	cost.append(ef_insts[0].objCost());
end_time1 = time.clock()
print ("avg time=%d" %((end_time1 - start_time1)/100.0));
print ("average cost");
print (np.average(cost))
print ("cost", cost)

		
