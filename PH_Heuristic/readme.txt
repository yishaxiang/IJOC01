This code is to implement progressive hedging based heuristc algorithm to solve stochastic grouping problem in multi-component system.
Which is the Algorithm 4 in the paper.


Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu



Code structure:
===============
	
./main.py:
-----------------
    main file.

Important Inputs:
=================
See file main.py for
	1. number of components.
	2. planning horizon. 
	3. number of scenarios. 
	4. extended planning horizon.
	5. initial age
	6. setup cost
	7. inspection interval.
	8. PR cost
	9. CR cost bounds
	10. Weibull shape parameter
	11. Weibull scale parameter bounds
	12. Lifetime random seed control
	13. Initial failure states
	14. PHA inputs, rho, eps, maximum iteration
	15. Heuristic algorithm inputs, \Delta , \iota 
See file class_info.py for
	1. Lifetime random seed control.