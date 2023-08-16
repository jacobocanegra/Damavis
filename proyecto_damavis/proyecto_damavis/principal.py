import sys
import os

# Para evitar problemas de rutas
ruta_actual = os.path.dirname(os.path.abspath(__file__))
sys.path.append(ruta_actual)

import funciones    #incluye las funciones creadas del archivo funciones

def main(labyrinth):
    if not isinstance(labyrinth, list) or not all(isinstance(row, list) for row in labyrinth):
        raise TypeError("El laberinto debe ser una lista de listas.")
    
    cols = len(labyrinth[0])#dimensiones del laberinto introducido
    filas=len(labyrinth)   
    if not all(len(row) == cols for row in labyrinth):
        raise ValueError("Todas las filas del laberinto deben tener el mismo número de columnas.")
    
    # Verificar si todas las celdas son "." o "#"
    for row in labyrinth:
        if not all(cell == "." or cell == "#" for cell in row):
            raise ValueError("Las celdas del laberinto deben contener solo '.' o '#'.")
    izq=[[0,0]]  #coordenadas iniciales del objeto
    cen=[[0,1]]
    der=[[0,2]]

    vali=funciones.comp_inicio_val(izq,filas,cols)  #se comprueba que las coordenadas iniciales sean válidas
    valc=funciones.comp_inicio_val(cen,filas,cols)
    vald=funciones.comp_inicio_val(der,filas,cols)
    if vali==False or valc==False or vald==False:
        sal=-1 #de no ser válidas, el programa acaba directamente
    else:
        comp=funciones.compr_compl(der,filas,cols)#se comprueba si se está en el caso de que el laberinto sea [[".",".","."]]
        imp=False  #se inicia la variable imp (imposible) que será True si se detecta que no hay solución
        movs=[] #lista para incluir movimientos
        regreso=False #se inicia la variable regreso, que solo será True cuando el objeto llegue a un callejón sin salida y deva volver atrás
        while comp==False and imp==False:#mientras que no se haya llegado a la meta o se haya llegado a la conclusión de que es imposible llegar
            if regreso==True:#cuando se haya detectado un callejón sin salida
                movval=False#la variable movval será False cuando aún no se haya encontrado un movimiento válido al que ir desde la posición en la que se encuentra el objeto
                regreso=False#se pasa la variable de regreso a False
                izq=izq[:-1]#se fuerza a que se "olviden" las ultimas coordenadas, al haber llevado a una ruta erronea
                der=der[:-1]
                cen=cen[:-1]
                movs=movs[:-1]
            else:
                movs.append(-1)#si no se esta retrocediendo, se comienza el nuevo paso añadiendo a la lista de movimientos "-1", valor que se cambiará por el siguiente paso de haber uno factible
            umov=movs[-1]#variable con -1 o con el último paso dado ( en el caso de que se esté retrocediendo, para no volver a dar el mismo paso)
            if len(movs)>1:#para asegurar que no entramos en un bucle simple ( el objeto por ejemplo no para de moverse de izq a der constantemente), se usa la variable ultimo
                ultimo=movs[-2]#la variable ultimo almace el ultimo paso que se dió, para forzar al objeto a no dar un paso que anule lo que acaba de hacer
            else:
                ultimo=-1  #de encontrarse en el primer paso, es imposible que el objeto empiece deshaciendo un ultimo paso, por lo que se le da como valor -1    
            if umov<0 and ultimo!=3:#Se comienza a realizar el movimiento. Si umov no es 0 ( es decir, no se esta retrocediendo despues de haber hecho la accion 0, y el ultimo paso no fue ir hacia la izquierda, se va hacia la derecha)
                ni,nc,nd=funciones.mov0(izq,cen,der)#el objeto se mueve a la derecha
                ival=funciones.comp_dentro_lab(ni,filas,cols)#se comprueba que el objeto no se haya salido del laberinto
                ider=funciones.comp_dentro_lab(nd,filas,cols)
                if ider==ival and ival==True:#de no haber salido, se comprueba que no se haya chocado
                    movval=funciones.comp_obst(ni,nc,nd,labyrinth)
                    if movval==True:#de no chocarse, se da oficialmente el paso
                        izq.append(ni)
                        cen.append(nc)
                        der.append(nd)
                        movs[-1]=0
                else:
                    movval=False#si se sale del laberinto, el movimiento sigue siendo invalido
            if umov<1 and movval==False and ultimo!=4:#si el ultimo movimiento no puede hacerse, se procede con el siguiente de forma equivalente. Ahora se prueba el movimiento de ir hacia abajo
                ni,nc,nd=funciones.mov1(izq,cen,der)
                ival=funciones.comp_dentro_lab(ni,filas,cols)
                ider=funciones.comp_dentro_lab(nd,filas,cols)
                if ider==ival and ival==True:
                    movval=funciones.comp_obst(ni,nc,nd,labyrinth)
                    if movval==True:
                        izq.append(ni)
                        cen.append(nc)
                        der.append(nd)
                        movs[-1]=1
                else:
                    movval=False
            if umov<2 and movval==False and ultimo!=2:#si el ultimo movimiento no puede hacerse, se procede con el siguiente de forma equivalente. Ahora se prueba el movimiento de girar
                ni,nc,nd=funciones.mov2(izq,cen,der)
                ival=funciones.comp_dentro_lab(ni,filas,cols)
                ider=funciones.comp_dentro_lab(nd,filas,cols)
                if ider==ival and ival==True:
                    movval=funciones.comp_obst_giro(nc,labyrinth)#la funcion de comprobar si se puede hacer el giro es diferente a la de comprobar si se puede hacer el resto de movimientos, tal y como se aprecia en el archivo funciones.py
                    if movval==True:
                        izq.append(ni)
                        cen.append(nc)
                        der.append(nd)
                        movs[-1]=2
                else:
                    movval=False
            if umov<3 and movval==False and ultimo!=0:#si el ultimo movimiento no puede hacerse, se procede con el siguiente de forma equivalente. Ahora se prueba el movimiento de ir hacia la izquierda
                ni,nc,nd=funciones.mov3(izq,cen,der)
                ival=funciones.comp_dentro_lab(ni,filas,cols)
                ider=funciones.comp_dentro_lab(nd,filas,cols)
                if ider==ival and ival==True:
                    movval=funciones.comp_obst(ni,nc,nd,labyrinth)
                    if movval==True:
                        izq.append(ni)
                        cen.append(nc)
                        der.append(nd)
                        movs[-1]=3
                else:
                    movval=False

            if umov<4 and movval==False and ultimo!=1:#si el ultimo movimiento no puede hacerse, se procede con el siguiente de forma equivalente. Ahora se prueba el movimiento de ir hacia abajo
        
                ni,nc,nd=funciones.mov4(izq,cen,der)
                ival=funciones.comp_dentro_lab(ni,filas,cols)
                ider=funciones.comp_dentro_lab(nd,filas,cols)
                if ider==ival and ival==True:
                    movval=funciones.comp_obst(ni,nc,nd,labyrinth)
                    if movval==True:
                        izq.append(ni)
                        cen.append(nc)
                        der.append(nd)
                        movs[-1]=4
                else:
                    movval=False    
            if movval==True and movs[-1]!=-1:#una vez se ha tenido la oportunidad de hacer todos los movimientos, se comprueba si se ha hecho alguno de ellos
                comp=funciones.compr_compl(der,filas,cols)#de haberse hecho uno de ellos, se comprueba si ha permitido llegar al final 
            else:#de no haber permitido, se hace la comprobacion de que el objeto no esta atrapado en la posicion incial ( por obstaculos o porque ya ha probado todos los movimientos posibles y no puede avanzar)
                if len(movs)==1:
                    imp=True#de estar atrapado, se considera el laberinto como imposible
                else:
                    regreso=True#de no estar atrapado, se considera que el camnino que se esta siguiendo es erroneo y se vuelve atras un paso a comprobar otras opciones
                
                    
        


        if imp==True:#si el while se rompio debido a que el laberinto era imposible, la salida sera 1
            sal=-1
        else:#en caso contrario, la salida sera el numero de movimientos dados
            sal=len(movs)
    return sal
    

if __name__ == "__main__":#ejemplo de uso del codigo
    try:#para asegurar que la entrada es correcta
        lybrinth = [[".",".",".",".",".",".",".",".","."],["#",".",".",".","#",".",".",".","."],[".",".",".",".","#",".",".",".","."],[".","#",".",".",".",".",".","#","."],[".","#",".",".",".",".",".","#","."]]
        a=main(lybrinth)
        print("Laberinto procesado correctamente.")
        print(a)
    except TypeError as e:#en caso de que el laberinto no este bien creado, salta un error
        print("Error:", e)
    