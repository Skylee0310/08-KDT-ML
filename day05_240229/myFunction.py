import pandas as pd
import numpy as np
from my_function import remove_outlier

file = '../data/iris.csv'
irisDF = pd.read_csv(file)
irisDF = remove_outlier(irisDF, 'sepal.width', 1.5)
print(irisDF)
