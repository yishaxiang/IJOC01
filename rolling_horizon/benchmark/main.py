#Author: Zhicheng Zhu
#Email: zhicheng.zhu@ttu.edu
#Benchmark policy for rolling horizon comparison
#paper:
#A dynamic policy for grouping maintenance activities
#EJOR 1997, Wildeman et al.

#Input:
#	1. number of components, I
#	2. Planning horizon, T, {0,1,...,T-1}
#	3. Setup cost, d
#	4. Weibull scale bounds, wScaleVector
#	5. CR cost bounds, cCrVector
#	6. Weibull shape bound, "sysParams.set_wShapeBound([1,3])"
#	7. PR cost bound, "sysParams.set_cPrBound([1,1])"
#	8. Random seed control, "sysParams.set_ranSeed(ranSeed)"
#Output:
#	1. CPU time, "print ("time             = %d" %time_)"
#	2. Cost of all replicates,"print ("cost"), print (cost)",
#	3. Average cost,"print ("average cost"), print (float(sum(cost))/len(cost))"
#	4. Cost variance, "print ("variance", np.var(cost));"
			

import class_info as myClass
import time
import numpy as np

#decide component next MX time.
def arrange_mx(sysRunning):
	currentTime = sysRunning.currentTime
	endTime = sysRunning.T
	#step 1: find out available moving window. t1 = 0	
	for i in range(sysRunning.comRunningNum):
		#reset nextMxTime to scheduled time point
		#get the widow
		#set failed component's nextMxTime to currentTime
		sysRunning.comRunning[i].cal_movingWindow(currentTime,endTime)
	
	#sort runnning componenet based on their nextMxTime
	sysRunning.sort_running_component()
	
	#step 2: find the optimal group, maximize total saving
	sysRunning.find_group()

def main(wScaleBound, setUpCost, crBound, ranSeed ):
	#
	#
	######################
	#start from here
	######################	
	#
	###
	#Two class objects:
	#1. sysRunning <- component_running <- component_parameters
	#2. sysParams
	###
	###
	#######
	#Step 1: define sysParams: static system info
	#######
	I = 8				#input: number of components
	T = 20				#input: planning horizon. 
	d = setUpCost		#input: setup cost

	sysParams = myClass.system_parameter(I, T, d)
	#define bounds
	sysParams.set_wShapeBound([1,3])		#input: shape parameter
	sysParams.set_wScaleBound(wScaleBound)
	sysParams.set_cCrBound(crBound)			
	sysParams.set_cPrBound([1,1])			#input: PR cost
	#init other parameters
	sysParams.w_shape_init()	
	sysParams.w_scale_init()	
	sysParams.cCr_init()	
	sysParams.cPr_init()
	sysParams.set_ranSeed(ranSeed)
	#print (sysParams.cCr);
	#print (sysParams.wScale);

	########
	#Step 2: define sysRunning: system grouping info
	########
	sysRunning = myClass.system_running(sysParams.T, sysParams.I)

	########
	#Step 3: 
	#component parameters, component running info
	#attach sysParams, sysRunning respectively
	########
	for i in range(sysParams.I):
		com_params = myClass.component_parameters(i, sysParams)
		com = myClass.component_running(i, com_params)
		sysRunning.add_com(com)
		sysRunning.add_comRunning(com)

	######
	#Step 4: begin rolling horizon
	######	

	

	for currentTime in range(sysParams.T):
		sysRunning.set_time(currentTime)
		#print (currentTime)
		#step 1: get residual life
		for i in range(sysRunning.comRunningNum):
			#use currentTime and index i to generate residual life
			sysRunning.comRunning[i].generate_residualLife(currentTime)	

		arrange_mx(sysRunning)
		
		#step 2: check whether there is any component needs to be mx at current time
		sysRunning.mx()
		'''
		#Step 3: reschedule the mx plan	
		if sysRunning.needSchedule == True or \
			sysRunning.newOpp == True:
			arrange_mx(sysRunning)
			
		#step 4: re-mx if new opportunity emerges
		if sysRunning.newOpp == True:	
			sysRunning.mx()
		#step 5: after re-mx. check whether there is any component is replaced.
			if sysRunning.needSchedule == True:
				arrange_mx(sysRunning)
			#it shouldn't be any new opp any more
			if sysRunning.newOpp == False:
				print ("biggggg error!!!")
		'''
	####		
	sysRunning.cal_TotalCost()
	#sysRunning.print_data()
	#sysRunning.print_com()	
		
	return sysRunning.TotalCost



wScaleH = [5, 10]
wScaleL = [1, 5]
wScaleVector = [wScaleL]#[wScaleH, wScaleL]	#input scale parameter
dVector = [100];#100,5						#input: setup cost
cCrH = [17, 27]
cCrL = [6, 16]
cCrVector = [cCrL]							#input: CR cost

counter = 100
print ("=============Benchmark=====================")

for wScale in wScaleVector:
	for d in dVector:
		for cCr in cCrVector:
			counter += 1
			print ("==============scale, d, ccr==================")
			print (wScale),
			print (d),
			print (cCr)
			counter1 = 10
			cost = []
			start_time = time.clock()
			for rep in range(counter,counter+10):
				counter1 += 1
				ranSeed = rep;
				#
				#ranSeed = rep + counter
				tmp = main(wScale, d, cCr, ranSeed)
				#print ("cost[%d] = %f" %(counter1, tmp))
				cost.append(tmp)
			end_time = time.clock()
			time_ = end_time-start_time			
			print ("time             = %d" %time_)
			print ("cost")
			print (cost)
			print ("average cost")
			print (float(sum(cost))/len(cost))
			print ("variance", np.var(cost));
			print ("=============================================")
				

	
	
	
	
	
	
	
	
	
	