
list = [5,10,15,20,25]
sumlist = sum(list)
countlist = len(list)
for i in list:
	mean = ((i+sumlist)/(countlist+1))
print (mean)