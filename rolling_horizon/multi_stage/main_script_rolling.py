#Author: Zhicheng Zhu
#Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu

#Info:
#script to control other main file for rolling horizion
#
#!/usr/bin/python


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
	
