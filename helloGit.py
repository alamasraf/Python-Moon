
import numpy as np

arr=np.array([10, 40, 50, 51, 53, 55, 57, 59, 210, 11, 90, 60])

flary=[]

for ele in arr:
	if ele > 50:
		flary.append(True)
	else:
		flary.append(False)

farry=arr[flary]
farry.sort() # show our result in sorted arrangement 

print(farry) 

#print("its a fork")

#print ("a new fork")

print("farry has been sorted by asrf")

#print("its a test of file updating.")
#print ("new changes")


#print ("more test")

