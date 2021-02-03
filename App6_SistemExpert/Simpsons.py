from kanren import Relation, fact,facts,var,run,conde


# Relaciones 
Progenitor = Relation()
Man = Relation()
Woman = Relation()


#Hechos
fact(Man,'Homero') # hecho verdadero cierto 
fact(Man,'Bart')
fact(Man,'Moe') 
fact(Man,'Mr Burns') 
fact(Man,'Kang') 
fact(Man,'Abraham') 
fact(Man,'Clancy') 
fact(Woman,'Lisa')
fact(Woman,'Marge')
fact(Woman,'Selma')
fact(Woman,'Maggie')
fact(Woman,'Mona')
fact(Woman,'Paty')
fact(Woman,'Jackeline')


facts(Progenitor,('Homero','Bart')
                ,('Marge','Bart')
                
     )
facts(Progenitor,('Homero','Lisa')
                ,('Marge','Lisa')
                
     )
facts(Progenitor,('Kang','Maggie')
                ,('Marge','Maggie')
                
     )
facts(Progenitor,('Abraham','Homero')
                ,('Mona','Homero')
                
     )
facts(Progenitor,('Clancy','Marge')
                ,('Jackeline','Marge')
                
     )
facts(Progenitor,('Clancy','Paty')
                ,('Jackeline','Paty')
                
     )
facts(Progenitor,('Clancy','Selma')
                ,('Jackeline','Selma')
                
     )

#Reglas
def Abuelo(X,Y):
    Z = var()
    return conde((Progenitor(X,Z),Progenitor(Z,Y),Man(X)))


def Abuela(X,Y):
    Z = var()
    return conde((Progenitor(X,Z),Progenitor(Z,Y),Woman(X)))

def Hermano(X,Y):
    Z = var()
    return conde((Progenitor(Z,X),Progenitor(Z,Y),Man(X)))

def Hermana(X,Y):
    Z = var()
    return conde((Progenitor(Z,X),Progenitor(Z,Y),Woman(X)))

def Madre(X,Y):
    Z = var()
    return conde((Progenitor(X,Y),Woman(X)))

def Padre(X,Y):
    Z = var()
    return conde((Progenitor(X,Y),Man(X)))

def Tio(X,Y):
    Z = var()
    return conde((Progenitor(Z,Y),Hermano(Z,X)))

def Tia(X,Y):
    Z = var()
    return conde((Progenitor(Z,Y),Hermana(Z,X)))

#### Inferencias de disque Experto 

X = var ()
Y = var ()

# Determinar el buelo de Bart

res = run (0,X,Abuelo(X,'Maggie')) 
#print (res)
#print (res[0])
#print ('"###########################')


# Determinar las tia de bart
madre = run (0,X,Madre(X,'Bart')) 
print (madre)
print ('"###########################3')
# Determinar las tia de bart
res = run (0,X,Tia(X,'Bart')) 
print (res)
print ('"###########################')

for i  in res:
    if (madre[0] != i ):
        print (i) 
        
        
lista = [x for x in res if x not in madre]        
print(lista)



