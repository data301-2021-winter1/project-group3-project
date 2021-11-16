import pandas as pd
import numpy as np
import seaborn as sns
from scipy import stats

def rawdata(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    return df

def process_data(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    CCdata = (df.columns = ['age',  'workclass','fnlwgt', 'education','education-num','marital-status','occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss' ,  'hours-per-week','native-country', 'salary' ])
    return CCdata

def useless_col(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    df_clean = df.dropna(axis=0)
    return df_clean

def f_salary(csv_data):
    df = pd.read_csv("../data/raw/adult.data")
    df1 = (df['salary'] = pd.factorize(df['salary'])[0])
    return df1

def mode_data(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    a = np.array(df[column])
    n = stats.mode(a)
    return n
    
    
