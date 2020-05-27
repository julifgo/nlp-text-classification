from sklearn.utils import resample
from imblearn.over_sampling import SVMSMOTE
import pandas as pd

def upsampleRandom(df,minorityColumn, minorityValue,sample_rate):
    assert sample_rate > 1 , 'You are upsampling, provide rate > 1.'
    samples_length = int(len(df[df[minorityColumn]==minorityValue])*sample_rate) #Me quedo con sample_rate porciento de lo que tiene (duplico, llevo a la mitad, etc)
    minority_class = df[df[minorityColumn]==minorityValue]
    minority_upsampled = resample(minority_class,
                          replace=True, # sample with replacement
                          n_samples= samples_length, 
                          random_state=42) # reproducible results
    df_aux = df[df[minorityColumn] != minorityValue]
    df_aux = pd.concat([df_aux, minority_upsampled])
    return df_aux

def downsampleRandom(df,majorityColumn, majorityValue,sample_rate):
    assert sample_rate < 1 , 'You are downsampling, provide rate < 1.'
    samples_length = int(len(df[df[majorityColumn]==majorityValue])*sample_rate) #Me quedo con sample_rate porciento de lo que tiene (duplico, llevo a la mitad, etc)
    majority_class = df[df[majorityColumn]==majorityValue]
    majority_downsampled = resample(majority_class,
                          replace=False,
                          n_samples= samples_length, 
                          random_state=42) # reproducible results
    df_aux = df[df[majorityColumn] != majorityValue]
    df_aux = pd.concat([df_aux, majority_downsampled])
    return df_aux

#Support just 'number' matrixes
def upsampleSvmSmote(params,X,y):
    svmsmote = SVMSMOTE(**params)
    X_rs, y_rs = svmsmote.fit_sample(X, y)
    return X_rs, y_rs
    