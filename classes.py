import numpy as np
import pandas as pd

"""
X: The Pandas data set.
comp_array: The array of values to compare two rows.
comp_function: A lambda function for comparing for determining how to compare the values.
"""

def diffmatrix(X, comp_array, comp_function):
    #Get number of rows
    num_rows = len(X)
    #Obtain classes and the index of the first appearance
    classes = []
    classes_index = []    
    for i in X.itertuples():
        if i[-1] not in classes:
            classes.append(i[-1])
            classes_index.append(i[0])
  
    #From the first to the n-1 class
    for i in xrange(classes[-1]-1):
        #Starting at the first appearance of the class i and ends on the class i+1 first index
        for j in xrange(classes_index[i], classes_index[i+1]):
            #From the end of the i class to the end of the data
            for k in xrange(classes_index[i+1], num_rows):
               #Compares based on a lambda the j-th row with the other k rows
               print(','.join(map(str, map(comp_function,X.loc[j][:-1],X.loc[k][:-1],comp_array))))

#Calculate the testors making all the comparations with the matrix rows
class BruteForce(object):
    def __init__(self, X, comp_array, comp_function):
        self.X = X
        self.comp_array = comp_array
        self.comp_function = comp_function
    
    #Returns an array of typycal testors
    def calculate_testors(self):
        dmatrix = diffmatrix(self.X, self.comp_array, self.comp_function)

class CT(object):

    def __init__(self, X, comp_array, comp_function):
        self.X = X
        self.comp_array = comp_array
        self.comp_function = comp_function
        print("Not implemented yet")
