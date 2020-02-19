# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 07:19:51 2020

@author: V Ojha
"""
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
#                                                                             #
#                          From Python to MATALB                              #
#                                                                             #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

import matlab.engine
eng = matlab.engine.start_matlab()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
#                                                                             #
#                Communication: From Python to MATALB                         #
#                                                                             #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#

#% inbuilt MATLAB functions test

# MATLAB inbuilt array test
tf = eng.isprime(37)
print('Is True:',tf)

# MATLAB inbuilt array test
vec = matlab.int8([1,2,3,4,5])
suma = eng.sum(vec)
print('Suma: ',suma)
#%% custom script test
# Addpath to locate MATLAB scrips

eng.addpath(r'C:\Users\~\~\PythonMATLAB','-end')


# Call the script - which has no function
###############################################################################
#                        NEED TO COMPLIE TWICE                                #
###############################################################################
suma1 = eng.summation(nargout=0)
print('Suma: ',suma1)
print('Answer is None becase there is no return value from sumation.m')

# Editeing a script 
eng.edit('summation',nargout=0)

# calling a function without argument
suma2 = eng.summationFunNoArg()
print('Suma: ',suma2)

# calling a function with arguments
suma2 = eng.summationFunArg(5,10)
print('Suma: ',suma2)

#eng.edit('matlabScript',nargout=0)
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
#                                                                             #
#           Bi-directional Communication: From Python to MATALB               #
#                                                                             #
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#
suma3 = eng.communication(5,10)
print('Suma: ',suma3)

