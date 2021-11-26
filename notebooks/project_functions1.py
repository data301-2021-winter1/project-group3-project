import pandas as pd

class pipeline:
    
    @staticmethod
    def load_data():
        
        # read in data
        df =  pd.read_csv("../data/raw/adult.data")
        # name columns properly 
        df.columns =['age',  'workclass','fnlwgt', 'education','education-num','marital-status','occupation', 'relationship', 
                       'race','sex', 'capital-gain', 'capital-loss' ,  'hours-per-week','native-country', 'salary']
        
        # factorize columns 
        df['salary'] = pd.factorize(df['salary'])[0]
        df['sex'] = pd.factorize(df['sex'])[0]
        
        ### drop n/a columns, reset index, and drop unused columns 
        df2 = (
        df
        .dropna()
        .reset_index(drop=True)
        .drop(['fnlwgt', 'age', 'education', 'education-num','relationship', 'capital-gain', 'capital-loss', 'hours-per-week', 
               'native-country', 'workclass',   'marital-status'], axis=1)
        )
        
        return df2
    
    def save_data(df, str):
        df.to_csv(f"../data/processed/{str}.csv")
    
