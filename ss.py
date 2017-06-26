#Difference of Squares
summed = 0
squared = 0

for i in range (1,100):
	summed += i
	squared += (i ** 2)
	print squared
#summed2 = summed ** 2

summed2 = 5050 ** 2
result = summed2 - squared
print result