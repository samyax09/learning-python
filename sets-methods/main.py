s = {1,2,3,4,5,6,2}
s2 = {5,6,7,8,9}
s.add(7)
s.pop()
print(s.pop())
print(s.union(s2))
print(s.intersection(s2))
print(s.symmetric_difference(s2))
print(s.difference(s2))
print(s.isdisjoint(s2))
print(s.issuperset(s2))
