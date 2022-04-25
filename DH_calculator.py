# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 16:00:54 2021

@author: 14649
"""
"""
import sympy
from sympy import symbols
sympy.init_printing()
x_1, x_2, x_3, x_4, x_5, x_6 = symbols('x_1 x_2 x_3 x_4 x_5 x_6')  # 定义自变量x_1, x_2, x_3, x_4, x_5, x_6
alpha, beta, x, y, gamma = symbols('alpha beta x y gamma')  # 定义参数alpha, beta, x, y, gamma
system = sympy.Matrix((  # 方程参数矩阵，为系数阵的增广矩阵
    (1, 0, x-1, -x, 0, 0, 0),
    (0, 1, 0, 0, -y, y-1, 0),
    (-gamma, 0, 1, 0, 0, 0, 2),
    ((alpha-1)*gamma, -alpha*gamma, 0, 1, 0, 0, -4*alpha+3),
    (-beta*gamma, (beta-1)*gamma, 0, 0, 1, 0, 4*beta-2),
    (0, -gamma, 0, 0, 0, 1, -1)
))
a = sympy.solve_linear_system(system,  # 方程求解函数
                          x_1, x_2, x_3, x_4, x_5, x_6)

for key, value in a.items():  # 输出方程结果
    print('{key}={value}'.format(key=key, value=value))


"""
import sympy
#import numpy as np
sympy.init_printing()
from sympy import symbols,pprint

"""
np.pi / 2
sympy.pi
sympy.cos()
sympy.sin()
"""

alpha_0, a_0, d_1, theia_1 = symbols('alpha_0 a_0 d_1 theia_1') # i = 1
alpha_1, a_1, d_2, theia_2 = symbols('alpha_1 a_1 d_2 theia_2') # i = 2
alpha_2, a_2, d_3, theia_3 = symbols('alpha_2 a_2 d_3 theia_3') # i = 3
alpha_3, a_3, d_4, theia_4 = symbols('alpha_3 a_3 d_4 theia_4') # i = 4

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

"""

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

# sympy.pi sympy.sqrt(2)

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


"""
print("T_0_2 is :")
pprint(sympy.N(T_0_2,2))

print("T_0_3 is :")
pprint(sympy.N(T_0_3,2))

print("T_0_4 is :")
pprint(sympy.N(T_0_4,2))
"""

#M= sympy.Matrix([[d_1, -1], [3, 4], [0, 2]])
#print(np.sin(np.pi / 2))
#print(expr.evalf(subs={x:sympy.pi}))
#N = sympy.Matrix([1, 3])
#print(M*N)
#x = symbols('x')
#expr = sympy.sin(x)
