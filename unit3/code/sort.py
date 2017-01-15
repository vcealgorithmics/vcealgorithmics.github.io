ourList =  [1,2,5,6,9,10,24,52,253,1423,131434]
lookingFor = 253
for item in ourList:
	if item == 5:
		print("Found it!")




ourList =  [1,2,5,6,9,10,24,52,253,1423,131434]
lookingFor = 253
lower = 0
upper = len(ourList)
# gotta test
while lower < upper: 
	midpoint = (lower + upper) // 2 # // just means divide and round down
	if ourList[midpoint] == lookingFor:
		print("Found it!")
	elif ourList[midpoint] > lookingFor:
		upper = midpoint
	else:
		lower = midpoint