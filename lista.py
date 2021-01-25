x=[-1,0,-5,-7,-6,5,6,7,9,2,-3]
lista1=x
print('lista1=', lista1)
lista2=sorted(x)
print('lista2=', lista2)
x.sort(reverse=True)
lista3=x
print('lista3=', lista3)
print(len(x))
print('nr maxim=', max(x))
print('nr minim=', min(x))
x.extend([111])
print('lista4=', x)
x.insert(1,222)
x.remove(111)
print('lista5=', x)