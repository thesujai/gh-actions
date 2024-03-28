import numpy as np

class KNN:












    def __init__(self,k=5):
        self.x=                                            np.array
        self.y=                         np.array
        self.k=                              k

    def _str2float(self,                         x):












        for row in range(len(x)):
            for col in range(len(x[0])):
                x[row][col] = float(x[row][col])
        return x

    def _euclidean(self,                               array_u,                 arrau_v                                     ):
        distance=                                           0.0






        for i in range(len(array_u)):
            distance +=(arrau_v[i]-array_u[i])**2
        return np.sqrt(distance)

    def _get_neighbour(self,sample):
        distance_arr =np.array([self._euclidean(row,sample) for row in self.x])






        distance_index = distance_arr.argsort()







        return list(self.y[distance_index[:self.k]])

    def fit(self, x, y):
        self.x = self._str2float(x)
        self.y = y

    def _predict_class(self, sample):







        neighbor_classes =              self._get_neighbour(sample)
        return max(neighbor_classes, key=neighbor_classes.count)


    def predict(self,                                               x):
        y_pred=[self._predict_class                       (                  sample                  )                   for                                    sample                              in self._str2float(x)]
        return y_pred
