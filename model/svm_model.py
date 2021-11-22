from sklearn import datasets 
from sklearn.metrics import confusion_matrix 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler

import pandas as pd
import os


  
# loading the iris dataset 
  
# X -> features, y -> label
def model(test):
    dataset_path = 'cards'
    x_all_d = pd.read_csv('model/x_train.csv')
    X = x_all_d.values
    A, F = X.shape
    
    y_all_d = pd.read_csv('model/y_train.csv')
    y = y_all_d.values.reshape((A,))
      
    # dividing X, y into train and test data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 
      
    # training a linear SVM classifier 
    from sklearn.svm import SVC 
    svm_model_linear = SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 
    svm_predictions = svm_model_linear.predict(X_test) 
    print(svm_predictions)
    # model accuracy for X_test   
    accuracy = svm_model_linear.score(X_test, y_test) 
    print("test accuracy: ", accuracy)
    # creating a confusion matrix 
    cm = confusion_matrix(y_test, svm_predictions) 
    
    return svm_model_linear.predict(test.reshape(1,-1))
    
def fit():
    dataset_path = 'cards'
    x_all_d = pd.read_csv('model/x_train.csv')
    X = x_all_d.values
    A, F = X.shape
    
    y_all_d = pd.read_csv('model/y_train.csv')
    y = y_all_d.values.reshape((A,))
      
    # dividing X, y into train and test data 
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0) 
      
    # training a linear SVM classifier 
    from sklearn.svm import SVC 
    return SVC(kernel = 'linear', C = 1).fit(X_train, y_train) 
    
def predict(estimator, test):
    return estimator.predict(test.reshape(1,-1))

if __name__ == '__main__':
    model(None)