from __future__ import annotations
import collections
from collections import defaultdict
import numbers
from river import base, stats 
from scipy.stats import chi2_contingency
class ChiSquare(base.Transformer):
    def __init__(self):
        #initlize chi-sq test.
        self.observed_frequencies = defaultdict(lambda: defaultdict(int))
        self.total_samples = 0
        print("initalisation works!!")
    def update(self, x, y):
        # Updates observed & expected frequency based on the incoming data (x, y)
        self.observed_frequencies[x][y] += 1
        self.total_samples += 1
        print("Update func works!!!")

    '''
    Area to work on. Code is not giving the desired output.
    Find the issue: (Is it the lib implementation or stats compution?)
    
    '''
    def chi_squared_test(self):
        observed_matrix = [
            [self.observed_frequencies[x][y] for y in self.observed_frequencies[x]]
            for x in self.observed_frequencies] 
        _, p_value, _, _ = chi2_contingency(observed_matrix)
        return p_value
    def transform_one(self, x):
        # Return the p-value for the chi-squared test
        return self.chi_squared_test()
    def transform_many(self, X):
        return [self.transform_one(x) for x in X]
    def reset(self):
        self.observed_frequencies = defaultdict(lambda: defaultdict(int))
        self.total_samples = 0

