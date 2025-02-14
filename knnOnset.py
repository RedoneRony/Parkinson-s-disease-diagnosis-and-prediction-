# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 22:01:34 2019

@author: rony-CSE
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:58:31 2019

@author: rony-CSE
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:54:29 2019

@author: rony-CSE
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:21:12 2019

@author: rony-CSE
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('D://work/for thesis/new alogorithm try/pd.csv')
X = dataset.iloc[:,[1,2]].values
y = dataset.iloc[:,5].values

#z = pd.DataFrame(y)
'''
#missing values
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
y = np.array(y).reshape(-1,1)
imputer = imputer.fit(y)
y = imputer.transform(y)'''

#encoding categorical data

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X= LabelEncoder()
X[:,1] = labelencoder_X.fit_transform(X[:,1])



labelencoder_y = LabelEncoder()
y = labelencoder_X.fit_transform(y)

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.35, random_state = 0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.45, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('KNN (train data)')
plt.xlabel('Human Age and Gender')
plt.ylabel('Duration of disease from first symptoms (years)')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.45, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('KNN (Test set)')
plt.xlabel('Human Age and Gender')
plt.ylabel('Duration of disease from first symptoms (years)')
plt.legend()
plt.show()






