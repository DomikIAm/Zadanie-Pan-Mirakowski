import collections
a=1
b=1
c=1
d=4
e=5
list=[a,b,c,d,e]
lista = collections.Counter(list)
if 3 in lista.values():
    print("Trzy liczby są takie same")
else:
    print("Trzy liczby nie są takie same")
    
