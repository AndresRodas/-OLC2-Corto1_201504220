# **[OLC2] CORTO 2** - Generador de C3D

| Carnet         | Nombre                      |
| --------      | --------                    | 
| 201504220     | José Andres Rodas Arrecis   |

### Descripción:
* La aplicacion toma como entrada una expresión en alto nivel y como salida tiene la misma expresión en codigo de tres direcciones.  El Scanner, Parser y traductor se realizaron con ayuda de la herramienta "PLY" de Python.

### Instrucciones de uso:

**1.**    Antes de ejecutar la aplicacion asegurarse de tener instalado **Python3** en el dispositivo.

**2.**    Para crear una nueva entrada dirijase al archivo **"entrada.txt"** y modifiquelo, de tal manera que lo único que quede en el archivo sea una expresion logica y/o aritmética.

**3.**    Para correr correr la aplicacion unicamente situarse en la carpeta raiz y ejecutar el comando **"python gramatica.py"**.

##### Entradas de ejemplo:

| Operador         | Entrada|
| --------      | --------  | 
| SUMA     |  `1 + 2`  |
| RESTA    |  `3 - 4`  |
| MULTIPLICACIÓN     |  `5 * 6`  |
| DIVISIÓN     |  `7 / 8`  |
| IGUAL     | `5 == 5`  |
| DIFERENTE     |  `3 != 4`  |
| NOT     |  `! 5 == 5`|
| AND     | `5==5 && 3 != 3`|
| OR      | `5==5 \|\| 3 != 3`|


##### Salidas de ejemplo:

![](https://i.imgur.com/6I9PIZr.png)

![](https://i.imgur.com/Gpc66N0.png)

![](https://i.imgur.com/kfYQSTJ.png)





