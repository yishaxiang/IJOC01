Basic benders decomposition to the two-stage model (model 2).

Code structure:
===============
./main.py:
-----------------
	Program starts from this file. It first calls ./genFile.py to generate the data files needed to ./data . It then 
implement the Benders decomposition, which is relied on the files in ./data, master problem implementation in ./master.py and 
subproblem implementation in ./sub.py
./genFile.py:
-------------
	generate scenario-specific data file in ./data
./sub.py:
--------------------
	sub-problem implementation. The subproblem is LP-relaxed.
./master.py:
--------------------
	master problem implementation.
./data/:
------- 
	Read-only data file for each scenario. Named as ScenNode[x].dat, where [x] is the scenario index, starts from 1.

Notice:
=======
1. Both Pyomo, and CPLEX+Python are used here.

 