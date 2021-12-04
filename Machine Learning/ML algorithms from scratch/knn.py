import numpy as np
from collections import defaultdict

class KNeighborsClassifier:
    '''Implementation from scratch of the KNN algorithm

        The following metrics will be implemented : 
            - Manhattan
            - Euclidean
            - Chebyshev
    '''

    def __init__(self, n_neighbors=5, metric='euclidean'):
        self.n_neighbors = n_neighbors
        self.metric = self.set_metric(metric)

    def fit_predict(self, X, y, X_infer, regression=False):
        '''Compute the distances for each test point, select the K
        closest points in the training set.
        Then, predict the current observation based on the given problem.
        
        If regression is False, consider the "majority class", 
        otherwise, take the average. 
        '''

        distances = defaultdict(list) # save test_idx : [(target,distance),...]

        for x_test in X_infer:
            # iterate on the train data
            for x_train,y_train in zip(X,y):
                distance = self.compute_distance(x_test,x_train)
                distances[x_test].append((y_train,distance))

        # select the K nearest neighbors 



    def set_metric(self,metric):
        '''Set the metric used for calculating the distances
        between points
        
        Args:
            metric (str) : distance metric provided by the user
        Returns:
            return the given metric if it has been implemented, otherwise
            raise an Error
        '''    
        if metric in ['euclidean']:
            return metric
        else:
            raise ValueError('{} has not been implemented - refer to [euclidean,manhattan,chebyshev]'.format(metric))

    def compute_distance(self, v1,v2):
        '''Compute the distance, according to the selected one'''

        if self.metric == 'euclidean':
            return self.euclidean_distance(v1,v2)
        elif self.metric == 'manhattan':
            return self.manhattan_distance(v1,v2)
        elif self.metric == 'chebyshev':
            return self.chebyshev_distance(v1,v2)

    def manhattan_distance(self, v1, v2):
        '''Compute the Manhattan distance between x1 and x2
                \sum_i | v1_i - v2_i | 
        '''
        v1, v2 = np.array(v1), np.array(v2) # convert to np arrays

        if not v1 or not v2:
            raise ValueError('The Manhattan distance cannot be computed from None')
        if len(v1) != len(v2):
            raise ValueError('Cannot compare arrays with different lengths ({},{})'.format(len(v1),len(v2)))
        if np.isnan(v1).any() or np.isnan(v2).any():
            raise ValueError('Cannot compare arrays with NaN values ({},{})'.format(np.isnan(v1).any(),np.isnan(v2).any()))
        
        return np.sum(np.abs((v1-v2)))

    def euclidean_distance(self, v1, v2):
        '''Compute the euclidean distance between x1 and x2
                \sqrt { \sum {v1_i - v2_i}^2 }
        '''
        v1, v2 = np.array(v1), np.array(v2) # convert to np arrays

        if v1 == None or v2 == None:
            raise ValueError('The euclidean distance cannot be computed from None')
        if len(v1) != len(v2):
            raise ValueError('Cannot compare arrays with different lengths ({},{})'.format(len(v1),len(v2)))
        if np.isnan(v1).any() or np.isnan(v2).any():
            raise ValueError('Cannot compare arrays with NaN values ({},{})'.format(np.isnan(v1).any(),np.isnan(v2).any()))
        
        return np.sqrt(np.sum((v1-v2)**2))

    def chebyshev_distance(self, v1, v2):
        '''Compute the Chebyshev distance between x1 and x2
                \max_i |v1_i - v2_i|
        '''
        v1, v2 = np.array(v1), np.array(v2) # convert to np arrays

        if v1 == None or v2 == None:
            raise ValueError('The Chebyshev distance cannot be computed from None')
        if len(v1) != len(v2):
            raise ValueError('Cannot compare arrays with different lengths ({},{})'.format(len(v1),len(v2)))
        if np.isnan(v1).any() or np.isnan(v2).any():
            raise ValueError('Cannot compare arrays with NaN values ({},{})'.format(np.isnan(v1).any(),np.isnan(v2).any()))
        
        return np.max(np.abs(v1-v2))
        

if __name__ == '__main__':
    knn = KNeighborsClassifier(n_neighbors=5, metric='euclidean')