'''
모델을 활용한 서비스 제공
'''

# 모듈 로딩
from joblib import load

# 전역 변수
mdl_file = '../model/iris_df.pkl'

# 모델 로딩
mdl = load(mdl_file)

# 로딩된 모델 확인
print(mdl.classes_)

# 붓꽃 정보 입력 => 4개 피처
datas = input('붓꽃 정보 입력 (예 : 꽃받침 길이, 꽃받침 너비, 꽃잎 길이, 꽃잎 너비 순서) : ')
if len(datas):
    #d = datas.split(',')
    #print(d)
    #ret = map(float, d)
    #print(list(ret))
    datas_list=list(map(float, datas.split(',')))


    # 입력된 정보에 해당하는 품종 알려주기
    # 모델의 predict(2d)
    irs_pre = mdl.predict([datas_list])
    irs_prob = mdl.predict_proba([datas_list])
    print(f'해당 꽃은 {irs_prob}% {irs_pre[0]}입니다.')

else :
    print('입력된 정보가 없습니다.')