import pandas as pd 

data={

    "name":['ram','shayam','raj',"varun","arun","karun","aman","usama","harish","siraj","virat","rohit"],
    "age":[10,20,30,40,50,60,50,40,None,32,None,29],
    "city":["nagpur","mumbai","delhi",'gaya','indore',"chandighar","bijnor","noida","gurugram","masuri","raipur","alighar"],
    "salary":[35000,40000,32000,44000,45000,47000,50000,55000,None,None,42000,None],
    "performance_score":[75,28,91,59,69,37,84,85,82,74,None,75]   
}

df=pd.DataFrame(data)
print(df)

print("----SHAPE-----")
print(f'shape:{df.shape}')

print("------COLUMN NAME------")
print(f"colunm name:{df.columns}")

print("------MISSING VALUES------")
print(df.isnull().sum())

df["age"].fillna(df['age'].mean())

df["salary"].fillna(df["salary"].mean())

df["performance_score"].fillna(df["performance_score"].mean())

print("--------CLEAN DATA------------")
print(df)


df.insert(0,'empID',[10,11,12,13,14,15,16,17,18,19,20,21])
print("------NEW DATA------")
print(df)


