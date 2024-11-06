from scipy import stats

def normalidad_ks(df):

    data_mean = df.mean()
    data_std = df.std()
    
    return stats.kstest(df, 'norm', args=(data_mean, data_std))