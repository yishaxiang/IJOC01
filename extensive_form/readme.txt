Deterministic extensive form (DEF) for the two-stage model 

Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu


Code structure:
===============
./run.py:
--------- 
	main script file, starts from here. Inputs parameters and generate the ./ef.dat file
	We only need to change the input in this file for different experiments. 
	The detail input and output information can be found inside the file.
./ef.py:
-------- 
	extensive form model
./ef.dat: 
-------
	extensive form data.Read-only

Important Inputs:
=================
a. See file run.py for
	1. number of componetns.
	2. planning horizon.
	3. Extensive planning horizon.
	4. setup cost.
	5. initial age. 
	6. number of scenario.
b. See file ef.py for
	1. PR cost.
	2. CR cost.
	3. Kesi. 	
	4. Weibull shape parameters. 
	5. Weibull scale parameters. 

Notice:
=======
1. No script to run multiple cases, i.e, different number of component and/or scenarios and/or time horizon.
2. For each experiment, one only need to amend file ./ef.dat for different parameters.
3. "REMEMBER": number of indidividuals changes along with time time horizon in ef.dat, i.e., R = T + 2
