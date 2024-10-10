#simple

a = 33
b = 200

if  b > a:
    print(b,"es mayor ", a)


#doble
y = 200
z = 333
if y < z:
    print(y,"es mayor que", z)
else:
    print(y,"no es mayor que", z)


#multiple
p=200
t=207
if p>t:
    print(p,"es mayor que", t)
elif p<t:
    print(p,"es menor que ",t)
else:
    print(p,"es igual que",t)

#condiciones enlazadas

v =28
if v >10:
    print("por encima de diez,")
if v >20:
    print("y tambien por encima de 20!")
else:
    print("pero no pro encima de 20.")


#parametros de end y sep

print("esrudiar los sabados ", end= '')
print("es genial")
#print("esrudiar los sabados ", end= '')
#print("es genial")




print("duban", "carlos", "pedro", "sara")#agregar un espacio por dfecto
print("duban", "carlos", "pedro", "sara", sep="")#quita el espacio
print("duban", "carlos", "pedro", "sara", sep=",")#agrega una coma

print("duban", "carlos", "pedro", "sara", sep="_", end="_curso_python")#implementacion de end y set





