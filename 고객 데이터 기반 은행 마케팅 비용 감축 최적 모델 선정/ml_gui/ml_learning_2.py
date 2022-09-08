from PyQt5.QtWidgets import *
import sys,pickle
from PyQt5 import uic, QtWidgets ,QtCore, QtGui
from data_visualise import data_ 
from table_display import DataFrameModel
from xgboost import XGBClassifier
import pandas as pd


class UI(QMainWindow):
    def __init__(self,X,raw):
        super(UI,self).__init__()
        uic.loadUi('predict.ui',self)
        self.table = self.findChild(QTableView, 'table')
        self.to_csv = self.findChild(QPushButton, 'to_csv')
        
        self.to_csv.clicked.connect(self.make_csv)
        
        model = XGBClassifier()
        model.load_model('Model.h5')
        self.pred = model.predict(X).transpose()
        self.pred = pd.DataFrame(data=self.pred,columns=['predict'])
        self.pred_result = pd.concat([raw,self.pred],axis=1).drop('Unnamed: 0',axis=1)
        self.pred_result = self.pred_result[self.pred_result['predict'] == 1].reset_index(drop=True).drop('y',axis=1)
        x = DataFrameModel(self.pred_result)
        self.table.setModel(x)
        print(self.pred_result)
        self.show()
    
    def make_csv(self):
        self.pred_result.to_csv('./result/predict_result.csv')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    window.show()
    sys.exit(app.exec_())