import pandas as pd
import numpy as np
import re
import warnings
import math
warnings.filterwarnings(action='ignore')

# 뿌리 모듈


from importlib import reload
# csv 경로, set_year = 최종 데이터 프레임의 기준 연도, self.start = 한계기업 기준 연도, self.standard = 한계기업 기준

class make_fin():
# a = make_fin.make_fin()
    def __init__(self):
        self
        
    def raw_df(self,url):
# a.raw_df(url = 'csv파일을 읽어올 경로')
        
        self.df = pd.read_csv(url,encoding='cp949')
        # 여기서 사용할 데이터는 실제 재무비율을 계산하기 위한
        # 원 재무 데이터이다.  

        for i in np.arange(len(self.df.columns)): 
            name = re.sub(pattern = '\([^)]*\)',repl='',string=self.df.columns[i])
            ### 각각의 컬럼명마다 괄호 안에 있는 모든 문자를 제거하여 name이라는 변수에 저장
            self.df.rename(columns={self.df.columns[i]:name},inplace=True)
            ### 컬럼명을 name에 저장된 값으로 바꾼다.

        self.df.columns =self.df.columns.str.replace('.1','')
        self.df.columns =self.df.columns.str.replace('.2','')
        self.df.columns =self.df.columns.str.replace('.3','')
        self.df.columns =self.df.columns.str.replace('.4','')
        self.df.columns =self.df.columns.str.replace('.5','')
        self.df.columns =self.df.columns.str.replace('.6','')
        # 이때, '자산.1','자산.2','자산.3','부채.1'... 식으로 컬럼명이 지정되어 있어
        # '.1'에 해당하는 부분을 지운다.

        self.df.columns = self.df.columns + self.df.loc[0,:]
        # '.1'에 해당하는 값을 지운 다음 재무데이터 바로 밑에 있는 연도 값을 합쳐서
        # '자산2011','자산2012'...식으로 columns값을 바꾼다.
         
        self.df.drop([0,1],axis=0,inplace=True)
        # 사용할 이유가 없어진 연도 행과 amount 값으로 채워진 행을 제거한다.
        
        self.df.drop('항목년도',axis=1,inplace=True)
        # 기업 코드가 적힌 컬럼을 없앤다.
        
        self.df.rename(columns={np.nan:'구분'},inplace=True)
        # 연도를 합치는 과정에서 기업명에 해당하는 '구분'이라는 컬럼명이 np.nan으로 바뀌었기에 
        # 해당 값을 다시 '구분'으로 바꾼다.
                
        self.df.set_index('구분',inplace=True)
        # '구분'을 인덱스 값으로 지정한다.
        
        self.df = self.df.astype('float64')   
        # 이제 데이터 프레임에 숫자만 남았기 때문에 데이터 형식을 실수로 바꾼다.
        
        self.df.dropna(inplace=True)
        
        return self.df 
        # 재무데이터를 계산할 재무 데이터 프레임 완성 
    
    
    def make_ratio_df(self,start):
        # a.make_ration_df(start = 기준연도)
        # 2014년도의 한계기업을 예측하고 2015년도의 정상기업 여부를 알고 싶다면
        # start에 2013을 넣는다.
        
        
        self.start =start
        col = pd.read_csv('./fin_col_names.csv',encoding='cp949')
        # 미리 만들어 놓은 재무데이터 작성용 컬럼값 csv파일을 열어놓는다.



        col.columns =col.columns.str.replace('.1','')
        col.columns =col.columns.str.replace('.2','')
        col.columns =col.columns.str.replace('.3','')
        col.columns =col.columns.str.replace('.4','')
        col.columns =col.columns.str.replace('.5','')
        col.columns =col.columns.str.replace('.6','')
        # 컬럼 값이 똑같기 때문에 '이자보상배율','이자보상배율.1','이자보상배율.2'로 출력된다. 
        # 따라서 '.1','.2' 등의 값을 제거한다.
        
        col.drop(['구분','항목'],axis=1,inplace=True)
        # 재무비율 데이터의 컬럼명이 될 컬럼명만 남긴다.
        
        year = pd.DataFrame([self.start,self.start+1,self.start+2]*len(col.columns[2:].unique())).T
        # start에서 지정된 연도 기준 start, start+1, start+2가 col의 실제 컬럼명의 개수만큼 반복한 데이터프레임 year을 만든다.
        
        year.columns=col.columns
        # col로 만들어놓은 재무비율 컬럼명을 year에 적용한다.
        
        year.columns = year.columns + year.loc[0,:].astype('str')
        # 재무비율 컬럼명에 연도 값을 추가해 '이자보상배율' -> '이자보상배율2016' 이런 식으로 바꾼다.
        
        self.dset = pd.DataFrame(columns=year.columns, index = self.df.index)
        # 이제 실제 재무비율 데이터를 넣을 데이터 프레임을 만들어 
        # 컬럼명을 year의 컬럼명과 동일하게, index값을 기업 이름에 해당하는 df의 index 값으로 설정한다. 
        
        self.df.reset_index(inplace=True)
        self.dset.reset_index(inplace=True)

        for i in self.dset.columns:
            if '이자보상배율' in i:
                self.dset[i] = self.df[f'영업이익{i[-4:]}']/self.df[f'이자비용{i[-4:]}']
                for j in self.dset.index:
                    if self.df[f'이자비용{i[-4:]}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)

            elif '영업손실' in i:
                self.dset[i] = self.df[f'영업이익{i[-4:]}']
            
            elif '차입금의존도' in i:
                self.dset[i] = (self.df[f'장기차입금{i[-4:]}']+self.df[f'단기차입금{i[-4:]}']+self.df[f'사채{i[-4:]}'])/self.df[f'자산{i[-4:]}']
                for j in self.dset.index:
                    if self.df[f'자산{i[-4:]}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                

            elif '총자산증가율' in i:
                self.dset[i] = (self.df[f'자산{int(i[-4:])}']-self.df[f'자산{int(i[-4:])-1}'])/self.df[f'자산{int(i[-4:])-1}']
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])-1}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '유동자산증가율' in i:
                self.dset[i] = (self.df[f'유동자산{int(i[-4:])}'] - self.df[f'유동자산{int(i[-4:])-1}'])/self.df[f'유동자산{int(i[-4:])-1}']
                for j in self.dset.index:
                    if self.df[f'유동자산{int(i[-4:])-1}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
            elif '매출액증가율' in i:
                self.dset[i] = (self.df[f'매출액{int(i[-4:])}'] - self.df[f'매출액{int(i[-4:])-1}'])/self.df[f'매출액{int(i[-4:])-1}']
                for j in self.dset.index:
                    if self.df[f'매출액{int(i[-4:])-1}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '매출액순이익률' in i:
                self.dset[i] = self.df[f'당기순이익{int(i[-4:])}']/self.df[f'매출액{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'매출액{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '자기자본순이익률' in i:
                self.dset[i] = self.df[f'당기순이익{int(i[-4:])}']/self.df[f'자본{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'자본{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '총자산순이익률' in i:
                self.dset[i] = self.df[f'당기순이익{int(i[-4:])}']/self.df[f'자산{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
            elif '매출원가대매출액비율' in i:
                self.dset[i] = self.df[f'매출원가{int(i[-4:])}']/self.df[f'매출액{int(i[-4:])}']  
                for j in self.dset.index:
                    if self.df[f'매출액{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)

            elif '매출액대판매관리비' in i:
                self.dset[i] = self.df[f'판매비와관리비{int(i[-4:])}']/self.df[f'매출액{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'매출액{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
                
            elif '매출채권회전율' in i:
                self.dset[i] = self.df[f'매출액{int(i[-4:])}']/self.df[f'매출채권{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'매출채권{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
            elif '재고자산회전율' in i:
                self.dset[i] = self.df[f'매출원가{int(i[-4:])}']/self.df[f'재고자산{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'재고자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
            elif '총자본회전율' in i:
                self.dset[i] = self.df[f'매출액{int(i[-4:])}']/self.df[f'자산{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
            elif '유형자산회전율' in i:
                self.dset[i] = self.df[f'매출액{int(i[-4:])}']/self.df[f'유형자산{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'유형자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)

            elif '부채비율' in i:
                self.dset[i] = self.df[f'부채{int(i[-4:])}']/self.df[f'자본{int(i[-4:])}'] 
                for j in self.dset.index:
                    if self.df[f'자본{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '유동비율' in i:
                self.dset[i] = self.df[f'유동자산{int(i[-4:])}']/self.df[f'유동부채{int(i[-4:])}']    
                for j in self.dset.index:
                    if self.df[f'유동부채{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                
            elif '자기자본배율' in i:
                self.dset[i] = self.df[f'자본{int(i[-4:])}']/self.df[f'자산{int(i[-4:])}'] 
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '당좌비율' in i:
                self.dset[i] = self.df[f'당좌자산{int(i[-4:])}']/self.df[f'유동부채{int(i[-4:])}']   
                for j in self.dset.index:
                    if self.df[f'유동부채{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '고정비율' in i:
                self.dset[i] = self.df[f'비유동자산{int(i[-4:])}']/self.df[f'자산{int(i[-4:])}'] 
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            

            elif '순운전자본비율' in i:
                self.dset[i] = (self.df[f'유동자산{int(i[-4:])}'] - self.df[f'유동부채{int(i[-4:])}'])/self.df[f'자산{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            
            elif '현금비율' in i:
                self.dset[i] = self.df[f'현금 및 현금성자산{int(i[-4:])}'] /self.df[f'유동부채{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'유동부채{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
            


            elif '부채/자산' in i:
                self.dset[i] = self.df[f'부채{int(i[-4:])}'] /self.df[f'자산{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'자산{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)
                    
            elif '유동부채/부채' in i:
                self.dset[i] = self.df[f'유동부채{int(i[-4:])}'] /self.df[f'부채{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'부채{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)

            elif '부채/현금흐름' in i:
                self.dset[i] = self.df[f'부채{int(i[-4:])}'] /self.df[f'현금의 증가{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'현금의 증가{int(i[-4:])}'][j] < 0 and self.df[f'부채{int(i[-4:])}'][j] < 0:
                        self.dset[i][j] = (-1)*self.dset[i][j]

            elif '부채/매출액' in i:
                self.dset[i] = self.df[f'부채{int(i[-4:])}'] /self.df[f'매출액{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'매출액{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)

            elif '현금흐름/매출액' in i:
                self.dset[i] = self.df[f'현금의 증가{int(i[-4:])}']/self.df[f'매출액{int(i[-4:])}']
                for j in self.dset.index:
                    if self.df[f'매출액{int(i[-4:])}'][j] < 0:
                        self.dset.drop(j,axis=0,inplace=True)

                    
            elif '차입금평균금리' in i:
                self.dset[i] = self.df[f'차입금평균이자율{int(i[-4:])}']



        # for문을 활용하여 특정 연도의 재무비율을 재무데이터 df를 사용하여 계산한다.

        self.dset.dropna(inplace=True)
        # 재무 비율이 추가된 dset에서 nan값을 제외한다.

        
        for i in self.dset.index:
            txt = self.dset['구분'][i]
            if txt[txt.find('호')-1]  in str(np.arange(11)):
                self.dset.drop(i,axis=0,inplace=True)


        # # for j in np.arange(1000):
        # #     for k in list(self.dset[self.dset['구분'].str.contains('{}호'.format(j))].index):
        # #         self.dset.drop(k,axis=0,inplace=True)

        for j in ['피에프브이','투자','금융','파이낸스','인베스트먼트','펀드','기금','임대','부동산']:
            for k in list(self.dset[self.dset['구분'].str.contains(j)].index):
                self.dset.drop(k,axis=0,inplace=True)
        
        # ~'호', 특수목적 회사를 분석 대상에서 제외한다.
        
        self.dset.set_index('구분',inplace=True)
        # 다시 회사명에 해당하는 '구분' 컬럼을 인덱스로 지정한다.
        
        self.dset[self.dset.columns[self.dset.columns.str.contains('이자보상배율')]] = self.dset[self.dset.columns[self.dset.columns.str.contains('이자보상배율')]].replace(math.inf,np.nan)
        self.dset[self.dset.columns[self.dset.columns.str.contains('이자보상배율')]] = self.dset[self.dset.columns[self.dset.columns.str.contains('이자보상배율')]].replace(-math.inf,np.nan)

        for i in self.dset.columns:
            self.dset[i] = self.dset[i].replace(math.inf,np.nan)
            self.dset[i] = self.dset[i].replace(-math.inf,np.nan)
            
        self.dset.dropna(inplace=True)


            
        return self.dset
        # 실제 재무데이터를 기반으로 한 재무비율이 계산되었다.
        
    def show_limit(self):
        # a.show()
        
        rate1 = []
        rate2 = []
        rate3 = []
        # 해당기간 기준에 따른 한계기업 여부를 추가할 리스트를 만든다.
        # rate1: 이자보상배율, rate2: 영업손실, rate3: 차입금의존도

        self.dset.reset_index(inplace=True)

        for i in self.dset.index:
            if float(self.dset['이자보상배율{}'.format(self.start)][i]) <1 and float(self.dset['이자보상배율{}'.format(self.start+1)][i]) <1:
                rate1.append(1)
            else:
                rate1.append(0)


        for i in self.dset.index:
            if float(self.dset['영업손실{}'.format(self.start)][i]) <0 and float(self.dset['영업손실{}'.format(self.start+1)][i]) <0:
                rate2.append(1)
            else:
                rate2.append(0)
                

        for i in self.dset.index:
            if float(self.dset['차입금의존도{}'.format(self.start+1)][i]) > 0.7:
                rate3.append(1)
            else:
                rate3.append(0)

        self.dset['한계기업(이자보상배율){}'.format(self.start+1)] = rate1
        self.dset['한계기업(영업손실){}'.format(self.start+1)] = rate2
        self.dset['한계기업(차입금의존도){}'.format(self.start+1)] = rate3
        # 한계기업을 1로 두고 정상기업을 0으로 둔다. 

        return self.dset
        # 기업별 한계기업 재무비율 데이터만 출력
    
    
    def select_limit(self,standard):
        # a.select_limit(standard = '한계기업 기준')
        # 한계기업 기준 = '이자보상배율','영업손실','차입금의존도'
        # 한계기업 분류 중 self.standard로 지정된 기준에 따라 한계기업으로 분류된 기업들의 데이터만 출력하는 함수

        self.standard = standard

        rate1= '한계기업(이자보상배율){}'.format(self.start+1) 
        rate2 = '한계기업(영업손실){}'.format(self.start+1) 
        rate3 = '한계기업(차입금의존도){}'.format(self.start+1)

        if self.standard == '이자보상배율':
            self.cess = self.dset.loc[self.dset['한계기업(이자보상배율){}'.format(self.start+1)] == 1]
            self.cess = self.cess.iloc[:,:len(self.cess.columns)-3]

        elif self.standard == '영업손실':
            self.cess = self.dset.loc[self.dset['한계기업(영업손실){}'.format(self.start+1)] == 1]
            self.cess = self.cess.iloc[:,:len(self.cess.columns)-3]


        elif self.standard == '차입금의존도':
            self.cess = self.dset.loc[self.dset['한계기업(차입금의존도){}'.format(self.start+1)] == 1]
            self.cess = self.cess.iloc[:,:len(self.cess.columns)-3]

        self.cess.reset_index(inplace=True,drop=True)
        return self.cess



    def what_is_normal(self):
        # a.what_is_normal()
        
        rate = []
        # 정상기업 여부를 추가할 빈 리스트 추가

        if self.standard == '이자보상배율':

            for i in self.cess.index:
                if float(self.cess['이자보상배율{}'.format(self.start+1)][i]) <1 and float(self.cess['이자보상배율{}'.format(self.start+2)][i]) <1:
                    rate.append(0)
                else:
                    rate.append(1)

        elif self.standard == '영업손실':
            for i in self.cess.index:
                if float(self.cess['영업손실{}'.format(self.start+1)][i]) <0 and float(self.cess['영업손실{}'.format(self.start+2)][i]) <0:
                    rate.append(0)
                else:
                    rate.append(1)
                    

        elif self.standard == '차입금의존도':
            for i in self.cess.index:
                if float(self.cess['차입금의존도{}'.format(self.start+2)][i]) > 0.7:
                    rate.append(0)
                else:
                    rate.append(1)

        self.cess['정상기업여부'] = rate

        # 정상기업을 1로 두고 여전히 한계기업 상태이면 0으로 표기한다.

        for i in self.cess.columns:
            if '영업손실' in i:
                self.cess.drop(i,axis=1,inplace=True)
        # '영업손실' 컬럼 데이터는 비율이 아닌 값의 데이터이기에 분석에 부적절하여 제거한다.


        for i in self.cess.columns:
            if str(self.start) in i or str(self.start+1) in i:
                self.cess.drop(i,axis=1,inplace=True)
        # 분석에 사용할 최종 데이터(ex: 2013~2014->한계기업 분류=> 2015년도: 한계기업 중 정상기업 회복 여부 데이터)
        # 출력을 위해 최종 데이터 직전 2개년 데이터를 삭제한다.

        return self.cess





