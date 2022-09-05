Portfolio_ML
============

Portfolio_ML
============

---

<h2> #1. Project - 지표를 이용한 삼성전자 주가 예측 및 상관관계 분석 </h2>

- Background

<p>1. 금융 빅데이터 분석가 과정 최초 진행 프로젝트</p>
 <p>2. 삼성전자 주가와 상관관계가 높은 지표를 파악한다.</p>
 <p>3. 분석 결과 최종 선택된 변수에 다양한 모형을 적용하여 최종 예측 모형을 도출한다.</p>

- Summary

  <p>(1). Data Collection </p> 
    	<p>[1] 수집 데이터 종류</p>
    	-주요 주가지수: 삼성전자 주가, 나스닥, 코스피, 항셍, 니케이225, 필라델피아반도체지수<br>
    	-무위험 이자율: 국고채 3년물, 미국채 10년물<br> 
    	- 원자재: 금 선물, 유가 3종(두바이유, 브렌트유, WTI) 현물<br>
    - 환율: 달러, 엔</p>
    	<p>[2] 데이터 출처</p>
    		- yahoofinance : 주요 주가지수, 환율, 금 선물
    		<br>
    		- 한국은행 100대 지표: 국고채 3년물
    		<br>
    		- 한국석유공사: 유가 3종 현물
    		<br>
    		- Finance Data Reader: 미국 국채 10년물
    <p>(2). Data Preprocessing <br/>
    	-데이터 타입 가공: 개별 지표의 날짜 형식 일치 및 단일 데이터 프레임화<br/>
    	- 결측치 처리: 선형 보간법 활용<br/>
    	- EDA<br/>
    	- 스케일링 <br/>
    	- 독립변수 간 상관관계 분석<br/>
    	--------> 변수간 상관관계가 매우 크다. 다중공선성 문제 예상됨<br/>
    	- 독립변수 선정(Lasso, Ridge, RandomForest,PCA 활용) <br/></p>

  <p>(3). Model & Algorithms <br/>
    	- 선형회귀, Lasso, Ridge, Randomforest 활용 <br/>
    	-----> 의미 없음 <br/>
    	-시계열 분석 <br/>
    <p>(4). Report <br/>
    	- 외부 변수를 독립변수로 한 회귀 모형을 기반한 주가 예측은 어렵다.<br/>
    	- 시계열 분석의 경우 단기 예측은 유의미한 결과가 나왔지만 장기 예측에 적합하지 않았다.</br>
    <p>(5). Review <br/>
    		<p>1) 변수 선정 과정: 도메인적 측면에서의 변수 선정 검증이 부족했다. <br/>
    		-----> 공신력 있는 자료를 통한 검증 필수<br/>
    		2) 모델, 알고리즘: 선형 회귀의 기본 가정을 만족하지 못했다.<br/>
    		3) 시계열 분석: 주식 가격은 시계열 데이터이지만 다양한 요인에 의해 영향을 받는 데이터이므로  장기 예측에 시계열 분석이 적절하지 않았던 것으로 생각된다.<br/></p>
    	- Futher Research : 교수님 -> 이 경우 패널 분석을 진행하는 것이 좋을 것이라면서 추후 개별적으로 알아가라 조언<br/>

