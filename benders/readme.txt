Basic benders decomposition to the two-stage model (algorithm 1 for model 2).

Code structure:
===============
./main.py:
-----------------
	Program starts from this file. It first calls ./genFile.py to generate the data files needed to ./data . It then 
implement the Benders decomposition, which is relied on the files in ./data, master problem implementation in ./master.py and 
subproblem implementation in ./sub.py. 
./genFile.py:
-------------
	generate scenario-specific data file in ./data
	It contains the random lifetime seed control. Not recommend to change it.
./sub.py:
--------------------
	sub-problem implementation. The subproblem is LP-relaxed.
./master.py:
--------------------
	master problem implementation.
./data/:
------- 
	Read-only data file for each scenario. Named as ScenNode[x].dat, where [x] is the scenario index, starts from 1.

Important Inputs:
=======
1. See file main.py for
	1.1 number of components
	1.2 planning horizon. 
	1.3 number of scenarios
2. See file genFile.py for
	2.1 PR cost. 
	2.2 CR cost.
	2.3 kesi. Initial failure states
	2.4 Weibull shape parameters. 
	2.5 Weibull scale parameters. 
	2.6 Initial first stage solution.
	2.7. The random lifetime seed control 
	
Notice:
=======
1. Both Pyomo, and CPLEX+Python are used here.

 