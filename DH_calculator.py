# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:00:54 2021

@author: Chuanlong Zang
"""

import sympy
#import numpy as np
sympy.init_printing()
from sympy import symbols,pprint

############# region 1: Here is nothing to be changed if you are computing a 4-link robot arm #############
alpha_0, a_0, d_1, theia_1 = symbols('alpha_0 a_0 d_1 theia_1') # i = 1
alpha_1, a_1, d_2, theia_2 = symbols('alpha_1 a_1 d_2 theia_2') # i = 2
alpha_2, a_2, d_3, theia_3 = symbols('alpha_2 a_2 d_3 theia_3') # i = 3
alpha_3, a_3, d_4, theia_4 = symbols('alpha_3 a_3 d_4 theia_4') # i = 4

# classic DH transformation
T_0_1 = sympy.Matrix([[sympy.cos(theia_1), -sympy.sin(theia_1), 0, a_0], 
                      [sympy.sin(theia_1)*sympy.cos(alpha_0), sympy.cos(theia_1)*sympy.cos(alpha_0), -sympy.sin(alpha_0), -sympy.sin(alpha_0)*d_1],
                      [sympy.sin(theia_1)*sympy.sin(alpha_0), sympy.cos(theia_1)*sympy.sin(alpha_0), sympy.cos(alpha_0), sympy.cos(alpha_0)*d_1],
                      [0, 0, 0, 1]])

T_1_2 = sympy.Matrix([[sympy.cos(theia_2), -sympy.sin(theia_2), 0, a_1], 
                      [sympy.sin(theia_2)*sympy.cos(alpha_1), sympy.cos(theia_2)*sympy.cos(alpha_1), -sympy.sin(alpha_1), -sympy.sin(alpha_1)*d_2],
                      [sympy.sin(theia_2)*sympy.sin(alpha_1), sympy.cos(theia_2)*sympy.sin(alpha_1), sympy.cos(alpha_1), sympy.cos(alpha_1)*d_2],
                      [0, 0, 0, 1]])

T_2_3 = sympy.Matrix([[sympy.cos(theia_3), -sympy.sin(theia_3), 0, a_2], 
                      [sympy.sin(theia_3)*sympy.cos(alpha_2), sympy.cos(theia_3)*sympy.cos(alpha_2), -sympy.sin(alpha_2), -sympy.sin(alpha_2)*d_3],
                      [sympy.sin(theia_3)*sympy.sin(alpha_2), sympy.cos(theia_3)*sympy.sin(alpha_2), sympy.cos(alpha_2), sympy.cos(alpha_2)*d_3],
                      [0, 0, 0, 1]])

T_3_4 = sympy.Matrix([[sympy.cos(theia_4), -sympy.sin(theia_4), 0, a_3], 
                      [sympy.sin(theia_4)*sympy.cos(alpha_3), sympy.cos(theia_4)*sympy.cos(alpha_3), -sympy.sin(alpha_3), -sympy.sin(alpha_3)*d_4],
                      [sympy.sin(theia_4)*sympy.sin(alpha_3), sympy.cos(theia_4)*sympy.sin(alpha_3), sympy.cos(alpha_3), sympy.cos(alpha_3)*d_4],
                      [0, 0, 0, 1]])
############# region 1 ended #############


############# region 2: Here you need to input your known parameters (real numbers), if any #############

""" something that might be frequently used
np.pi / 2
sympy.pi
sympy.cos()
sympy.sin()
sympy.sqrt(2)
"""

# if you want something parameterized, comment the parameters as below!
T_0_1_eva=T_0_1.evalf(subs={alpha_0:0,
                        a_0:2,
                        d_1:0,
                        #theia_1:-sympy.pi/2
                        })

T_1_2_eva=T_1_2.evalf(subs={alpha_1:-sympy.pi/2,
                        a_1:2,
                        d_2:0,
                        #theia_2:0
                        })

T_2_3_eva=T_2_3.evalf(subs={alpha_2:-sympy.pi/2,
                        a_2:2,
                        d_3:0,
                        #theia_3:sympy.pi
                        })

T_3_4_eva=T_3_4.evalf(subs={alpha_3:sympy.pi/2,
                        a_3:2,
                        d_4:0,
                        #theia_4:0
                        })

""" initial state (all 0 - no rotation and no translation)

T_0_1_eva=T_0_1.evalf(subs={alpha_0:0,
                        a_0:0,
                        d_1:0,
                        theia_1:0
                        })

T_1_2_eva=T_1_2.evalf(subs={alpha_1:0,
                        a_1:0,
                        d_2:0,
                        theia_2:0
                        })

T_2_3_eva=T_2_3.evalf(subs={alpha_2:0,
                        a_2:0,
                        d_3:0,
                        theia_3:0
                        })

T_3_4_eva=T_3_4.evalf(subs={alpha_3:0,
                        a_3:0,
                        d_4:0,
                        theia_4:0
                        })
"""
############# region 2 ended #############


############# region 3: Here you need to adjust your output if you don't need all outputs! #############

T_0_2=T_0_1_eva*T_1_2_eva

T_0_3=T_0_1_eva*T_1_2_eva*T_2_3_eva

T_0_4=T_0_1_eva*T_1_2_eva*T_2_3_eva*T_3_4_eva

print("T_0_1 is :")
pprint(sympy.N(T_0_1_eva,2))

print("T_1_2 is :")
pprint(sympy.N(T_1_2_eva,2))

print("T_2_3 is :")
pprint(sympy.N(T_2_3_eva,2))

print("T_3_4 is :")
pprint(sympy.N(T_3_4_eva,2))

print("T_0_2 is :")
pprint(sympy.N(T_0_2,2))

print("T_0_3 is :")
pprint(sympy.N(T_0_3,2))

print("T_0_4 is :")
pprint(sympy.N(T_0_4,2))

############# region 3 ended #############

