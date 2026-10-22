
import pandas as pd
import numpy as np

 



def simple_dataframes():
    print("one with a single column(a SERIE)")
    s = pd.Series([10, 20, 30], index=["a", "b", "c"])
    print(s["b"])
    print(s * 2)

    print('another with multiple columns(A DATAFRAME)')
    members= pd.DataFrame({"name":["fik","ray","rick","whit"],
                         "age":[10,20,30,24],
                         "city":["kampala","masaka","mbaale","gulu"],
                         "score":[24.5,21.7,33.5,28.7]}
                         )

    print(members)

    print("\n another from a numpy array")
    data = pd.DataFrame(np.arange(12).reshape(4,3), columns=["a","b","c"])
    print(data) 

#simple_dataframes()

class importing_data():
    
    def __init__(self,csv,excel="non",zip="non"):
        self.csv = csv
        self.excel = excel
        self.zop = zip
    
    def reading_cvs(self):
        csv_data =pd.read_csv(self.csv)

        
        print(csv_data.head())
business = importing_data(csv="PANDAS/test_data.csv")
#business.reading_cvs()

print("MAKING A DATAFRAME FROM A RANDOM DATASET")

rng = np.random.default_rng(seed=42)
n=10

df = pd.DataFrame({
    "CLASS": ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10'],
    "MATH": rng.integers(0,100,size = n),
    "ENGLISH": rng.integers(0,100,size = n),
    "SCIENCE": rng.integers(0,100,size = n),
    "HISTORY": rng.integers(0,100,size = n),
    "AVERAGE":np.nan
})
subject_cols = ["MATH", "ENGLISH", "SCIENCE", "HISTORY"]

df.loc[len(df)] = {
    "CLASS": "TOTAL",
    **df[subject_cols].sum().to_dict(),
    "AVERAGE": np.nan,
}

print(df)




