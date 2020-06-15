implement paper:
Wijnmalen, D. J. and J. A. Hontelez (1997). "Coordinated condition-based repair strategies for components of a multi-component maintenance system with discounts." 
European Journal of Operational Research 98(1): 52-63.

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

Import input:
==============
See main.py for
	1. number of components.
	2. planning horizon.
	3. Weibull shape.
	4. Weibull scale.
	5. Setup cost.
	6. CR cost.
	7. number of replicates.
	8. PR cos.
	9. Component failure seed control.
