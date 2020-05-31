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

