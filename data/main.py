#Author: Zhicheng Zhu
#Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu
#
#Description:
# Code to generate lifetime examples, to .csv
#
#Input:
#	1. number of components, I
#	2. planning horizon, T
#	3. number of individuals. R
#	4. number of scenarios, W
#	5.initial failure states, kesi, 1 is failed and 0 otherwise
#	6. intial age, age
#	7. w_shape, Weibull shape parameters
#	8 w_scale, Weibull scale parameters
#Output:
#	The lifetime data. Separated in different scenarios. In each scenario, the data size is I*R.
#	Track f for more details

import csv
import random
import math

I = 8;		#number of components.
T=20;		#planning horizon.
R=T+2;		#number of individuals
W= 2000;		#number of scenarios.
w_shape = [];
w_scale = [];
kesi = [];
age = [];
for i in range(I):
	#shape
	random.seed(i*20) ;
	temp = random.uniform(1,3);
	w_shape.append(round(temp,1));
	#scale
	random.seed(i*10) ;
	temp = random.uniform(1,5);
	w_scale.append(round(temp,1));
	#init failure state
	temp = 0;
	if i == 0:
		temp = 0;	
	kesi.append(temp);
	#init age:
	tmp = 0;
	age.append(tmp);	



for idxW in range(W):
	f = open(str(idxW)+".csv","w");
	f_csv = csv.writer(f);
	for idxI in range(I):
		tmp = [0]*R;
		for idxR in range(R):
			random.seed(idxI + idxR+idxW);  
			ran_num = random.uniform(0,1);
			if idxR == 0:
				if kesi[idxI]== 1:
					tmp[0]  = 0	#force to replace the first individual	
				else:
					part1 = math.log(ran_num);
					s_inv = 1.0/w_shape[idxI];
					part2 = (age[idxI]/w_scale[idxI])**w_shape[idxI];
					part3 = part2 - part1;
					tmp[idxR] = max(1,round((part3**s_inv)*w_scale[idxI]) - age[idxI]);
					tmp[idxR] = int(tmp[idxR]);
			else:
				ran_num_log = -math.log(ran_num)
				s_inv = 1.0/w_shape[idxI]
				LT1 = round((ran_num_log**s_inv)*w_scale[idxI])
				tmp[idxR] = int(max(1,LT1))	
		
    		f_csv.writerow(tmp);
	f.close();