*보러가기: [지표를 이용한 삼성전자 주가 예측 및 상관관계 분석](https://github.com/siamga/portfolio/tree/main/%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90%EC%A3%BC%EA%B0%80%EC%98%88%EC%B8%A1)*

---

<h2> #2. Project - 푸드트럭 상권분석 </h2>

- Background

<p> BA '비즈니스 분석' 과목의 과제(data 분석을 통한 문제 해결 프로젝트)<br/>

    주제 : 서울시 푸드트럭 수익 최적 위치 추천`<br/>`

    주제 선정 배경 : 고정적 수익 창출이 어려운 현재 상황(지역축제 or 야시장)`<br/>`

    기존 가게들과 푸드트럭의 마찰`<br/>`

    ---> 서울시 공공데이터 분석을 통해 최적의 신규 영업허가지 장소 추천`</p>`

- Summary

  <p>(1). Data Collection</br>
    	- 수집대상 : 유동인구(골목, 지하철) , 상권추정매출, 서울시 특화 산업단지, 재래시장 <br/>
    	- 수집 출처 : 서울시 열린데이터 광장</p>

  <p>(2). Data Preprocessing <br/>
    	- 데이터 통합</p>

  <p>(3). Model & Algorithms <br/>
       - 전통적 상권분석<br/>

  * 매출 추정 과정`<br/>`
  프로세스 : 상권설정 --> 상권정보 추출, 입력 --> 매출, 수익성 분석 --> 우량입지 추출 / 관리

  주요 상권 정보 변수들 : 경쟁자 매출, 잠재 고객 분석-세대수, 세대특성, 거주 형태, 소비지출형태, 유동인구
  대중교통, 횡단보도등 접근성(접근성, 가시성), 기타 주변환경

  모델링 : 1. 기본모델 - 고객수 x 객단가 = 매출(매장 앞 유동 인구 수 중 매장 방문/구매 고객의 비율)
  - 시장규모 x 시장 점유율 = 매출
  2. 회귀 모형 모델 - 과거 데이터가 있는 경우 적용 가능(인구 밀집 or 상권 밀집, 또는 소득 등에 따라서
  지역을 그룹화한 후 각각의 그룹에 맞는 모형을 선택하여 추정)

  - BLD 모형

  * 푸드트럭 특화 모형`<br/>`
  영업장소 특성을 반영하여 아침, 점심, 저녁에 따른 이동 영업`<br/>`
  아침 : 1인 가구 / 점심 : 서울시 특화 산업단지 / 저녁 : 전통 재래시장

  <p>(5). Review <br/>
    	- 매출 데이터가 없어서 정확한 모형을 만들기 어려움

*보러가기: [푸드트럭 위치추천](https:ck)*

---

<h2> #3. Project - 감자과자 시장분석</h2>

- Background

<p>Text Mining(크롤링, 상관분석, 연관규칙...) --> 감자과자 시장분석</p>

- Summary

  <p>(1). Data Collection</br>
    	- 수집대상 : 오리온-포카칩 / 농심-수미칩 / 해테 - 허니버터칩 / 롯데 - 레이즈 감자칩 / PB-이마트 노브랜드 감자칩 <br/> 
    	- 수집 방법 : R을 통한 크롤링<br/>
    	- 수집 출처 : 네이버 블로그, 트위터, 페이스북</p>

  <p>(2). Data Preprocessing <br/>
    	- 형태소 저장 <br/>
    	- 불필요한 단어 제거 </p>

  <p>(3). Model & Algorithms <br/>
    - Wordcloud : 빈도분석의 시각화를 위해<br>
    	- 상관관계 : network graph를 통해 시각화<br>
    	- graphical lasso : 추가 변수의 효과를 제어하고, 두 변수간  의 효과를 알기 위해 사용 <br>
    	- 연관규칙 : support, confidence, lift(by apriori 알고리즘)<br>
    	- 시계열 분석 : 검색 추세 분석

  <p>(4). Report
    	- jupyter notebook with R로 작성

  <p>(5). Review <br/>
    	- Feedback : 크롤링, 연관규칙, 가우시안 그래프 모델 등 다양한 분석방법을 활용할 수 있어서 좋았다 <br/>
    	- Futuer Research : 코드가 깔끔하지 않고, 명확한 결론을 내리지 못했다. 감성사전을 통해 감성분석을 하는게 필요해보인다.

*보러가기: [감자과자시장분석](httpstosnack)*

---

<h2> #4. Project - 2018 러시아 월드컵 결과 예측</h2>

- Background

<p>Kaggle Predicting the winner of the 2018 FIFA World Cup 참고하여 진행</p>

- Summary

  <p>(1). Data Collection</br>
    	- 수집대상 : 피파랭킹 / 공식경기기록 / 월드컵  <br/> 
    - 수집 출처 : kaggle</p>

  <p>(2). Data Preprocessing <br/>
    	- 형태소 저장 <br/>
    	- 불필요한 단어 제거 </p>

  <p>(3). Model & Algorithms <br/>
    - Wordcloud : 빈도분석의 시각화를 위해<br>
    	- 상관관계 : network graph를 통해 시각화<br>
    	- graphical lasso : 추가 변수의 효과를 제어하고, 두 변수간  의 효과를 알기 위해 사용 <br>
    	- 연관규칙 : support, confidence, lift(by apriori 알고리즘)<br>
    	- 시계열 분석 : 검색 추세 분석

  <p>(4). Report
    	- jupyter notebook with R로 작성

  <p>(5). Review <br/>
    	- Feedback : 크롤링, 연관규칙, 가우시안 그래프 모델 등 다양한 분석방법을 활용할 수 있어서 좋았다 <br/>
    	- Futuer Research : 코드가 깔끔하지 않고, 명확한 결론을 내리지 못했다. 감성사전을 통해 감성분석을 하는게 필요해보인다.

*보러가기: [감자과자시장분석](https://github.copotatosnack)*

머신러닝 프로젝트 포트폴리오 정리

---

<h2> #1. Project - 지표를 이용한 삼성전자 주가 예측 및 상관관계 분석 </h2>

- Background

```
<p>각종 경제 지표를 활용하여 삼성전자 주가의 향후 가격을 예측한다.</br>

<p> 선정 지표를 4가지 범주(무위험 이자율, 원자재, 환율, 주요 주가지수)로 나누어 선정하여 해당 지표와의 삼성전자와의 상관관계를 분석한다.</p>
<p> 상관관계 분석 결과 최종 선택 변수에 다양한 모형을 적용하여 최종 예측 모형을 도출한다 </p>
<p> 도출 모형에 2022년 1월~4월까지의 데이터셋을 적용하여 성능을 검증한다. </p>
```

- Summary

  <p>(1). Data Collection <br/>
    	- 은행 데이터 마트(지점데이터 + 고객데이터) + 외부데이터(금융결제원)</p>
    <p>(2). Data Preprocessing <br/>
    	- EDA (지점데이터 + 고객데이터 + 외부데이터) <br/>
    	- Reduction (특성이 다른 지점 데이터  제거, missing value 포함한 고객데이터 제거)</p>
    <p>(3). Model & Algorithms <br/>
    	- xgboost regression(지점 데이터) --> RMSE 작을 때 feature importance <br/>
    	- xgboost classifier(고객 데이터) --> F1 높을 때 feature importance<br/>
    	- Aggregation(고객데이터 --> 지점데이터) --> Clustering(Hierarchical, K-means, Gaussian mixture)</p>
    <p>(4). Report <br/>
    	- 이탈에 영향을 주는 변수 목록 작성
    	- 변수 특성이 비슷한 지점끼리 클러스터링한 결과 표 작성
    <p>(5). Review <br/>
    	- 피드백 : 클러스터링보다 나은 방법이 있지 않았을까<br/>
    	- Futher Research : 바뀌는 금융환경 ---> 모델링 반복 필요<br/>
    	 : 통폐합이 영향을 준 고객만을 대상으로 분석 모델을 구축해야 한다

*보러가기: [은행이탈률 클러스터링](깃 주소)*
      

---

<h2> #2. Project - 푸드트럭 상권분석 </h2>

- Background

<p> BA '비즈니스 분석' 과목의 과제(data 분석을 통한 문제 해결 프로젝트)<br/>

     주제 : 서울시 푸드트럭 수익 최적 위치 추천 `<br/>`

    주제 선정 배경 : 고정적 수익 창출이 어려운 현재 상황(지역축제 or 야시장)`<br/>`

    기존 가게들과 푸드트럭의 마찰`<br/>`

    ---> 서울시 공공데이터 분석을 통해 최적의 신규 영업허가지 장소 추천`</p>`

- Summary

  <p>(1). Data Collection</br>
    	- 수집대상 : 유동인구(골목, 지하철) , 상권추정매출, 서울시 특화 산업단지, 재래시장 <br/>
    	- 수집 출처 : 서울시 열린데이터 광장</p>

  <p>(2). Data Preprocessing <br/>
    	- 데이터 통합</p>

  <p>(3). Model & Algorithms <br/>
       - 전통적 상권분석<br/>

  * 매출 추정 과정 `<br/>`
    프로세스 : 상권설정 --> 상권정보 추출, 입력 --> 매출, 수익성 분석 --> 우량입지 추출 / 관리

  주요 상권 정보 변수들 : 경쟁자 매출, 잠재 고객 분석-세대수, 세대특성, 거주 형태, 소비지출형태, 유동인구
  대중교통, 횡단보도등 접근성(접근성, 가시성), 기타 주변환경

  모델링 : 1. 기본모델 - 고객수 x 객단가 = 매출(매장 앞 유동 인구 수 중 매장 방문/구매 고객의 비율)

  - 시장규모 x 시장 점유율 = 매출

  2. 회귀 모형 모델 - 과거 데이터가 있는 경우 적용 가능(인구 밀집 or 상권 밀집, 또는 소득 등에 따라서
     지역을 그룹화한 후 각각의 그룹에 맞는 모형을 선택하여 추정)

  - BLD 모형

  * 푸드트럭 특화 모형 `<br/>`
    영업장소 특성을 반영하여 아침, 점심, 저녁에 따른 이동 영업 `<br/>`
    아침 : 1인 가구 / 점심 : 서울시 특화 산업단지 / 저녁 : 전통 재래시장

  <p>(5). Review <br/>
    	- 매출 데이터가 없어서 정확한 모형을 만들기 어려움

*보러가기: [푸드트럭 위치추천](https:ck)*

---

<h2> #3. Project - 감자과자 시장분석</h2>

- Background

<p>Text Mining(크롤링, 상관분석, 연관규칙...) --> 감자과자 시장분석</p>

- Summary

  <p>(1). Data Collection</br>
    	- 수집대상 : 오리온-포카칩 / 농심-수미칩 / 해테 - 허니버터칩 / 롯데 - 레이즈 감자칩 / PB-이마트 노브랜드 감자칩 <br/> 
    	- 수집 방법 : R을 통한 크롤링<br/>
    	- 수집 출처 : 네이버 블로그, 트위터, 페이스북</p>

  <p>(2). Data Preprocessing <br/>
    	- 형태소 저장 <br/>
    	- 불필요한 단어 제거 </p>

  <p>(3). Model & Algorithms <br/>
    - Wordcloud : 빈도분석의 시각화를 위해<br>
    	- 상관관계 : network graph를 통해 시각화<br>
    	- graphical lasso : 추가 변수의 효과를 제어하고, 두 변수간  의 효과를 알기 위해 사용 <br>
    	- 연관규칙 : support, confidence, lift(by apriori 알고리즘)<br>
    	- 시계열 분석 : 검색 추세 분석

  <p>(4). Report
    	- jupyter notebook with R로 작성

  <p>(5). Review <br/>
    	- Feedback : 크롤링, 연관규칙, 가우시안 그래프 모델 등 다양한 분석방법을 활용할 수 있어서 좋았다 <br/>
    	- Futuer Research : 코드가 깔끔하지 않고, 명확한 결론을 내리지 못했다. 감성사전을 통해 감성분석을 하는게 필요해보인다.

*보러가기: [감자과자시장분석](httpstosnack)*

---

<h2> #4. Project - 2018 러시아 월드컵 결과 예측</h2>

- Background

<p>Kaggle Predicting the winner of the 2018 FIFA World Cup 참고하여 진행</p>

- Summary

  <p>(1). Data Collection</br>
    	- 수집대상 : 피파랭킹 / 공식경기기록 / 월드컵  <br/> 
    - 수집 출처 : kaggle</p>

  <p>(2). Data Preprocessing <br/>
    	- 형태소 저장 <br/>
    	- 불필요한 단어 제거 </p>

  <p>(3). Model & Algorithms <br/>
    - Wordcloud : 빈도분석의 시각화를 위해<br>
    	- 상관관계 : network graph를 통해 시각화<br>
    	- graphical lasso : 추가 변수의 효과를 제어하고, 두 변수간  의 효과를 알기 위해 사용 <br>
    	- 연관규칙 : support, confidence, lift(by apriori 알고리즘)<br>
    	- 시계열 분석 : 검색 추세 분석

  <p>(4). Report
    	- jupyter notebook with R로 작성

  <p>(5). Review <br/>
    	- Feedback : 크롤링, 연관규칙, 가우시안 그래프 모델 등 다양한 분석방법을 활용할 수 있어서 좋았다 <br/>
    	- Futuer Research : 코드가 깔끔하지 않고, 명확한 결론을 내리지 못했다. 감성사전을 통해 감성분석을 하는게 필요해보인다.

*보러가기: [감자과자시장분석](https://github.copotatosnack)*
