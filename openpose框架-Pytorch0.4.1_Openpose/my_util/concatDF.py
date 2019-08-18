import pandas as pd
import glob


csv_num = glob.glob('../csv/*.csv')
print("csv_num = ",len(csv_num))
# cancat dataframe
df = pd.DataFrame()
for i in range(len(csv_num)):
	d = pd.read_csv("../csv/df{}.csv".format(i))
	df = pd.concat([d,df])

df.to_csv("result-student.csv")
print(df)