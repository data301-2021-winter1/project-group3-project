# Kevin Pierce 
import pandas as pd
import numpy as np
import seaborn as sns

def unprocessed(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    return df

def named_columns(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    df1_clean = (df.columns = ['age',  'workclass','fnlwgt', 'education','education-num','marital-status','occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss' ,  'hours-per-week','native-country', 'salary'])
    return df1_clean

def processed_columns(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    df2_clean = (df.drop(['fnlwgt','education-num','capital-gain','capital-loss'])
           .value_counts("Education")
           .value_counts("Occupation")
           .unique("Education")
    return df2_clean

def age_processed(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    df3_clean = (df1_clean.dropna(axis=0))
                 .sort_values(by ='age', ascending = True)
                 .rename(columns = {"hours-per-week":"Weekly Hours"}, inplace = True)
                 .nunique()
                 .dtypes()
    return df3_clean

def workclass_processed(csv_file):
    df = pd.read_csv("../data/raw/adult.data")
    df4_clean = (df1_clean.dropna(axis=0))
                 .sort_values(by ='workclass', ascending = True)
    return df4_clean

