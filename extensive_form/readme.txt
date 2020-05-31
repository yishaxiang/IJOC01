Deterministic extensive form (DEF) for the two-stage model (model 2)

For paper: xxxxxxxxx

Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu


Code structure:
===============
./run.py:
--------- 
	main script file, starts from here. Inputs parameters and generate the ./ef.dat file
./ef.py:
-------- 
	extensive form model
./ef.dat: 
-------
	extensive form data.Read-only


Notice:
=======
1. No script to run multiple cases, i.e, different number of component and/or scenarios and/or time horizon.
2. For each experiment, one only need to amend file ./ef.dat for different parameters.
3. "REMEMBER": number of indidividuals changes along with time time horizon in ef.dat, i.e., R = T + 2
