import pandas as pd
import numpy as np
import re

class company():
    def __init__(self,url):
        self.url = url
        # 클래스 생성과 동시에 읽어낼 파일 경로 입력


    def start(self):
        # 기본적인 컬럼값을 맞춰주는 함수
        self.df = pd.read_csv(self.url,encoding='cp949')
        self.df.drop('항목',axis=1,inplace=True)
        # 거래소 코드 제거

        for i in np.arange(len(self.df.columns)): 
            ### 0에서부터 self.df의 컬럼 개수에 해당하는 정수로 구성된 1차원 행렬 구성
            ### i에 0부터 self.df의 컬럼 개수까지 정수를 넣어서 반복한다.
            name = re.sub(pattern = '\([^)]*\)',repl='',string=self.df.columns[i])
            ### 각각의 컬럼명마다 괄호 안에 있는 모든 문자를 제거하여 name이라는 변수에 저장
            self.df.rename(columns={self.df.columns[i]:name},inplace=True)
            ### 컬럼명을 name에 저장된 값으로 바꾼다.
    


        self.df.drop([1],axis=0,inplace=True)
        # 회사명 및 amount 표기된 행 제거

        self.df.reset_index(drop=True,inplace=True)
        # 행 제거로 인덱스 초기화
        
        self.df.columns =self.df.columns.str.replace('.1','')
        self.df.columns =self.df.columns.str.replace('.2','')
                
        self.df.rename(columns = {'CASH FLOW 대 매출액비율':'매출/현금흐름'},inplace=True)
        self.df.rename(columns = {'CASH FLOW 대 부채비율':'부채/현금흐름'},inplace=True)

        self.df.columns = self.df.columns + self.df.loc[0,:]
        self.df.drop(0,axis=0,inplace=True)
        # 컬럼명 맨 뒤에 연도를 추가하고 연도 행을 삭제한다.
        
        self.df.rename(columns={np.nan:'구분'},inplace=True)
        # nan으로 처리된 컬럼명을 '구분'으로 변경하고 다시한번 인덱스 초기화
        self.df.dropna(inplace=True)
        
        #######################################################################################
        for i in self.df.index:
            txt = self.df['구분'][i]
            if txt[txt.find('호')-1]  in str(np.arange(11)):
                self.df.drop(i,axis=0,inplace=True)
        
        
        # for j in np.arange(1000):
        #     for k in list(self.df[self.df['구분'].str.contains('{}호'.format(j))].index):
        #         self.df.drop(k,axis=0,inplace=True)

        for j in ['피에프브이','투자','금융','파이낸스','인베스트먼트','펀드','기금','임대','부동산','개발']:
            for k in list(self.df[self.df['구분'].str.contains(j)].index):
                self.df.drop(k,axis=0,inplace=True)
                        
        self.df.reset_index(inplace=True, drop=True)
        ######################################################################################
        # -> 금융업 및 투자회사 제거 
        
        return self.df
        
    def show_company(self,start):
        self.start = start
        df1 = self.df.columns.str.contains(f'{start}')
        df2 = self.df.columns.str.contains(f'{start+1}')
        df3 = self.df.columns.str.contains(f'{start+2}')
        
    
    
    
    
    def limit_com(self,start=0):
        # 각각의 기준에 맞는 기업별 한계기업 여부를 데이터 프레임 맨 뒤에 추가해주는 함수
        
        rate1 = []
        rate2 = []
        rate3 = []
        self.start = start

        

        for i in self.df.index:
            if float(self.df['이자보상배율{}'.format(start)][i]) <1 and float(self.df['이자보상배율{}'.format(start+1)][i]) <1:
                rate1.append(1)
            else:
                rate1.append(0)
    

        for i in self.df.index:
            if float(self.df['영업이익{}'.format(start)][i]) <0 and float(self.df['영업이익{}'.format(start+1)][i]) <0:
                rate2.append(1)
            else:
                rate2.append(0)
                

        for i in self.df.index:
            if float(self.df['차입금의존도{}'.format(start+1)][i]) > 70:
                rate3.append(1)
            else:
                rate3.append(0)
        
        self.df['한계기업(이자보상배율){}'.format(start+1)] = rate1
        self.df['한계기업(영업이익){}'.format(start+1)] = rate2
        self.df['한계기업(차입금의존도){}'.format(start+1)] = rate3
        # 한계기업을 1로 두고 정상기업을 0으로 둔다.

        return self.df
        # 기업별 한계기업 여부가 추가
    
    def show_limit(self,standard):
        # 한계기업 분류 중 standard로 지정된 기준에 따라 한계기업으로 분류된 기업들의 데이터만 출력하는 함수
        
        self.standard = standard
        if standard == '이자보상배율':
            cess = self.df.loc[self.df['한계기업(이자보상배율){}'.format(self.start+1)] == 1]
        # 한계기업 여부 데이터 프레임 추출
            self.cess = cess.iloc[:,:len(cess.columns)-3].reset_index(drop=True)
            return self.cess
        
        elif standard == '영업이익':
            cess = self.df.loc[self.df['한계기업(영업이익){}'.format(self.start+1)] == 1]
        # 한계기업 여부 데이터 프레임 추출
            self.cess = cess.iloc[:,:len(cess.columns)-3].reset_index(drop=True)
            return self.cess
        
        elif standard == '차입금의존도':
            cess = self.df.loc[self.df['한계기업(차입금의존도){}'.format(self.start+1)] == 1]
        # 한계기업 여부 데이터 프레임 추출
            self.cess = cess.iloc[:,:len(cess.columns)-3].reset_index(drop=True)
            return self.cess
    
    
    def devide(self):
        # 한계기업들 중 정상기업으로 전환하는지 여부를 데이터프레임에 추가하는 함수
        rate = []


        if self.standard == '이자보상배율':

            for i in self.cess.index:
                if float(self.cess['이자보상배율{}'.format(self.start+1)][i]) <1 and float(self.cess['이자보상배율{}'.format(self.start+2)][i]) <1:
                    rate.append(0)
                else:
                    rate.append(1)
    
        elif self.standard == '영업이익':
            for i in self.cess.index:
                if float(self.cess['영업이익{}'.format(self.start+1)][i]) <0 and float(self.cess['영업이익{}'.format(self.start+2)][i]) <0:
                    rate.append(0)
                else:
                    rate.append(1)
                    

        elif self.standard == '차입금의존도':
            for i in self.cess.index:
                if float(self.cess['차입금의존도{}'.format(self.start+2)][i]) > 70:
                    rate.append(0)
                else:
                    rate.append(1)
        
        self.cess['정상기업여부'] = rate
        
        # 정상기업을 1로 두고 여전히 한계기업 상태이면 0으로 표기한다.
        return self.cess

    def select_df(self):
        # 최종 재무비율 데이터 세트에서 정상기업이 추가되어 출력된다.
        
        df = self.cess
        df = df.set_index('구분')[df.columns[df.columns.str.contains('{}'.format(self.start+2))]].reset_index()
        df = pd.concat([df,self.cess['정상기업여부']],axis=1)
        
        return df