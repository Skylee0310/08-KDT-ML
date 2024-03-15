

def check_null(df) :
    dfna = df.isna().sum()
    if dfna == True :
        print('결측값이 있습니다.')
    else :
        print('결측값이 없습니다.')

def remove_outlier(df, col, n):
    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3-q1

    boundary = iqr*n

    idx1 = df[df[col]>q3+boundary].index
    idx2 = df[df[col]<q1-boundary].index

    df = df.drop(idx1) # 최댓값보다 큰 이상치 drop
    df = df.drop(idx2) # 최솟값보다 작은 이상치 drop
    df = df.reset_index(drop=True)
    return df

def print_feature(nrows, ncols, df, target, features, corr) :
    plt.figure(figsize=(10, 10))
    for idx in range(len(features)):
        plt.subplot(nrows, ncols, idx+1)
        plt.scatter(df[target], df[features[idx]], label =f'corr : {corrs[idx]:.2}')
        plt.xlabel(target)
        plt.ylabel(features[idx])
        plt.legend()
    plt.tight_layout() # 간격 안 맞는 거 맞춰주는 건가..?
    plt.show()