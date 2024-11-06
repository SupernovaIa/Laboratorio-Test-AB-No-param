from scipy import stats

def normalidad_ks(df):

    data_mean = df.mean()
    data_std = df.std()
    
    return stats.kstest(df, 'norm', args=(data_mean, data_std))


def test_no_param(datos, dependencia=False):

    if len(datos) > 2:
        print('Test Kruskal Wallis')
        return stats.kruskal(*datos)

    elif len(datos) == 2 and dependencia:
        print('Wilcoxon')
        return stats.wilcoxon(*datos)

    elif len(datos) == 2 and not dependencia:
        print('Test U')
        return stats.mannwhitneyu(*datos)

    else:
        print('Tienes que pasar al menos 2 grupos')