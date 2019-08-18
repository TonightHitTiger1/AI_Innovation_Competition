import os
import glob


def delfile():
	filenames = glob.glob("../csv/*.csv")
	print("now has file=",len(filenames))
	for filename in filenames:
		try:
			os.remove(filename)
		except:
			print("file not exits")

#     filenames = glob.glob(path + r"\*.csv")
# print("now has file=", len(filenames))
