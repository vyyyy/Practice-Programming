#implementation 1: for loop
#procedural

for i in range(101):
	if i%3==0 and i%5==0:
		print('FizzBuzz')
	elif i%3==0:
		print('Fizz')
	elif i%5==0:
		print('Buzz')
	else:
		print(i)

#implementation 2: list comprehension
#where f(x) == 0

print(['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3==0 else 'Buzz' if i%5==0 else i for i in range(101)])

#implementation 3: list comprehension
#where !f(x)

print(['FizzBuzz' if not i%3 and not i%5 else 'Fizz' if not i%3 else 'Buzz' if not i%5 else i for i in range(101)])
