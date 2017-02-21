# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:21:39 2017

@author: Ronak
"""

from random import randint
from sklearn.linear_model import LogisticRegression
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.svm import LinearSVC


calintake=[]
calburnt=[]
labels=[]
for i in xrange(500):
    calintake.append(randint(1000,12000))
    calburnt.append(randint(500,10000))
    labels.append(randint(0,1))
x= pd.DataFrame(calintake,calburnt)
X_train, X_test, y_train, y_test= train_test_split(x,labels, test_size=0.2, random_state=42)
clf= LinearSVC()
clf.fit(X_train, y_train)
score= clf.score(X_test,y_test)
print score
