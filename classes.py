import numpy as np
import pandas as pd

def diffmatrix(X, comp_functions):
    #Obtain the standart deviation for each column except the last (class)
    X_stdvect = X.ix[:,:-1].apply(comp_functions[0], 0)
    #Get number of rows and columns
    (numr, labels) = X.shape
    #Obtain classes and the index of the first appearance
    classes = []
    classes_index = []
    comparator = lambda x,y,z: 1 if x + z > y and x - z < y else 0
    
    for i in X.itertuples():
        if i[-1] not in classes:
            classes.append(i[-1])
            classes_index.append(i[0])
  
    
    for i in xrange(classes[-1]-1):
        for j in xrange(classes_index[i], classes_index[i+1]):
            for k in xrange(classes_index[i+1], numr):
               print(','.join(map(str, map(comparator,X.loc[j][:-1],X.loc[k][:-1],X_stdvect))))
    
    
    #for i in xrange(numr-1):
    #    for j in xrange(i+1, numr):
    #        if X.loc[i][-1] != X.loc[j][-1]:
    #            print(str(i) + ',' + str(j))
    #            print(','.join(map(str, map(comparator,X.loc[i][:-1],X.loc[j][:-1],X_stdvect))))
    #            
#def basicmatrix():


def compare(row1, row2, tolerance):
    new_row = row1
    
    

class BruteForce(object):
    def __init__(self, X, comp_functions=[np.std]):
        self.X = X
        if len(comp_functions) == 1 or len(comp_functions) == len(X.columns) - 1 :
            self.comp_functions = comp_functions
        else :
            print('Functions must be one per attribute or only one')
            return
    
    #Returns an array of testors
    def calculate_testors(self):
        dmatrix = diffmatrix(self.X, self.comp_functions)
        #bmatrix = basicmatrix(dmatrix)

class CT(object):

    def __init__(self, X, comp_functions):
        if (len(comp_functions) == 1) or (len(comp_functions) == len(X.columns) - 1) :
            self.X = X
            self.comp_functions = comp_functions
        else :
            print('Functions must be one per attribute or only one')
            return
        print(len(X.columns))
