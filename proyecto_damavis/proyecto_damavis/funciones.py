def comp_dentro_lab(pos,filas,columnas):#esta funcion comprueba si una posicion dada por sus coordenadas se encuentra dentro de la matriz del laberinto, dando el numero de filas y columnas del mismo.
    if (pos[0]>=0 and pos[0]<filas)and(pos[1]>=0 and pos[1]<columnas):
        return True
    else:
        return False

def comp_inicio_val(pos,filas,columnas):#esta funcion comprueba si la primera posicion del objeto, que viene dado por sus coordenadas, se encuentra dentro de la matriz del laberinto, dando el numero de filas y columnas del mismo. Es diferente a la funcion anterior porque recibe una lista de posiciones como entrada
    if (pos[-1][0]>=0 and pos[-1][0]<filas)and(pos[-1][1]>=0 and pos[-1][0]<columnas):
        return True
    else:
        return False
        
def mov0(izq,cen,der):#movimiento hacia la derecha
    nizq=[izq[-1][0],izq[-1][1]+1]
    ncen=[cen[-1][0],cen[-1][1]+1]
    nder=[der[-1][0],der[-1][1]+1]
    return nizq,ncen,nder

def mov1(izq,cen,der):#movimiento hacia abajo
    nizq=[izq[-1][0]+1,izq[-1][1]]
    ncen=[cen[-1][0]+1,cen[-1][1]]
    nder=[der[-1][0]+1,der[-1][1]]
    return nizq,ncen,nder

def mov2(izq,cen,der):#giro
    ncen=[cen[-1][0],cen[-1][1]]
    if izq[-1][1]<cen[-1][1]:#se comprueba si el objeto se ecuentra horizontal o vertical
        nizq=[cen[-1][0]-1,cen[-1][1]]
        nder=[cen[-1][0]+1,cen[-1][1]]
    else:
        nizq=[cen[-1][0],cen[-1][1]-1]
        nder=[cen[-1][0],cen[-1][1]+1]
    return nizq,ncen,nder

def mov3(izq,cen,der):#movimiento a la izquierda
    nizq=[izq[-1][0],izq[-1][1]-1]
    ncen=[cen[-1][0],cen[-1][1]-1]
    nder=[der[-1][0],der[-1][1]-1]
    return nizq,ncen,nder

def mov4(izq,cen,der):#movimeinto hacia arriba
    nizq=[izq[-1][0]-1,izq[-1][1]]
    ncen=[cen[-1][0]-1,cen[-1][1]]
    nder=[der[-1][0]-1,der[-1][1]]
    return nizq,ncen,nder

def comp_obst(ni,nc,nd,labyrinth):#se comprueba si al llegar a una nueva psoicion, esta es valida
    if labyrinth[ni[0]][ni[1]]=='.' and labyrinth[nc[0]][nc[1]]=='.' and labyrinth[nd[0]][nd[1]]=='.':
        return True
    else:
        return False


def comp_obst_giro(nc,labyrinth):#se comprueba si se puede hacer el giro, comprobando todas las posiciones alrededor del centro
    if labyrinth[nc[0]][nc[1]]=='.' and labyrinth[nc[0]-1][nc[1]-1]=='.' and labyrinth[nc[0]-1][nc[1]]=='.' and labyrinth[nc[0]-1][nc[1]+1]=='.'and labyrinth[nc[0]][nc[1]-1]=='.' and labyrinth[nc[0]][nc[1]+1]=='.' and labyrinth[nc[0]+1][nc[1]-1]=='.' and labyrinth[nc[0]+1][nc[1]]=='.' and labyrinth[nc[0]+1][nc[1]+1]=='.':
        return True
    else:
        return False

def compr_compl(pos,filas,columnas):#se comprueba si se ha llegado al final del laberinto
    if pos[-1][0]==filas-1 and pos[-1][1]==columnas-1:
        return True
    else:
        return False