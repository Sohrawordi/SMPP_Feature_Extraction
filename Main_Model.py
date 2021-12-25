# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 10:37:40 2021

@author: Md. Sohrawordi
"""

import pandas as pd
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.metrics import matthews_corrcoef
from sklearn.svm import SVC


positive=pd.read_csv('Numerical_Moment_features/positive_numerical_moment_samples.csv')
negative=pd.read_csv('Numerical_Moment_features/negative_numerical_moment_samples.csv') 






class_label=[]
for i in range (len(positive.index)):
    class_label.append(1)





for i in range (len(negative.index)):
    class_label.append(0)



sample=pd.concat([positive,negative], ignore_index=True, sort =False)
raw_cols=sample.columns


X=sample
y=class_label

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
x_data=scaler.transform(X)
x_data=pd.DataFrame(x_data, columns=raw_cols)   

classifier =SVC(kernel='rbf', C=1,gamma=0.017,probability=True, class_weight={0:2,1:3}) 

cv = KFold(n_splits=10)


y_pred = cross_val_predict(classifier, x_data, y, cv = cv)

print(classification_report(y, y_pred))

print("Accuracy Score: "+str(accuracy_score(y,y_pred)))
print("Confusion_matrix :")


cm=confusion_matrix(y,y_pred)
print(cm)



TP = cm[1,1] # true positive 
TN = cm[0,0] # true negatives
FP = cm[0,1] # false positives
FN = cm[1,0] # false negatives
acc=(TP+TN)/(TP+TN+FP+FN)
sn=TP / (TP + FN)
sp =TN / (TN + FP)


print('Sensitivity : ', sn)


print('Specificity : ', sp)

print("Matthews correlation coefficient (MCC): ",matthews_corrcoef(y, y_pred))



#Distribution of y 
print('y actual : \n' +  str(pd.Series(y).value_counts()))
#Distribution of y predicted
print('y predicted : \n' + str(pd.Series(y_pred).value_counts()))


from sklearn.model_selection import cross_val_predict
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt

# calculate roc curve
fpr, tpr, thresholds = roc_curve(y, y_pred)

import numpy as np
np.savetxt("ROC_Data/tpr_SMPP.txt",tpr,delimiter=',');
np.savetxt("ROC_Data/fpr_SMPP.txt",fpr,delimiter=',');
np.savetxt("ROC_Data/thresholds_SMPP.txt",thresholds,delimiter=',');

# calculate AUC
auc = roc_auc_score(y, y_pred)
print('AUC: %.3f' % auc)



#plot_roc_curve(fpr, tpr)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([-0.1, 1.05])
plt.ylim([0.0, 1.10])
plt.xlabel('1-Specificity(False Positive Rate)')
plt.ylabel('Sensitivity(True Positive Rate)')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show() 








from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_data, y, test_size=0.20, random_state=10)

#Distribution of y predicted
print('Distribution of Train Data : \n' + str(pd.Series(y_train).value_counts()))

print('Distribution of Test Data : \n' + str(pd.Series(y_test).value_counts()))






classifier.fit(X_train, y_train) 


pred=classifier.predict(X_test) 
    
  
print(classification_report(y_test, pred))


print("Accuracy Score: "+str(accuracy_score(y_test,pred)))
print("Confusion_matrix :")


cm=confusion_matrix(y_test,pred)
print(cm)


TP = cm[1,1] # true positive 
TN = cm[0,0] # true negatives
FP = cm[0,1] # false positives
FN = cm[1,0] # false negatives
acc=(TP+TN)/(TP+TN+FP+FN)
sn=TP / (TP + FN)
sp =TN / (TN + FP)


print('Sensitivity : ', sn)


print('Specificity : ', sp)

print("Matthews correlation coefficient (MCC): ",matthews_corrcoef(y, y_pred))



# calculate roc curve
fpr, tpr, thresholds = roc_curve(y_test, pred)

import numpy as np
np.savetxt("ROC_Data/tpr_SMPP_independent.txt",tpr,delimiter=',');
np.savetxt("ROC_Data/fpr_SMPP_independent.txt",fpr,delimiter=',');
#np.savetxt("ROC_Data/thresholds_SMPP.txt",thresholds,delimiter=',');



# calculate AUC
auc = roc_auc_score(y_test, pred)
print('AUC: %.3f' % auc)

#plot_roc_curve(fpr, tpr)

plt.plot(fpr,tpr,label="AUC="+str(auc))
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([-0.1, 1.05])
plt.ylim([0.0, 1.10])
plt.xlabel('1-Specificity(False Positive Rate)')
plt.ylabel('Sensitivity(True Positive Rate)')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show() 




























