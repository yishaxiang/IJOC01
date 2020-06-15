implement paper:
A dynamic policy for grouping maintenance activities
EJOR 1997, Wildeman et al.

Code author: Zhicheng Zhu
Email: zhicheng.zhu@ttu.edu


Code structure:
===============
./main.py:
-----------------
    main file.
./class_info.py:
----------------
	all 4 classes in main.py:
	1. system_parameter: system static information
	2. component_parameters: component static information
	3. component_running: component running information. Dynamically changing in program
	4. system_running: system running information. Dynamically changing in program

Important Inputs:
=================
See file main.py for
	1. number of components
	2. Planning horizon.
	3. Setup cost.
	4. Weibull scale bounds.
	5. CR cost bounds.
	6. Weibull shape bound.
	7. PR cost bound.
	8. Random seed control.

Notice:
=======
1. It's using age-based maintenance + perfect maintainenace here.
   Reference paper: block-based maintenance + minimum repair
2. It's a rolling horizon version.
 