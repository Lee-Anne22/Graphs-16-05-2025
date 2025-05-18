import pandas as pd
df=pd.read_csv(r"annual-enterprise-survey-2023-financial-year-provisional-size-bands.csv")
#Columns in data
print("Data Columns in the Annual Enterprise Survey 2023:")
for col in df.columns:
    print (col)

#Number of columns
num_column=len(df.columns)
print(f"Number of columns:{num_column}")
#Number of rows
rows=df.shape
print("Number of Rows:{rows}")