with open('input.txt','r')as f:
    lista1=list(eval(f.read()))
    lista2=sorted(lista1)
    lista3=sorted(lista1,reverse=True)
    lista4=lista1+[111]
with open ('output.txt','w') as f:
    f.write(list('lista1: ', lista1))
    f.write('lista2(in ordine crecatoare): ', lista2)
    f.write('lista3(in ordine descrescatoare): ', lista3)
    f.write('numarul de caractere: ' , len(lista1))
    f.write('nr maxim din lista: ', max(lista1))
    f.write('nr minim din lista: ', min(lista1))
    f.write('lista4: ', lista4)
    