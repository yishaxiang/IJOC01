This code is to implement integer L-shape method to solve stochastic grouping problem in multi-component system.
Which is the Algorithm 2 in the paper

Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu

Code structure:
===============
./data/:
------- 
	data file for each scenario. Named as ScenNode[x].dat, where [x] is the scenario index, starts from 1.
./main_single.py:
-----------------
    main file for single-cut implementation.
./genFile.py:
-------------
	generate scenario-specific data file in ./data
./sub.py (subIP.py):
--------------------
	relaxation (integer) version of sub-problem implementation.

Important Inputs:
=================
a. See file main_single.py for
	1. number of components
	2. planning horizon
	3. number of scenarios
	4. setup cost
b. See file fenFile.py for
	1. Extended planning horizon T_ex;
	2. Initial ag
 	3. PR cost.
	4. CR cost: See function pCCR_init(). 5. Kesi. The initial failure state. 
	6. Weibull shape parameters. 
	7. Weibull scale parameters. 
	8. Initial first stage solution.
	9. Lifetime random seed control.

Notice:
=======
1. We are using python-CPLEX to solve master problem by using branch-and-cut.
2. master problem is built by python-CPLEX.
3. B&C is embeded in CPLEX. So master problem is solved as integer problem.
4. Sub-problem is solved via Pyomo package, solver is CPLEX
 