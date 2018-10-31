import urllib.request as req

i=1
f = open("ambulance.txt")
for x in f:
	try:
		req.urlretrieve(str(x),str(i))
		i+=1
	except:
		d=1
print(i)