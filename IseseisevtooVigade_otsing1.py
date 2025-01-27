from math import * #import valesti tehtud
print("Ruudu karakteristikud")
a=int(input('Sisesta ruudu külje pikkus => ')) #lisan int, )
S=a**2)
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt, P") #valesti '
di=a*math.sqr(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") #emaldasin )
b=input("Sisesta ristküliku 1. külje pikkus => ")
c=input("Sisesta ristküliku 2. külje pikkus => ")
S=b*c
print("Ristküliku pindala", S) #lisan "
P=2*(b+c)   #lisan *
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di)) #lisan )
print()
print("Ringi karakteristikud")
r=input("Sisesta ringi raadiusi pikkus =>") #lisan ", emaldasin )
d=2*r  #lisan *
print("Ringi läbimõõt", d) #lisan ,
S=pi*r*2 #emaldasin ()
print("Ringi pindala", round(S))
C=2*pi*r #emaldasin ()  #lisan *
print("Ringjoone pikkus", round(C)) #lisan )