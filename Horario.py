from random import *

materias=['Matemáticas', 'Lengua','Ciencias','Geografía e Historia']
# Estructura de profesores: abrev, materia, grupo, aula, nºhoras
profMatGru=[
    ['Pep1','lcl','1ºESOA','A1',4],
    ['Lol1','mat','1ºESOA','A1',4],
    ['AnV1','ing','1ºESOA','A1',4],
    ['Dio1','byg','1ºESOA','A1',3],
    ['Ant1','geh','1ºESOA','A1',3],
    ['Jor1','edf','1ºESOA','Gy',3],
    ['Ana1','epv','1ºESOA','TD',2],
    ['Lol1','tut','1ºESOA','A1',1],
    ['Gui1','mus','1ºESOA','A1',2],
    ['San1','cyr','1ºESOA','H4',2],
    ['Raf1','fra','1ºESOA','A1',2]
]

# Estructura que almacena los horarios. Las filas son las horas, las columnas los días.
horarios=[]
for fil in range(6):
    horarios.append([])
    for col in range(5):
        horarios[fil].append([])

# Muestra el horario por la pantalla.
def muestraHor():
    for fil in range(6):
      print()
      for col in range(5):
        if horarios[fil][col] != []:
            print(horarios[fil][col],end="")
        else:
            print('[                   ]',end="")
    print()

# Coloca al profesor con materia pasado por parámetros en el horario.
def coloca(prof):
    for n in range(prof[4]):
        hor=randint(0,5)
        dia=randint(0,4)
        while horarios[hor][dia] != []:
            hor=randint(0,5)
            dia=randint(0,4)
        horarios[hor][dia]=[prof[0],prof[1],prof[3]]

# Genera un horario.
def genHor():
    for prof in profMatGru:
        coloca(prof)

genHor()
muestraHor()

