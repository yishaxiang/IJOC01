#Author: Zhicheng Zhu
#Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu
#
#Description:
#  main file script for basic Benders decomposition using Pyomo.
#
###input:
#	1. comp_list: it is a list of the numbers of components we need to conduct the experiment.
#				for example, if we need to conduct an expriment with n=4, then we only need to put 4 in it.
#				The list structure allows us to run multiple experiments in batches.
#	2. time_list: planning horizon list. For each T in the list, the planning horizon is {0,1,...,T}.
#	3. scen_list: the list of number of scenarios.
#	4. directory: the folder path of this file. For example, C:\\Users\\JohnDoe\\Desktop\\code\\benders
#	5. max_iterations: maximum number of iterations allowed for Benders decomposition.
###output:
#	1. number of converge iterations.
#	2. CPU time
#	3. number of cuts used
#	4. objective value of the master problem.
#	5. objective values of each scenario subproblem.


from pyutilib.misc import import_file
from pyomo.environ import *
from pyomo.opt import SolverFactory
from pyomo.opt.base import SolverFactory
from pyomo.opt.parallel import SolverManagerFactory
from pyomo.opt.parallel.manager import solve_all_instances
import pdb
import time
import genFile
import os

comp_list = [4]					#input: number of components
time_list = [9]					#input: length of planning horizon, starts from 0.
scen_list = [1080]				#input: number of scenarios
counter = 0
directory = "xxxxx" 			#input:data file directory. This should be the path of this file.
for I in comp_list:
	for T in time_list:
		for w in scen_list:
			#excmd = "python genFile.py " + str(I) + " " + str(T) + " " + str(w)
			#os.system(excmd)
			counter += 1
			print (str(counter) + "_" + str(I) + "_" + str(T) + "_" + str(w))
			#
			#generate .dat files for master problem and sub-problems in $directory/data folder
			#
			genFile.create_allFiles(I,T,w,directory)
			start_time1 = time.clock()
			# import the master model
			master_path = directory + "\\data\\master.dat"
			mstr_mdl = import_file("master.py").model
			# initialize the master instance.
			mstr_inst = mstr_mdl.create_instance(master_path)
			
			# import sub-problem model
			sb_mdl = import_file("sub.py").model
			# initialize the sub-problem instances.
			sub_insts = []
			for s in mstr_inst.Scen:
				sub_path = directory + "\\data\\ScenNode" + str(s) + ".dat"
				sub_insts.append(
					sb_mdl.create_instance(name="sub"+str(s), \
									   filename=sub_path))
				#print ("instance name = %s" %sub_insts[-1].name)
			# initialize the solver manager.
			solver_manager = SolverManagerFactory("serial")
			# initialize sita of in master problem
			for i in mstr_inst.Scen:
				mstr_inst.sita[i] = float("-Inf")

			max_iterations = 50;			#input: the maximum number of iterations allowed.
			#indicate each subproblem cut converged or not
			cut_num = 0

			end_time1 = time.clock()
			print ("loading time = ",str(end_time1-start_time1))
			# main benders loop.
			start_time = time.clock()
			for ii in range(1, max_iterations+1):
				flag_sita = [0 for i in range(0,mstr_inst.NUMSCEN())] 
				#print("\nIteration=%d"%(ii))
				#solve the subproblem
				solve_all_instances(solver_manager, 'cplex', sub_insts)
				#start multi-cut
				for s, inst in enumerate(sub_insts, 1):
					Lbound = mstr_inst.prob*inst.oSub()					#get lower bound from second-stage obj. 
					#print("Lower bound ["+str(s)+"]= " \
					#                       +str(round(Lbound, 4)))
					#print("Upper bound ["+str(s)+"]"\
					#	+str(round(mstr_inst.sita[s].value, 4)))
						
					newgap = round(mstr_inst.sita[s].value - \
								Lbound, 6)
					newgap = abs(newgap)

					if newgap <= 0.01:
						#flag_sita == 1 means convergence for this scenario, no benders cut is needed
						flag_sita[s-1] = 1								
						continue
						#print("scenario["+str(s)+"]converged")

					cut_num	= cut_num + 1		
					#
					#start to generate benders cut
					#
					cut = 0
					#constraint g
					for i in inst.scg:
						cut += inst.dual[inst.cSg[i]]
					
					#constraint p
					for i in inst.sI:
						for t in inst.sT:
							cut += inst.dual[inst.cSp[i,t]]*(-1)
					
					#constraint q,r,s,t
					for i in inst.sI:
						for t in inst.sT:
							for r in inst.sR:
								cut += inst.dual[inst.cSq[i,t,r]]
								cut += inst.dual[inst.cSr[i,t,r]]
								cut += inst.dual[inst.cSs[i,t,r]]
								cut += inst.dual[inst.cSt[i,t,r]]
					#constraint s1
					for i in inst.sI:
						for r in inst.sR_0:
							cut += 2*inst.dual[inst.cSs1[i,r]]
					#constraint u
					for t in inst.sT_0:
						cut += inst.dual[inst.cSu[t]]	
					#constraint v
					for i in inst.sI:
						for t in inst.sT_ex:
							for r in inst.sR:
								cut += inst.dual[inst.cSv[i,t,r]]
					cut = mstr_inst.prob*cut
					#print "added cut"
					#print cut,
					#constraint i
					for i in inst.sI:
					#	print ("+%f*x[%d]" %(mstr_inst.prob*inst.dual[inst.cSi[i]],i)),
						cut += mstr_inst.prob*inst.dual[inst.cSi[i]]*mstr_inst.x[i]
					#print ""
					mstr_inst.Cut_Defn.add(mstr_inst.sita[s] >= cut)
				
				if flag_sita.count(0) == 0:
					#all scenarios are converged
					#print("Multicut converged!!")
					break
				# re-solve the master and update the subproblem inv1 values.
				solve_all_instances(solver_manager, 'cplex', [mstr_inst])
				#print "solving master problem:"
				#for i in mstr_inst.sI:
				#	print("x["+str(i)+"]="+str(round(mstr_inst.x[i](), 4)))
				#print ("objective value=%f"  %mstr_inst.oMaster())
				#for p in mstr_inst.Scen:
				#	print("objective valule ["+str(p)+"]"+str(round(mstr_inst.sita[p].value, 4)))

				for instance in sub_insts:
					for i in instance.sI:
						instance.x[i] = max(mstr_inst.x[i](),0)

			else:
				# this gets executed when the loop above does not break
				print("Maximum Iterations Exceeded")

			end_time = time.clock()
			CPU_time = end_time - start_time
			#print("\nConverged master solution values:")
			print ("iterations="),
			print (ii)
			print ("CPU time="),
			print (CPU_time)
			print ("cut="),			
			print (cut_num)														#output number of cuts.
			for i in mstr_inst.sI:
				print("x["+str(i)+"]="+str(round(mstr_inst.x[i](), 4)))
			print ("objective value=%f" %mstr_inst.oMaster())					#output: objective values
			for p in mstr_inst.Scen:
				print("objective valule ["+str(p)+"]"+str(round(mstr_inst.sita[p].value, 4)))	#output: objective values for each scenario

				
