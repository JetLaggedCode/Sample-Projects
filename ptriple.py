#Special Pythagorean Triple

a = 0
b = 0
c = 0
product = 0
for i in range(1,1000):
	a = i
	bc = 1000 - a
	for j in range(1,bc):
		b = j
		c = bc - b
		if a + b + c == 1000:
			if a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
				product = a * b * c
				break
print product