import math
import timeit
start = timeit.default_timer()


def simpleRandom(seed=1,c=12689):
	# Definition des constantes
	# a est un grand nombre
	# b est un grand nombre premier
	# c est également un nombre premier
	a = 10000
	b = 23459
	return (a*seed+b)%c



L = [simpleRandom(i) for i in range(10)]
print(L)


def simpleRandomSequence(seed=1,m=10):
	if m < 1:
		return []
	L = [simpleRandom(seed)]
	for i in range(1,m):
		L.append(simpleRandom(L[-1]))
	return L


L = simpleRandomSequence()
print(L)
L = simpleRandomSequence(2)
print(L)

def timeRandomSequence(m=101):
	timer = timeit.default_timer()
	t = math.floor(10000000 * timer)
	print(t)
	return simpleRandomSequence(t,m)

L = timeRandomSequence()
print(L)



def basicRandom(n,r=3.57):
	x = 0.5
	for _ in range(n):
		x = r * x * (1-x)
	return x

def basicRandomSequence(m=10,r=3.57):
	if m < 1:
		return []
	L = [basicRandom(100)]
	for i in range(m):
		x = r * L[-1] * (1-L[-1])
		L.append(x)
	return L

L = basicRandomSequence(20)
print(L)
