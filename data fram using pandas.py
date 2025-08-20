import pandas as pd
import numpy as np

exam_data={"name":["Anushka","Devanshi","Kartik","Janavi","Elsa","Mansi","Muhammad","Lavanya","Lilly","Kaveri"],
"score":[12.5,16.5,9,20,np.nan,7,17.5,13,np.nan,13],
"attempts":[ 2, 3,  2, 1, 1, 3, 2, 3, 1, 1 ],
"qualify":["no","no","yes","yes","yes","yes","no","yes","no","yes"]}
lables=["a","b","c","d","e","f","g","h","i","j"]

df=pd.DataFrame(exam_data,index=lables)
print(df)
print("Summary of the basic information about this data fram and its data:")
print(df.info())