d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = {i : d1.get(i,0) + d2.get(i,0) 
    for i in set(d1).union(d2)}

print(d)