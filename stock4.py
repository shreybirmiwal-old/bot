import yfinance as yf
import pandas as pd

russ = pd.read_csv('rus2k.csv')['Symbol']
#russ = ["aapl", "tsla", "fcel", "snap", "crvs", "mmat", "ride", "bb", "uber"]
hypelist = []

for symb in russ:
	try:

		tick = yf.Ticker(symb.lower())
		gotData = tick.history(start="2021-09-22", interval="1d")

		del gotData['Dividends']
		del gotData['Stock Splits']
		del gotData['High']
		del gotData['Low']


		closeval = (gotData.iloc[0].Close)
		openval = (gotData.iloc[0].Open)

		change = closeval - openval
		changeper = (change/openval) * 100
		
		if(changeper > 5):
			print("hype " + symb)
			#print(changeper)
			hypelist.append(symb)
	except:
		print ("")

print(hypelist)

flat = []
for hypers in hypelist:
	#check if flat
	
	tick2 = yf.Ticker(hypers.lower())
	flatdata = tick2.history(start="2021-09-22")

	#print(flatdata)
	lowD = flatdata.iloc[1].Low
	highD = (flatdata.iloc[flatdata.shape[0] -1].High)
	difLowHigh = highD - lowD

	#print(difLowHigh)

	if(difLowHigh < .5):
		print("HYPE + FLAT!!")
		flat.append(hypers)

print(flat)




