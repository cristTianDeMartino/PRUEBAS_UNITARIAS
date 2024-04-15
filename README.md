  



# PRUEBAS UNITARIAS

  como parte de mi proyecto de fundamentos en ingenieria en software vengo a mostrar la importancia y su implementacion de las pruebas unitarias del software en sus respectivos proyectos sin embargo vamos a retroceder un poco y vamos a  ver en un poco en general  acerca de las pruebas de software y su evaluación del mismo.

  ## contenido 
- [introducción](#evaluacion-del-software)
- [requisitos previos](#requisitos_previos)
- [ejemplo de pruebas unitarias por separado](#ejemplos-de-pruebas-unitarias)
- [aplicacion de pruebas a un codigo](#video)
- [observaciones](#puntos-importantes-a-tener-en-cuenta)
- [conclusión](#conclusión)





  # EVALUACION DEL SOFTWARE

   a la hora de  evaluar un software existen dos tipos:

   # verificación:  
         
   El proceso implica verificar si los productos de una etapa específica del desarrollo de software cumplen con los requisitos establecidos en la fase anterior. El objetivo es determinar si estamos creando el producto de manera correcta, lo que incluye revisar el programa para asegurarnos de que esté en conformidad con sus especificaciones. basicamente es  ver si los productos de la etapa cumplen con los requisitos establecidos o no.
   
   # validación: 
   
   Proceso de evaluación del SW al final del proceso de desarrollo para asegurar el cumplimiento de necesidades del cliente. ¿Estamos creando el producto correcto?. Revisión del programa conforme a las expectativas del usuario.basicamente al final del proceso se hace una evaluacion para ver si el programa corre perfectamente o tiene errores.

  # los objetivos de V&V:
   son básicamente descubrir los defectos del sistema, y determinar cuando un sistema es útil o no en una situación. Existen  dos tecnicas para la evaluación del  SW.

  1) las tecnicas estaticas:
  consisten en revisiones de requerimientos, diseños y lista de programas.

  2) las tecnicas dinamicas(pruebas):
     se estudia  como se comporta el sistema a la hora de ingresar datos:
     1) pruebas unitarias.
     2) pruebas de integración.
     3) pruebas de sistema.
     4) pruebas de aceptación.

      
  todas estas pruebas son importantes a la hora de hacer un proyecto de software ya que fuero creadas justamente para la necesidad de garantizar la calidad y fiabilidad de los programas informáticos, sin embargo nosotros  haremos enfasis y hablaremos mas en especifico sobre las pruebas unitarias ya que son una parte muy importante a la hora de probar el software.

  # PLAN DE PRUEBAS
      https://ibb.co/1GsyLrR


 # REQUISITOS PREVIOS
   
 ahora ya sabemos mas acerca de las pruebas y las pruebas unitarias en general pero para que se entienda de mejor manera voy hacer una prueba muy sencilla utilizando python  y la libreria de pytest.
 
  sin embargo para que la prueba sea mas fluida y entendible es recomendable que el que vaya a hacer la prueba tenga los siguientes conocimientos bien marcados.
  1)  instalar visual studio code.
  2)  saber  un lenguaje de programacion ( en este caso  python ya que sera el lenguaje que utilizaremos para hacer la prueba).   
  3)  crear una carpeta y arrastrarla al visual studio code(  yo la llamare src).
  4)  crear y activar  un entorno virtual (Virtualenv).
  5) instalar la libreria pytest con el comando : pip install pytest
  6) comprobar que se haya instalado correctamente la libreria con el comando: pip list


#  EJEMPLOS DE PRUEBAS UNITARIAS


  ##  1. funcion sum y is_greather_than
 **paso 1:**
 
  para empezar vamos a crear otra carpeta en la cual crearemos un archivo el cual sera nuestro main(importante poner el .py que es la terminacion de python)

 **paso 2:**
 
  vamos a crear otro documento porque lo querremos tomar como paquete por lo que es importante llamarlo :
__init__.py
 
**paso 3:** 

en nuestro documento main vamos  hacer dos funciones muy sencillas  para observar como funcionan las pruebas en este caso vamos hacer una suma y comparar dos numeros para encontrar el mayor( copiar las funciones que aparecen abajo y pegarlas en el main)

 ```py
def sum(x,  y):
    return x + y 


def is_greater_than(number_1, number_2):
    return number_1 > number_2 
```


**paso 4:**

 vamos a crear una subcarpeta  con el nombre test( ya que en esta carpeta haremos las pruebas) y  vamos a repetir el paso 2, es decir vamos a crear un documento que se llame  test_main y  le agregamos el mismo documento para que se convierta en un paquete.(foto)

**paso 5:** 

vamos a  importar las 2 funciones que hicimos anteriormente en el main para probarlas y ver como funcionan
empezaremos con la funcion sum tal como se muestra en la imagen, utilizaremos la palabra clave assert para indicar 
que un valor debe ser igual a otro, aqui es donde vamos a comprobar si el resultado de una funcion es el esperado.
 ( importacion de las funciones)
```py
 
from src.main import sum, is_greater_than
```
```py
def test_sum():
    assert sum(2, 5) == 7

def test_is_greater_than():
    assert is_greater_than(10, 2)
    assert is_greater_than(-2, -6)
    assert is_greater_than(10, 22) == False    
 
```
**paso 6:**
ahora  abrimos la consola/terminal y ejecutamos pytest (foto) una vez ejecutado el pytest lo que hace es  detectar todos los archivos de prueba y te dice  las pruebas que pasaron y las que no.  ( si agregas  -v al comando pytest te da un resultado mas detallado de todas las pruebas)

