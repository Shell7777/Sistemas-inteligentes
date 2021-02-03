from kanren import Relation, fact,facts,var,run,conde

padre = Relation()
madre = Relation()

facts(padre,('Vito','Michael'),
            ('Vito','Sonny'),
            ('Vito','Fredo'),
            ('Michael','Anthony'),
            ('Michael','Mary'),
            ('Sonny','Vincent'),
            ('Sonny','Kathryn'),
            ('Sonny','Francesca'),
            ('Sonny','Frank'),
            ('Sonny','Santino'),
    )
facts(madre,('Carmela','Michael'),
            ('Carmela','Sonny'),
            ('Carmela','Fredo'),
            ('Kay','Mary'),
            ('Kay','Anthony'),
            ('Sandra','Francesca'),
            ('Sandra','Kathryn'),
            ('Sandra','Kathryn'),
            ('Sandra','Kathryn'),
            ('Sandra','Santino')
    )


def padres (nombre):
    q = var ()
    return [run(0,q,padre(q,nombre)),run(0,q,madre(q,nombre))]


def hermanos (nombre):
    q = var ()
    padre1 = run(0,q,padre(q,nombre))
    madre1 = run(0,q,madre(q,nombre))
    return [run(0,q,padre(padre1[0],q)),run(0,q,madre(madre1[0],q))]

def hijos (nombre):
    q = var ()
    return run(0,q,padre(nombre,q))

def abuelos(nombre):
    q = var ()
    padre1 = run(0,q,padre(q,nombre)) 
    print (padre1[0])
    return run(0,q,padre(q,padre1[0]))


def padres2 (p,child):
    return  conde([padre(p,child)],[madre(p,child)])
def abuelos2(gfather,hijo):
    p = var ()
    return conde((padres2(gfather,p),padres2(p,hijo)))


q = var ()

# vito es padre de ................
#print ((run(0,q,padre('Vito',q))))


#  quien es el papa de Michael

#print ((run(0,q,padre(q,'Michael'))))

#print (padres('Michael'))
print ((run (0,q, abuelos2('Vito',q))))

# todos los esposos 
x,y,z = var (),var (),var (),
print (run (0,(x,y),(padre,x,z),(madre,y,z)))
