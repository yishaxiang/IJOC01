Rolling horizon Algorithm 4(PH_Heuristic) in the paper

Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu, zhich.zhu@gmail.com



Code structure:
===============
./class_info.py
---------------
	Class information.
./main.py:
-----------------
    main file.
	rolling horizon version of Algorithm 4

Important Inputs:
=================
See file main.py for
	1. number of components.
	2. planning horizon.
	3. number of scenarios.
	4. number of replicates.
	5. extended planning horizon.
	6. initial age.
	7. setup cost.
	8. inspection interval.
	9. PR cost.
	10. CR cost bounds.
	11. Weibull shape parameter bounds.
	12. Weibull scale parameter bounds.
	13. Lifetime random seed control.
	14. Failure random see control in rolling horizon.
	15. Initial failure states, kesi
	16. PHA inputs, rho, eps, maximum iteration:max_iter
	17. Heuristic algorithm inputs, \Delta: , \iota:  
