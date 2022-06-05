y = lambda a,b: a*b
print(y(6,8))

p = [2,3,7,6]
for item in p:
    print(item+5)

print(list(map(lambda item: item + 5,p)))

[item for item in p if item % 2 == 1]
print(list(filter(lambda item: item % 2 == 1, p)))

def f(n):
    return lambda a: a*n

doubler = f(2)
print(doubler(11))

tripler = f(3)
print(tripler(55))

#args and kwags (key word arguments)

def pargs(a, *args):
    print(a, sum(args))
pargs(1,4,5,6,-2)

def pargs(a, *args):
    print(a, args[0] + args[2])
pargs(1,4,5,6,-2)


def printkw(a, **kwargs):
    print(a, kwargs)
printkw(1, x=78, y=34)