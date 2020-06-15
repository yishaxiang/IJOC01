This code is to implement progressive hedging algorithm to solve stochastic grouping problem in multi-component system.
Which is the Algorithm 3 in the paper:


Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu



Code structure:
===============
./models/:
--------- 
	ReferenceModel.py: problem model. It has to be named as this because of "runph" script
./nodedata/: 
-------------
	ScnearioStructure.dat: register file. Register user-defined file to the hook of "runph" script.
	RootNode.dat: shared parameters across different scenarios.
	ScenNode[x].dat: scenario-specific parameters
./result/:
----------
	result files
./main.py:
-----------------
    main file.
	create files in ./nodedata/ .
	call runph script.

Important Inputs:
=================
See file main.py for
	1. number of components.
	2. planning horizon.
	3. number of scenarios.
	4. extended planning horizon.
	5. initial age.
	6. setup cost.
	7. PR cost.
	8. CR cost.
	9. Weibull shape parameter.
	10. Weibull scale parameter.
	11. Lifetime random seed control.
	12. Initial failure states, kesi.


Notice:
=======
1. runph script from Pyomo/PySP package is used for solving standard progressive hedging problem.
2. runph requires:
	2.1 a model file: ./models/ReferenceModel.py
	2.2 a register file: ./nodedata/ScnearioStructure.dat
	2.3 some user-defined files for different scenarios
3. For more questions, one can refer http://www.pyomo.org/documentation/
 