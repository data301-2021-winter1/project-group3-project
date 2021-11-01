import pandas as pd

class pipeline:
    
    @staticmethod
    def load_data():
        
        df =  pd.read_csv("../data/raw/adult.data")
        df.columns =['age',  'workclass','fnlwgt', 'education','education-num','marital-status','occupation', 'relationship', 
                       'race','sex', 'capital-gain', 'capital-loss' ,  'hours-per-week','native-country', 'salary']
        # drop useless row
        df['salary'] = pd.factorize(df['salary'])[0]
        df['sex'] = pd.factorize(df['sex'])[0]
        
        ### add argreget columns
        df2 = (
        df
        .dropna()
        .reset_index(drop=True)
        )
        del df2["fnlwgt"]
        del df2["age"]
        del df2["education"]
        del df2["education-num"]
        del df2["relationship"]
        del df2["capital-gain"]
        del df2["capital-loss"]
        del df2["hours-per-week"]
        del df2["native-country"]
        del df2["workclass"]
        del df2["marital-status"]
        
        return df2
    
    
