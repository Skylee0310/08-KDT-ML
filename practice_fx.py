'''

<붓꽃 분류 예측 모델 만들기>

(1) 데이터 : iris.csv
(2) 타 겟 : variety
(3) 피 처 : petal, sepal...

'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

'''데이터 전처리'''
# 파일 불러와서 데이터 프레임으로 변환
iris = load_iris()
#print(iris)

irisDF = pd.DataFrame(iris.data, columns=iris.feature_names)
irisDF['target'] = iris.target

# 데이터 타입 정보 확인
#print(type(irisDF))

# 각 컬럼별 타입 정보 확인
print(irisDF.info())

# 결측값 확인
print('결측값 확인 :', irisDF.isna().sum(), sep='\n')

# 박스 그래프를 통해 이상치 확인
# plt.boxplot(irisDF[irisDF.columns[:-1]])
# plt.show()

# 사분위수를 이용해서 이상치 제거.
q1 = irisDF['sepal width (cm)'].quantile(0.25)
q3 = irisDF['sepal width (cm)'].quantile(0.75)

iqr = q3-q1

maxmask = q3+1.5*iqr
minmask = q1 - 1.5*iqr

maxIdx = irisDF[irisDF['sepal width (cm)'] >maxmask].index
minIdx = irisDF[irisDF['sepal width (cm)']<minmask].index
irisDF = irisDF.drop(maxIdx)
irisDF = irisDF.drop(minIdx)
print(irisDF.info())

# 중복치 확인 => 1개 그냥 두기
print('중복값 : ',  irisDF.duplicated().sum())

# plt.boxplot(irisDF[irisDF.columns[:-1]])
# plt.show()
# 분포 확인
plt.scatter(irisDF[irisDF.columns[:2]], irisDF[irisDF.columns[2:-1]])
plt.show()


# 피처 + 타겟으로 나누기
featureDF = irisDF[irisDF.columns[:-1]]
targetDF = irisDF['target']


# 훈련용 데이터와 테스트용 데이터로 나누기.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(featureDF, targetDF, test_size = 0.3, stratify= targetDF)

print('X_train :', X_train.shape)
print(X_train.head(2))
print('X_test :', X_test.shape)
print(X_test.head(2))
print('y_train :', y_train.shape)
print(y_train.head(2))
print('y_test :', y_test.shape)
print(y_test.head(2))

# 모델 학습
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

modelK = KNeighborsClassifier()
modelK.fit(X_train, y_train)
print(modelK.score(X_test, y_test))


modelL = LogisticRegression(max_iter=100)
modelL.fit(X_train, y_train)
print(modelL.score(X_test, y_test))


# 성능 평가

y_preK = modelK.predict(featureDF)
print(y_preK)

y_preL = modelL.predict(featureDF)
print(y_preL)
print()


from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print('modelK R2_score : ', r2_score(targetDF, y_preK))
print('modelL R2_score : ', r2_score(targetDF, y_preL))
print('modelK mean_absolute_error :', mean_absolute_error(targetDF, y_preK))
print('modelL mean_absolute_error :', mean_absolute_error(targetDF, y_preL))
print('model1K mean_squared_error : ', mean_squared_error(targetDF, y_preK))
print('model1L mean_squared_error: ', mean_squared_error(targetDF, y_preK))