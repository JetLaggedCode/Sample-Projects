#10001st prime

plist = [2]
temp = plist[-1]
while len(plist) <= 10001:
	prime = True
	temp += 1
	#print temp
	for i in plist:
		if temp % i == 0:
			prime = False
			break
	if prime == True:
		plist.append(temp)
		#print plist
print(plist[-1:])
