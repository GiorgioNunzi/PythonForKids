name=input('nome')
print('Ciao '+name)
a=input('Inserisci il primo numero: ')
b=input('Inserisci il primo numero: ')
print("I numeri che mi hai dato sono: "+a+" e "+b)

a_int=int(a)
b_int=int(b)
type_a=type(a)
type_a_int=type(a_int)
print("La variable a è di questo tipo; "+str(type_a))
print("La variable a_int è di questo tipo; "+str(type_a_int))

c=a_int+b
print(c)

d=a_int/b_int
d_int=int(d)
print(str(a_int)+" diviso "+str(b_int)+" fa "+str(d)+" arrotondato al decimale "+str(d_int))

e=d_int*b_int
print("Il prodotto è "+str(e))

if e==a_int:
    print(a+' è pari')
else:
    print(a+' è dispari')
