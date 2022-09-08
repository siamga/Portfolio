from lightgbm import train
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelEncoder
import sys,pickle
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings(action='ignore')
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow_addons as tfa
import tensorflow as tf
from keras.models import load_model
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import tensorflow_addons as tfa
from sklearn.model_selection import train_test_split
from table_display import DataFrameModel

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtWidgets ,QtCore, QtGui
import ml_learning_2




class UI(QMainWindow):
    def __init__(self, df):
        super(UI,self).__init__()
        uic.loadUi('test.ui',self)
        
        self.table = self.findChild(QTableView, 'table')
        self.ml_predict = self.findChild(QPushButton,'ml_predict')
       
        
        self.ml_predict.clicked.connect(self.predict)
        
        self.show()
        
        self.raw_df = df
        ############################
        job = df['job']

        encoder=LabelEncoder()
        job = encoder.fit_transform(job)


        job_labels=job.reshape(-1,1)

        oh_encoder=OneHotEncoder()
        oh_encoder.fit(job_labels)
        job_encode = oh_encoder.transform(job_labels).toarray()

        df_job_encode = pd.DataFrame(data=job_encode,columns=encoder.inverse_transform(np.arange(12)))

        ############################ 
        df_mar=df['marital']
        df_mar
        encoder=LabelEncoder()
        encoder.fit(df_mar)
        marital = encoder.transform(df_mar)


        marital=marital.reshape(-1,1)

        oh_encoder=OneHotEncoder()
        oh_encoder.fit(marital)
        marital_encode = oh_encoder.transform(marital).toarray()


        df_marital_encode = pd.DataFrame(data=marital_encode,columns=encoder.inverse_transform(np.arange(4)))

        df_marital_encode.columns=['divorced','married','single','marital_unknown']
        ################################
        df_edu = df['education']


        edu_category= ['illiterate','basic.4y','basic.6y','basic.9y','high.school','university.degree','professional.course','unknown']   

        for i in edu_category:
            df_edu = df_edu.apply(lambda x: x.replace(i,str(edu_category.index(i))))

        edu=df_edu.astype('int64')

        edu_label = np.array(edu).reshape(-1,1)

        oh_encoder=OneHotEncoder()
        oh_encoder.fit(edu_label)
        edu_encode = oh_encoder.transform(edu_label).toarray()

        edu_encode


        df_edu_encode = pd.DataFrame(data=edu_encode,columns=edu_category)


        df_edu_encode = df_edu_encode.rename(columns={'unknown':'edu_unknown'})
        ##################################################
        default = df['default']

        def_category=['no','yes','unknown']


        for i in def_category:
            default = default.apply(lambda x: x.replace(i,str(def_category.index(i))))

        default = default.apply(lambda x: x.replace('unk0wn','2'))
                    
        default= default.astype('int64')


        default = np.array(default).reshape(-1,1)
        

        oh_encoder=OneHotEncoder()
        oh_encoder.fit(default)
        default_encode = oh_encoder.transform(default).toarray()

        default_encode
        
        df_default_encode = pd.DataFrame(columns=['no','yes','unknown'])
        

        df_default_encode = pd.DataFrame(data=default_encode,columns=['no','yes','unknown'])


        df_default_encode.columns = ['default_no', 'default_yes','default_unknown']
        df_default_encode
        ############################################################################
        house = df['housing']


        house = house.apply(lambda x: x.replace('no','0'))
        house = house.apply(lambda x: x.replace('yes','1'))
        house = house.apply(lambda x: x.replace('unknown','2'))
        house = house.apply(lambda x: x.replace('unk0wn','2'))

        house.astype('int64')

        encoder = OneHotEncoder(sparse=True)
        house_encode = encoder.fit_transform(np.array(house).reshape(-1,1)).toarray()


        df_house_encode = pd.DataFrame(data=house_encode,columns=['no','yes','unknown'])

        df_house_encode.columns = ['house_no', 'house_yes','house_unknown']

        ###########################################################################
        loan = df['loan']


        loan = loan.apply(lambda x: x.replace('no','0'))
        loan = loan.apply(lambda x: x.replace('yes','1'))
        loan = loan.apply(lambda x: x.replace('unknown','2'))
        loan = loan.apply(lambda x: x.replace('unk0wn','2'))

        loan.astype('int64')

        encoder = OneHotEncoder()
        loan_encode = encoder.fit_transform(np.array(loan).reshape(-1,1))
        loan_encode = loan_encode.toarray()

        df_loan_encode = pd.DataFrame(data=loan_encode,columns=['no','yes','unknown'])

        df_loan_encode.columns = ['loan_no', 'loan_yes','loan_unknown']
       
        ##########################################################################
        pdays = df['pdays'].astype('str')
        pdays = pdays.apply(lambda x: x.replace('999','-1'))

        pdays = pdays.astype('int64')

        pdays = pd.DataFrame(data=pdays)
        ###########################################################################33
        pout=df['poutcome']
        pout


        pout= pout.apply(lambda x: x.replace('failure','0'))
        pout = pout.apply(lambda x: x.replace('success','1'))
        pout = pout.apply(lambda x: x.replace('nonexistent','2'))



        labels_p=np.array(pout).reshape(-1,1)
        oh_encorder=OneHotEncoder()
        oh_encorder.fit(labels_p)
        oh_labels_p=oh_encorder.transform(labels_p)
        oh_labels_p = oh_labels_p.toarray()


        df_oh_labels_p = pd.DataFrame(data=oh_labels_p,columns=['pout_no','pout_yes','pout_unknown'])


        df_oh_labels_p
        ################################################################################
        # y = df['y']

        # encorder=LabelEncoder()
        # encorder.fit(y)
        # labels_y=encorder.transform(y)

        # y_encode = pd.DataFrame(data=labels_y,columns=['y'])
        #################################################################################
        df_onehot = pd.DataFrame(df['age'])
        df_onehot = pd.concat([df_onehot,df_job_encode,df_marital_encode,df_edu_encode,df_default_encode,df_house_encode, df_loan_encode,pdays,df['previous'],df_oh_labels_p],axis=1)
        self.df = df_onehot
        print(df_onehot)
        
        x = DataFrameModel(df_onehot)
        self.table.setModel(x)
        
    def predict(self):
        self.send = ml_learning_2.UI(self.df,self.raw_df)

        # #########################################
        
        ##########################################
        # X_train,X_test,y_train,y_test = train_test_split(df_onehot.loc[:,:'pout_unknown'],df_onehot['y'],test_size=0.3,random_state=0)
        
        # X = df_onehot.loc[:,:'pout_unknown']
        # y= df_onehot['y']
        
        # load_model = keras.models.load_model('dnn_model.h5')
        # pred = load_model.predict(X)
        # print(pred)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())