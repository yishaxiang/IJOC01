#Author: Zhicheng Zhu
#Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu

#Info:
#script to control other main file for rolling horizion
#
#Inputs:
#	1. number of components, nComponents.
#	2. setup cost, cS.
#	3. inspection interval, intvl,
#	4. planning horizon, nStages, {0,1,...,nStages-1}
# 	5. initial failure states, kesi,
#	6. initial age, age;
#	7. PR cost, cPR
#	8. CR cost, cCR
#	9. Weibull shape parameter, w_shape
#	10. Weibull scale parameter, w_scale
#Outputs(in file main_dynamic_solver.py):
#	1.CPU time. "print ("calculation time is %f"  %time_elapsed)"
#	2.Objective value. "print (bestObj0);"
#	3.Optimal solution	"print (bestSol0);"

import main_dynamic_solver

import class_info
import copy
import random
import time

import numpy as np
		
##########################
#start from here
##########################
# some fixed parameters
nComponents = 3;		#input: component numbers	
high = 100;
low = 5;
cS = high;				#input: setup cost
intvl = 1;				#input: inspection interval. 
nStages = 6;			#input: planning horizon, 1,2,...,nStages

sysInfo = class_info.system_info(nComponents, nStages, intvl, cS);


kesi = [0]*nComponents;
age = [0]*nComponents;
cPR = [0]*nComponents;
cCR = [0]*nComponents;
w_shape = [0]*nComponents;
w_scale = [0]*nComponents;

for i in range(nComponents):
	#input: initial failure state kesi
	if i==0:
		kesi[i] = 0;
	#input: initial age
	age[i] = 0;
	#input: initial PR cost
	cPR[i] = 1;
	
	#input: Weibull shape parameters
	random.seed(i*20)   
	high = [4, 7];
	low = [1, 3];
	tmp = high;
	temp = random.uniform(tmp[0],tmp[1]);
	w_shape[i] = round(temp,1);		

	
	#input: Weibull scale parameters
	random.seed(i*10)   
	high = [5, 10];
	low = [1, 5];
	tmp = high;  
	temp = random.uniform(tmp[0],tmp[1])#(1,5)
	w_scale[i] = round(temp,1);	
	
	#high = 100;
	#low = 5;
	#cS = low;				#fix setup cost

	#input: CR cost
	random.seed(i*30);
	high = [17, 27];
	low = [6, 16];
	tmp = high
	temp = random.uniform(tmp[0],tmp[1]);#(6,16) (17,27)
	cCR[i] = round(temp,1);		

	
	comInfo = class_info.component_info(i, w_shape[i], w_scale[i], age[i], kesi[i], intvl, cCR[i], cPR[i], cS);
	sysInfo.add_com(comInfo);


sysInfo1 = copy.deepcopy(sysInfo);
main_dynamic_solver.main(sysInfo1);
	
