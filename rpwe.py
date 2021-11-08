#===================================================
#   Error storing and comparing Part of each models
#===================================================

eeg_val_MSE = 0.5 * np.square(np.subtract(y_act_val[0],tmp_eeg_val))
eeg_aro_MSE = 0.5 * np.square(np.subtract(y_act_aro[0],tmp_eeg_aro))

eda_val_MSE = 0.5 * np.square(np.subtract(y_act_val[0],tmp_eda_val))
eda_aro_MSE = 0.5 * np.square(np.subtract(y_act_aro[0],tmp_eda_aro))

resp_val_MSE = 0.5 * np.square(np.subtract(y_act_val[0],tmp_resp_val))
resp_aro_MSE = 0.5 * np.square(np.subtract(y_act_aro[0],tmp_resp_aro))

val_MSE = [eeg_val_MSE, eda_val_MSE, resp_val_MSE] #Valence errors 
aro_MSE = [eeg_aro_MSE, eda_aro_MSE, resp_aro_MSE] #Arousal errors



#=================================================================
# Valence Arousal MSE Compariosn and storing in Cbest and Cworst
#=================================================================

if (jj==0): #First Video
    cBest_val = val_MSE
    cBest_aro = aro_MSE

    cWorst_val  = val_MSE
    cWorst_aro = aro_MSE

else:
    #--------------------------------------------------------------
    # Classifiers best MSE error and worst MSE error value update
    #-------------------------------------------------------------
    cBest_val = np.minimum(cBest_val, val_MSE)
    cBest_aro = np.minimum(cBest_aro, aro_MSE)
    cWorst_val = np.maximum(cWorst_val, val_MSE)
    cWorst_aro = np.maximum(cWorst_aro, aro_MSE)

    #-----------------------------------------
    #Beta for calence and arousal calculation
    #-----------------------------------------              
    beta_val = np.true_divide(list(np.subtract(cBest_val,val_MSE)), (1+np.exp(list(np.subtract(cWorst_val,cBest_val)))))
    beta_aro = np.true_divide(list(np.subtract(cBest_aro,aro_MSE)), (1+np.exp(list(np.subtract(cWorst_aro,cBest_aro)))))

#============================================
# Controls for the first time
#============================================
if ccc ==0:
    val_label = [0, 0, 0]
    aro_label = [0, 0, 0] 
    ccc =ccc+1
else:
    val_label = [y_pred_val_eeg[0], y_pred_val_eda[0], y_pred_val_resp[0]]
    aro_label = [y_pred_aro_eeg[0], y_pred_aro_eda[0], y_pred_aro_resp[0]] 


##=============================
# Confusion Matric Calculation
##=============================

eeg_cm_val = eeg_cm_val.update(y_act_val[0], y_pred_val_eeg[0])
eeg_cm_aro = eeg_cm_aro.update(y_act_aro[0], y_pred_aro_eeg[0])

eda_cm_val = eda_cm_val.update(y_act_val[0], y_pred_val_eda[0])
eda_cm_aro = eda_cm_aro.update(y_act_aro[0], y_pred_aro_eda[0])

resp_cm_val = resp_cm_val.update(y_act_val[0], y_pred_val_resp[0])
resp_cm_varo = resp_cm_aro.update(y_act_aro[0], y_pred_aro_resp[0])            


#====================================================================
# Decision label ensemble --> Reward Penalty Based Weightrd Ensemble
#====================================================================

#------------------------------------------
# Valence Class ensemble
#------------------------------------------

p_val = np.dot(val_label, w_val)
mer_val = 1 if p_val > 0.5 else 0

#------------------------------------------
# Arousal Class ensemble
#------------------------------------------            
p_aro = np.dot(aro_label,w_aro)
mer_aro = 1 if p_aro > 0.5 else 0

# print([val_label, aro_label])
# print([p_val,p_aro])
#============================================
# Weight update for Valence
#============================================
w_val = w_val + list(np.multiply(w_val,beta_val))    
w_val_sum = sum(w_val) #total sum of weights
w_val = np.array(w_val/w_val_sum) #weight rescaling

#============================================
# Weight update for Arousal
#============================================

w_aro = w_aro + list(np.multiply(w_aro,beta_aro))
w_aro_sum = sum(w_aro) #total sum of weights
w_aro = np.array(w_aro/w_aro_sum) #weight rescaling
