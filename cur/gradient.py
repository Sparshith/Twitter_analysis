import csv
import sys
import collections

lis1=[]
lis2=[]
ind=[]

with open('twitter_stats.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
    	lis1.append(row[2])
    	lis2.append(row[1])

    	
del(lis1[0])
del(lis2[0])

count1= len(lis1)
lis3= set(lis2)
lis3= list(lis3)
count2= len(lis3)


for j in range(0,count2):
	#count=0
	indices=[]
	indices = [i for i, x in enumerate(lis2) if x == lis3[j]]
	count3= len(indices)
	for k in range(0,count3-1):
		print int(lis1[indices[k+1]])-int(lis1[indices[k]]),
		if(k<count3-2):
			print ",",
	print ""