## 3. utilizar las funciones odd y even ( par e impar)
**paso 1:**

definimos las funciones de odd y even en el main. para el caso del odd sabemos que cualquier numero  dividido entre 2 y que su residuo sea 1 es un numero impar 
```py
def is_odd(num):
    # returns true if number is odd
    return num % 2 == 1
```

**paso 2:**

 el even es mas sencillos se puede hacer de dos formas  la primera es usando el mismo metodo que el odd simplemente en vez de poner el 1 en el residuo ponemos 0 ya que  cualquier numero dividido entre 2 nos tiene que dar de residuo 0 o la otra forma es   utilizando el odd y negarlo, por lo tanto  si odd == false  entonces es par  tal como se muestra  a continuación.
 ```py
 def is_even(num):
    # returns true if number is even
    return is_odd(num) == False
______________________________________
def is_even(num):
  return num % 2== 0

```

**paso 3:**

  vamos al test main  para importar las dos funciones donde importamos anteriormente las  de suma y greather than.
  seguidamente definimos la variable de   preferencia test_is_odd_even y con la ayuda del assert le damos los valores que   queremos probar  tanto con el odd como con el even.
  ```py
  from src.main import sum, is_greater_than,  is_odd, is_even

  def test_is_odd_even():
    assert is_odd(1)
    assert is_odd(3)
    assert is_even(7) == False
    assert is_even(4)

```
 ##   4. utilizar las funciones sum y is_greather_than con parametros
**paso 1:**

 el siguiente paso es utilizar una nueva   opcion que nos ofrece pytest por lo que primero vamos a importar pytest y luego  vamos a  volver a  definir la funcion test sum pero esta vez  con params, todo esto en el documento de test_main justo como lo muestro en la parte de abajo
 ```py
 import pytest
def test_sum_params(input_x, input_y, expected):   
   
```
  
**paso 2:**  

el imputx y el imputy  indica los 2 valores que espera ( los numeros que se van a sumar) y el parametro expected  es el valor que se espera recibir sin embargo necesita  unos parametros para que pueda probar  mediante pytest tenemos un decorador @pytest.mark.parametrize el cual le insertaremos una serie de parametros en una lista y dentro pondremos duplas con valores( los valores puedes poner los que tu quieras).abajo del parametrize tenemos que  volver  a escribir dentro comillas los imputx y el expected tal que asi :  " input_x, input_y, expected", para que quede mas claro adjunto la foto para que se entienda mejor el orden de cada parametro.
```py
 import pytest
 @pytest.mark.parametrize(
     "input_x, input_y, expected",
     [
         (5, 1, 6),
         (6, sum(4, 2), 12),
         (sum(19, 1), 15, 35),
         (-7, 10, sum(-7, 10))
     ]
 )

def test_sum_params(input_x, input_y, expected):   
    assert sum(input_x, input_y) == expected
```
nuevamente volver a ejecutar pytest -v para ver si las pruebas pasaron correctamente.


  ##  5. simular una base de datos para comprobar credenciales

  **paso 1:**

  primero tenemos que regresar al main para escribir la nueva función. 
```py
  def  login(username, password):
    if  ((username == "alumnouady") and  (password == "uady1234")):
         return True
    else:
        return False
  ```  


 esto nos va a regresar verdadero siempre y cuando nuestro username  y nuestra password sean las mismas que hayamos ingresado anteriormente, en caso de que no se cumpla uno de los dos  nos regresaria a falso.


 **paso 2:**

 ahora regresamos al test main para hacer la prueba importando en la parte superior (donde  se importaron  el sum y el greather than) para que pueda hacerse la prueba.
 ```py
 from src.main import sum, is_greater_than, __login__, is_odd, is_even
```

 **paso 3:** 
 
  definimos el  test login (), en la siguiente linea hacemos una variable en este caso login passed que sea igual a login  y le pasamos los valores corectos es decir el nombre de usuario y la contraseña tal como aparece en la foto.

    ```py
   def test_login_pass():
    login_passes=login("alumnouady","uady1234")
    assert   login_passes 
    ```


**paso 4:** 

crearemos otro test pero esta vez para cuando  vaya a ser falso es decir  lo unico que cambiaremos es el nombre de la variable ( de passed a  fails),  el nombre de usuario o la contraseña y el assert le agregaremos el not ¿porque? porque lo que estamos buscando es que la prueba nos retorne a falso y eso lo podemos hacer con el uso del not  

    ```py
def test_login_fail():
    login_fails=login("alumnouadytete","uady12343412")
    assert not login_fails
    ```


## puntos importantes  a tener en cuenta

   1. tener mucho cuidado a la hora de hacer los paquetes,asegurarse de que esten en su sitio y en su respectiva carpeta y que tenga todos los signos incluyendo el .py
  2.  verificar los lugares a la hora de copiar el codigo, al ser python el lugar en el que se encuentra cada variable importa muchisimo
  





 ##  CONCLUSIÓN 

 en  resumen La evaluación del software se divide en verificación (asegurar que se desarrolle según especificaciones) y validación (comprobar si cumple las necesidades del cliente). Las técnicas incluyen estáticas (revisiones) y dinámicas (pruebas unitarias, de integración, de sistema y de aceptación).  Las pruebas unitarias son fundamentales para garantizar la calidad del software, ya que se enfocan en probar componentes individuales para asegurar su correcto funcionamiento. Esto contribuye a la fiabilidad del producto final y lo convierte en un proyecto mas solido y fiable a la hora de presentarlo al cliente.




  ##  REFERENCIAS 
   https://www.youtube.com/watch?v=JZ0TMkwMgp8&ab_channel=UskoKruM2010
   https://docs.pytest.org/en/latest/
