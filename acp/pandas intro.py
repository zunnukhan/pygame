import pandas as pd
import numpy as np

exam_data={"Name":["Alice","Bob","Charlie","Diana","Ethan"],
"Math score":[78,88,45,75,82],
"Science score":[85,92,50,80,88],
"Language score":[80,86,52,78,84],
"Attendence in persentage":[90,95,60,85,92]}
lables=[1,2,3,4,5]

df=pd.DataFrame(exam_data,index=lables)
print(df)
print("Summary of the basic information about this data fram and its data:")
print(df.info())