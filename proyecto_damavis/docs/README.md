## Descripción
Este proyecto resuelve el problema de los laberintos propuesto por Damavis.


## Guía de Uso
1. Ejecuta el programa principal usando python main.py [laberinto], donde [laberinto] es una matriz de laberinto en formato JSON.

## Documentación de Funciones
### main(laberinto)
Esta función toma una matriz de laberinto y devuelve, si es posible, el número de pasos para resolverlo. Se podría haber mejorado creando una segunda función que tome como entrada la combinación de pasos que propone este programa y busque si es psobible
otra combinación de pasos que lleve a la misma solución de forma más rápida partiendo de la ya creada. Además, no se ha puesto ningún mecanismo que evite que puedan ocurrir bucles
de forma que el objeto se mueva a la derecha, suba, se mueva a la izquierda, baje, y vuelva a moverse a la izquierda en bucle.

## Ejemplos de Uso
laberinto = [[".",".","."],["#","#","."],[".",".","."]]
resultado = main(laberinto)
print("Resultado:", resultado)

## Contacto

Si tienes alguna duda, puedes contactar conmigo en mi correo electrónico: jacobocanegra@gmail.com