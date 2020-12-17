l=[1,2,"ram",3,4,5,3]
t=(1,4,3,4,4,2)
s={2,4,562,"ram",45}
d={"prathap":45,"gevi":2, "prathi":30}
print(tuple(sorted(t)))
print(tuple(sorted(t,reverse=True)))

print(sorted(d.keys()))
print(sorted(d.keys(),reverse=True))

print(sorted(d.values()))
print(sorted(d.values(),reverse=True))


print(dict(sorted(d.items())))
print(dict(sorted(d.items(),reverse=True)))

print(dict(sorted(d.items(), key=lambda item: item[1],reverse=True)))