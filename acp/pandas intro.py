import pandas as pd
import numpy as np

exam_data={"Name":["Alice","Bob","Charlie","Diana","Ethan","Fiona",
"George","Hannah","Ian","Julia","Kevin","Laura","Michael","Nina","Oliver","Aaron","Bella","Carlos","Daisy","Edward","Fatima","Gabriel","Hazel","Isaac","Jasmine","Karim","Lily","Marcus","Nisha","Omar","Pooja","Quentin","Riya","Samuel","Tanya"],
"Math score":[78,88,45,75,82,72,95,83,67,100,76,89,91,70,98,91,76,84,100,63,95,72,88,60,97,69,83,75,92,66,81,79,90,68,94],
"Science score":[85,92,50,80,88,60,62,75,88,91,95,73,84,67,90,65,72,97,83,91,76,88,69,95,74,86,93,79,67,90,81,96,70,85,92],
"Language score":[80,86,52,78,84,76,82,95,88,100,79,91,84,97,75,92,77,85,94,99,76,83,97,88,90,79,95,81,93,87,98,82,96,89,75],
"Attendence in persentage":[90,95,60,85,92,60,74,83,99,62,91,77,68,95,88,60,74,83,99,62,91,77,68,95,88,72,96,85,63,90,79,66,84,97,69]}
lables=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35]

df=pd.DataFrame(exam_data,index=lables)
print(df)
print("Summary of the basic information about this data frame and its data:")
print(df.info())