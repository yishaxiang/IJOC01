This is the source code for paper "Multi-component Maintenance Optimization: A Stochastic Programming Approach." 
by Zhicheng Zhu, Yisha Xiang and Bo Zeng.

Contact:
========
zhicheng.zhu@ttu.edu, yisha.xiang@ttu.edu

Packages:
=========
1. The code should be run in Python 2.x. Python 3 may have compatibility issue.
2. The source codes are relied on Pyomo (http://www.pyomo.org/) and CPLEX.
3. Pyomo version 5.2.0 or 5.5.0; see folder ./support for these Pyomo versions. Higher version may have comatibility issue. 
4. CPLEX 12.8.00 still works for this code. 

Folder structure:
=================
./benders:			Benders decomposition for the two-stage model (model 2), which is also referred to as Algorithm 1 in the paper
./extensive_form:	Solve model 2 as an integer programming.
./ILshape:			Integer L-shaped method for model 2, which is also referred to as Algoithm 2 in the paper.
./PH:				Progressive hedging algorithm for model 2, which is also referred to as Algorithm 3 in the paper.
./PH_Heuristic: 	Progressive hedging algorithm based heuristic algorithm for model 2, which is Algorithm 4 in the paper.
./rolling_horizon:	Use rolling horizon + Algorithm x to approximate the multi-stage model. It also includes two benchmarks
					that used for comparison in the paper.
./support:			Support files, which are Pyomo 5.2.0 and 5.5.0 for the need of the readers.

