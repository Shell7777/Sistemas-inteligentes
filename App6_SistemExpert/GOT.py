from kanren import Relation, fact,facts,var,run,conde

Progenitor = Relation()
hombre = Relation()
mujer = Relation()


fact(hombre,'Richard')
fact(hombre,'Eddart')
fact(hombre,'Brandom')
fact(hombre,'Benjen')
fact(hombre,'Robb')
fact(hombre,'Bran')
fact(hombre,'Rickon')
fact(hombre,'Aegon')
fact(hombre,'Viserys')
fact(hombre,'Rhaegar')
fact(hombre,'Aerys')
fact(hombre,'Jon')

fact(mujer,'Lyarra')
fact(mujer,'Catelyn')
fact(mujer,'Lyanna')
fact(mujer,'Sansa')
fact(mujer,'Arya')
fact(mujer,'Elia')
fact(mujer,'Rhaella')
fact(mujer,'Rhaenys')
fact(mujer,'Daenerys')


facts(Progenitor,('Richard','Eddart')
                ,('Lyarra','Eddart')
                
     )
facts(Progenitor,('Richard','Brandom')
                ,('Lyarra','Brandom')
                
     )
facts(Progenitor,('Richard','Benjen')
                ,('Lyarra','Benjen')
                
     )
facts(Progenitor,('Richard','Lyanna')
                ,('Lyarra','Lyanna')
                
     )

facts(Progenitor,('Eddart','Robb')
                ,('Catelyn','Robb')
                
     )
facts(Progenitor,('Eddart','Sansa')
                ,('Catelyn','Sansa')
                
     )
facts(Progenitor,('Eddart','Arya')
                ,('Catelyn','Arya')
                
     )
facts(Progenitor,('Eddart','Bran')
                ,('Catelyn','Bran')
                
     )
facts(Progenitor,('Eddart','Rickon')
                ,('Catelyn','Rickon')
                
     )


facts(Progenitor,('Aerys','Rhaegar')
                ,('Rhaella','Rhaegar')
                
     )
facts(Progenitor,('Aerys','Viserys')
                ,('Rhaella','Viserys')
                
     )
facts(Progenitor,('Aerys','Daenerys')
                ,('Rhaella','Daenerys')
                
     )
facts(Progenitor,('Rhaegar','Rhaenys')
                ,('Elia','Rhaenys')
                
     )
facts(Progenitor,('Rhaegar','Aegon')
                ,('Elia','Aegon')
                
     )
facts(Progenitor,('Rhaegar','Jon')
                ,('Lyanna','Jon')
                
     )

#abuelo
    
#abuela

def abuelo(x,y):
    z = var()
    return conde((Progenitor(x,z),Progenitor(z,y),hombre(x)))
def abuela(x,y):
    z = var()
    return conde((Progenitor(x,z),Progenitor(z,y),mujer(x)))
#padre
def padre(x,y):
    return conde((Progenitor(x,y),hombre(x)))
def madre(x,y):
    return conde((Progenitor(x,y),mujer(x)))
#hermano
def hermano(x,y):
    z=var()
    return conde((Progenitor(z,x),Progenitor(z,y),hombre(x)))
#hermana
def hermana(x,y):
    z=var()
    return conde((Progenitor(z,x),Progenitor(z,y),mujer(x)))
#tio
def tio(x,y):
    z=var()
    return conde((Progenitor(z,y),hermano(z,x),hombre(x)))
#tia
def tia(x,y):
    z=var()
    return conde((Progenitor(z,y),hermano(z,x),mujer(x)))

#sobrino
def sobrino(x,y):
    z=var()
    y=var()
    return conde((Progenitor(z,y),Progenitor(z,y),Progenitor(y,x),hombre(x)))
#sobrina
def sobrina(x,y):
    z=var()
    y=var()
    return conde((Progenitor(z,y),Progenitor(z,y),Progenitor(y,x),mujer(x)))



q = var()
print ("############### Padres #################")
print (run(0,q,madre(q,'Eddart')))
print (run(0,q,padre(q,'Eddart')))
print ("############### Hermano #################")
print (run(0,q,hermano(q,'Eddart')))
print (run(0,q,hermana(q,'Eddart')))
print ("################ Tios ################")
print (run(0,q,tio(q,'Sansa')))
print (run(0,q,tia(q,'Sansa')))
print ("################    Abuelos  ################")
print (run(0,q,abuelo(q,'Sansa')))
print (run(0,q,abuela(q,'Sansa')))
print ("################    Sobrino  ################")
print (run(0,q,sobrino(q,'Benjen')))
print (run(0,q,sobrina(q,'Benjen')))



