# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 01:12:07 2020

@author: Shaikot
"""


#from sklearn.metrics import roc_curve

import matplotlib.pyplot as plt
import numpy as np

#print(proba)

tpr_SMPP= np.loadtxt("tpr_SMPP_independent.txt",delimiter=",")
fpr_SMPP= np.loadtxt("fpr_SMPP_independent.txt",delimiter=",")
plt.plot(fpr_SMPP,tpr_SMPP,label="SMPP, AUC="+str(95.89))




tpr_Bigram_PGK= np.loadtxt("tpr_Bigram_PGK_independent.txt",delimiter=",")
fpr_Bigram_PGK= np.loadtxt("fpr_Bigram_PGK_independent.txt",delimiter=",")
plt.plot(fpr_Bigram_PGK,tpr_Bigram_PGK,label="Bigram, AUC="+str(91.14))




tpr_Phogly_PseAAC= np.loadtxt("tpr_Phogly_PseAAC_independent.txt",delimiter=",")
fpr_Phogly_PseAAC= np.loadtxt("fpr_Phogly_PseAAC_independent.txt",delimiter=",")
#thresholds_CKSAAP_FormSite=np.loadtxt("thresholds_CKSAAP_FormSite.txt",delimiter=",")
plt.plot(fpr_Phogly_PseAAC,tpr_Phogly_PseAAC,label="PSAAP, AUC="+str(88.32))



tpr_RAM_PGK= np.loadtxt("tpr_RAM-PGK_independent.txt",delimiter=",")
fpr_RAM_PGK= np.loadtxt("fpr_RAM-PGK_independent.txt",delimiter=",")
plt.plot(fpr_RAM_PGK,tpr_RAM_PGK,label="RAM, AUC="+str(81.73))

tpr_iDPGK= np.loadtxt("tpr_iDPGK_independent.txt",delimiter=",")
fpr_iDPGK= np.loadtxt("fpr_iDPGK_independent.txt",delimiter=",")
plt.plot(fpr_iDPGK,tpr_iDPGK,label="PSSM+PWM+AAC+AAPC, AUC="+str(94.22))


tpr_PhoglyPred= np.loadtxt("tpr_PhoglyPred_independent.txt",delimiter=",")
fpr_PhoglyPred= np.loadtxt("fpr_PhoglyPred_independent.txt",delimiter=",")
plt.plot(fpr_PhoglyPred,tpr_PhoglyPred,label="IKMD+PSPKSD+MCKSAAP, AUC="+str(94.34))


plt.plot([0, 1], [0, 1],'r--')
plt.xlim([-0.1, 1.05])
plt.ylim([0.0, 1.10])
plt.xlabel('1-Specificity(False Positive Rate)')
plt.ylabel('Sensitivity(True Positive Rate)')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")






"""
probs = proba[:, 1]

fpr, tpr, thresholds = roc_curve(y_class, probs)

#plot_roc_curve(fpr, tpr)

plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([-0.1, 1.05])
plt.ylim([0.0, 1.10])
plt.xlabel('1-Specificity(False Positive Rate)')
plt.ylabel('Sensitivity(True Positive Rate)')
plt.title('Receiver Operating Characteristic')
plt.legend()

"""