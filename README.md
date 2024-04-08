# PRUEBAS UNITARIAS

  como parte de mi proyecto de fundamentos en ingenieria en software vengo a mostrar la importancia y su implementacion de las pruebas unitarias del software en sus respectivos proyectos sin embargo vamos a retroceder un poco y vamos a  ver en un poco en general  acerca de las pruebas de software y su evaluación del mismo.

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
 paso 1:
 
  para empezar vamos a crear otra carpeta en la cual crearemos un archivo el cual sera nuestro main(importante poner el .py que es la terminacion de python)

 paso 2:
 
  vamos a crear otro documento porque lo querremos tomar como paquete por lo que es importante llamarlo :
__init__.py
 
paso 3: 

en nuestro documento main vamos  hacer dos funciones muy sencillas para observar como funcionan las pruebas
( copiar las funciones que aparecen abajo y pegarlas en el main)

paso 4:

 vamos a crear una subcarpeta  con el nombre test( ya que en esta carpeta haremos las pruebas) y  vamos a repetir el paso 2, es decir vamos a crear un documento que se llame  test_main y  le agregamos el mismo documento para que se convierta en un paquete.(foto)

paso 5: 

vamos a  importar las 2 funciones que hicimos anteriormente en el main para probarlas y ver como funcionan
empezaremos con la funcion sum tal como se muestra en la imagen, utilizaremos la palabra clave assert para indicar 
que un valor debe ser igual a otro, aqui es donde vamos a comprobar si el resultado de una funcion es el esperado.

paso 6: 

ahora  abrimos la consola/terminal y ejecutamos pytest (foto) una vez ejecutado el pytest lo que hace es  detectar todos los archivos de prueba y te dice  las pruebas que pasaron y las que no.  ( si agregas  -v al comando pytest te da un resultado mas detallado de todas las pruebas)

## 3. utilizar las funciones odd y even ( par e impar)
paso 1: 

definimos las funciones de odd y even, para el caso del odd sabemos que cualquier numero  dividido entre 2 y que su residuo sea 1 es un numero impar ( tal como esta en la imagen)

paso 2:

 el even es mas sencillos se puede hacer de dos formas  la primera es usando el mismo metodo que el odd simplemente en vez de poner el 1 en el residuo ponemos 0 ya que  cualquier numero dividido entre 2 nos tiene que dar de residuo 0 o la otra forma es   utilizando el odd y negarlo, por lo tanto  si odd == false  entonces es par ( tal como se muestra en la imagen)


paso 3:

  vamos al test main  para importar las dos funciones donde importamos anteriormente las  de suma y greather than.
  seguidamente definimos la variable de   preferencia test_is_odd_even y con la ayuda del assert le damos los valores que   queremos probar  tanto con el odd como con el even.( foto)


 ##   4. utilizar las funciones sum y is_greather_than con parametros
paso 1:

 el siguiente paso es utilizar una nueva   opcion que nos ofrece pytest por lo que primero vamos a importar pytest y luego  vamos a  volver a  definir la funcion test sum pero esta vez  con params    justo como lo muestro en la foto de abajo ( foto)


  
paso 2:  

el imputx y el imputy  indica los 2 valores que espera ( los numeros que se van a sumar) y el parametro expected  es el valor que se espera recibir sin embargo necesita  unos parametros para que pueda probar  mediante pytest tenemos un decorador @pytest.mark.parametrize el cual le insertaremos una serie de parametros en una lista y dentro pondremos duplas con valores( los valores puedes poner los que tu quieras).abajo del parametrize tenemos que  volver  a escribir dentro comillas los imputx y el expected tal que asi :  " input_x, input_y, expected", para que quede mas claro adjunto la foto para que se entienda mejor el orden de cada parametro. ( foto) nuevamente volver a ejecutar pytest -v para ver si las pruebas pasaron correctamente.


  ##  5. simular una base de datos para comprobar credenciales
  paso 1:

  primero tenemos que regresar al main para escribir la nueva función. adjunto la imagen ( foto)
    


 esto nos va a regresar verdadero siempre y cuando nuestro username  y nuestra password sean las mismas que hayamos ingresado anteriormente, en caso de que no se cumpla uno de los dos  nos regresaria a falso.


 paso 2:

 ahora regresamos al test main para hacer la prueba importando en la parte superior (donde  se importaron  el sum y el greather than) para que pueda hacerse la prueba.( foto)

 paso 3: 
 
  definimos el  test login (), en la siguiente linea hacemos una variable en este caso login passed que sea igual a login  y le pasamos los valores corectos es decir el nombre de usuario y la contraseña tal como aparece en la foto.( foto)



paso 4: 

crearemos otro test pero esta vez para cuando  vaya a ser falso es decir  lo unico que cambiaremos es el nombre de la variable ( de passed a  fails),  el nombre de usuario o la contraseña y el assert le agregaremos el not ¿porque? porque lo que estamos buscando es que la prueba nos retorne a falso y eso lo podemos hacer con el uso del not  (foto)


## 6. simular la conexion a una base de datos y el retorno  de una lista
 
paso 1:

adentro de la carpeta src vamos a crear  otra carpeta llamada models, despues vamos a crear el documento __init__.py, despues otro documento  que nos hara la funcion de main pero le llamaremos languageMode.py como si tuvieramos un modelo para poder leer lenguajes de programacion ahora dentro de test vamos a crear otra carpeta  llamada models y vamos a repetir el mismo paso anterior solo que el nombre del documento languageMode.py ahora lo llamaremos test_languageModel.


paso 2:

 tenemos una clase  llamada languageModel  y un metodo de clase llamada get_language que lo unico que hace es retornar una lista de  lenguajes de programacion.  simulamos aqui que nos hemos conectado a una base de datos y esto lo estamos trayendo mediante una consulta. ( foto) 

paso 3:

dentro de test_languageModel vamos a comprobar priemro que  esa lista que  se nos retorne sea distinto  de NONE( el none equivale a la ausencia de un valor)  entonces primero importamos el  languagemodel como lo hemos echo anteriormente despues creamos una funcion llamada test_get_languages_not_none(): (para comprobar que lo que me retorne no sea None)
 seguidamente creamos una variable llamada languange = languageModel.get_languages()  y luego haremos un assert para que language sea diferente de none ( foto)


 paso 4:

 ahora vamos  hacer la misma prueba pero comprobando si tiene elementos por lo tanto  ahora va a ser :def  test_get_languages_has_elements():  y el assert  ahora va a ser :  assert len(languages) >  0  que significa que la longitud de estos lenguajes sea mayor a 0 (foto).


 paso 5:

 copiamos la misma funcion y ahora vamos a comprobar la longitud de cada uno de esos elementos  por lo tanto cambiamos el nombre de la  funcion a : def test_get_languages_check-elements_length(): despues crearemos un for  para cada lenguaje en esta lista de lenguajes vamos hacer un assert de que la longitud de cada uno de estos lenguajes sea mayor a 0 (foto)

  paso 6: 
  
  abrir la terminar y ejecutar pytest -v  vamos  a ver que todos han pasado corectamente ya que primero la lista no es NONE despues existen elementos  y tambien cada elemento su longitud es mayor a 0. esto fallaria si por ejemplo uno de los elementos lo quitamos y dejamos una cadena de caracteres vacia. vemos que la 3 prueba fallo porque la longitud de un elemento en particular  ( en este caso   el elemento que borramos) fue 0 por lo tanto fallo. 