
class BruteForce(object):
    def __init__(self, X, comp_functions):
        self.X = X
        if len(comp_functions) == 1 or len(comp_functions) == X.num_columns - 1 :
            self.comp_functions = comp_functions
        else :
            print('Functions must be one per attribute or only one')
            return
        print(X.num_columns)

class CT(object):

    def __init__(self, X, comp_functions):
        if (len(comp_functions) == 1) or (len(comp_functions) == len(X.columns) - 1) :
            self.X = X
            self.comp_functions = comp_functions
        else :
            print('Functions must be one per attribute or only one')
            return
        print(len(X.columns))
