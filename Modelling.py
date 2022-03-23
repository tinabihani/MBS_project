#importing all the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# importing the cleaned dataset
data = pd.read_csv("data_new.csv", low_memory=False)

data=data.drop(['FirstPaymentDate', 'FirstTimeHomebuyer', 'MaturityDate','MSA',
             'Occupancy',  'Channel', 'ProductType', 'PropertyState',
            'PropertyType', 'PostalCode', 'LoanSeqNum', 'LoanPurpose',
            'OrigLoanTerm', 'NumBorrowers', 'SellerName', 'ServicerName', 'MonthsDelinquent','Years in Repayment',
            'Repay_range_in_years','CreditRange','LTV_range','IsFirstTime'], axis=1)

data['PPM'] = np.where(data['PPM'] == 'Y', 1, 0)
from sklearn.model_selection import train_test_split
X=data.drop(['EverDelinquent'],axis=1)
y=data['EverDelinquent']


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test=train_test_split( X, y , train_size=0.8 , random_state=0)
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
from sklearn.ensemble import RandomForestClassifier
model_rf=RandomForestClassifier(n_estimators=10, criterion='entropy', max_depth = 3)
model_rf.fit(X_train,y_train)
from sklearn.metrics import  accuracy_score
y_predict_rf1=model_rf.predict(X_test)
print(accuracy_score(y_test,y_predict_rf1))

def prediction(CreditScore,MIP,Units,OCLTV,DTI,OrigUPB,LTV,OrigInterestRate,PPM,MonthsInRepayment):

    x_input=[[CreditScore,MIP,Units,OCLTV,DTI,OrigUPB,LTV,OrigInterestRate,PPM,MonthsInRepayment]]
    y_predict_rf=model_rf.predict(x_input)
    if y_predict_rf == 0:
        return ("The borrower will pay the loan on time")
    else:
        return ("Alert!Alert! This looks like a risky loan")


    #return y_predict_rf
    