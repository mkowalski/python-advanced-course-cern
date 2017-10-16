items = [1, 2, 3, 4, 5]
items2 = ( int(d) for d in '12345' )


def sqr(x): return x ** 2


as1 = list(map(lambda x: x**2, items))
as2 = list(map(sqr, list(items2)))

print(as1)
print(as1 == as2)

as3 = list(map(int, items))
as4 = list(map(int, list( ( int(d) for d in '12345' ) )))

print(as3)
print(as3 == as4)
