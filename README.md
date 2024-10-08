
# Analizador Lexicográfico en Python para C++

## Descripción del Proyecto

Este proyecto es un analizador lexicográfico desarrollado en Python (versión 3.9.13) para procesar código C++. El analizador identifica tokens y palabras reservadas, clasificando elementos como operadores, delimitadores, palabras clave e identificadores. Está diseñado específicamente para extraer los componentes léxicos de un programa en C++.

El proyecto evita el uso de bibliotecas externas como `ply`, basándose en expresiones regulares para la detección de tokens.

### Conceptos Clave

- **Token**: Un par en la forma de clave-valor, que consiste en el nombre del token y su valor de atributo respectivo, si es aplicable.
- **Lexema**: Una secuencia de caracteres en el programa fuente que coincide con el patrón definido para un token. El analizador léxico identifica esta secuencia como una instancia de un token.
- **Expresión Regular**: Una secuencia de caracteres que define un patrón de búsqueda según ciertas reglas predefinidas. Este es el principal método utilizado para tokenizar la entrada.

### Funcionalidad

El analizador léxico ha sido adaptado para leer código C++ en su versión más reciente. Procesa archivos de código fuente, extrayendo símbolos como palabras clave, operadores e identificadores, y muestra una tabla de símbolos detallada junto con una lista de tokens.

### Palabras Reservadas

Las siguientes palabras reservadas han sido definidas para el analizador léxico, basándose en los elementos clave del lenguaje C++:

| Palabra Reservada | Función                                                                         |
|-------------------|---------------------------------------------------------------------------------|
| **#include**       | Directiva de preprocesador para incluir archivos de encabezado.                 |
| **if**            | Permite evaluar una condición y ejecutar un bloque de código si es verdadera.    |
| **else**          | Se ejecuta cuando la condición del bloque `if` es falsa.                        |
| **class**         | Define una clase que puede contener propiedades y métodos.                      |
| **return**        | Devuelve un valor específico de una función al lugar donde fue llamada.          |
| **const**         | Declara constantes que no pueden cambiar después de ser asignadas.              |
| **using**         | Comúnmente utilizado para la gestión de espacios de nombres o recursos.         |
| **int**           | Define una variable de tipo entero.                                             |
| **double**        | Define una variable de tipo punto flotante de doble precisión.                  |
| **string**        | Define una variable que almacena una secuencia de caracteres (texto).           |
| **bool**          | Define una variable booleana con valores `true` o `false`.                      |
| **for**           | Repite un bloque de código un número específico de veces.                       |
| **cout**          | Para imprimir valores en la consola, parte de la biblioteca estándar.           |
| **cin**           | Para capturar valores desde la consola, parte de la biblioteca estándar.        |
| **endl**          | Salto de línea para la consola, parte de la biblioteca estándar.                |
| **void**          | Tipo de retorno vacío de una función o método.                                  |
| **switch**        | Evalúa una expresión y ejecuta el código basado en múltiples casos.             |
| **case**          | Un caso en una instrucción `switch`.                                            |
| **break**         | Interrumpe el flujo en una estructura como `switch` o bucle.                    |
| **continue**      | Salta a la siguiente iteración de un bucle.                                     |
| **public**        | Modificador de acceso de una clase o estructura.                                |
| **private**       | Modificador de acceso de una clase o estructura.                                |
| **protected**     | Modificador de acceso de una clase o estructura.                                |
| **static**        | Indica que una variable o método pertenece a la clase y no a las instancias.    |
| **new**           | Reserva memoria para una nueva instancia de un objeto o tipo.                   |
| **do**            | Ejecuta un bloque de código en un bucle al menos una vez antes de verificar la condición.|

### Definiciones de Tokens

Se han definido los siguientes tokens con sus respectivas expresiones regulares para este analizador léxico:

| Token                 | Expresión Regular                    | Descripción                                                           |
|-----------------------|--------------------------------------|-----------------------------------------------------------------------|
| **header_file**    | `r'<[a-zA-Z0-9_]+>'`        | Representa un archivo de encabezado entre `<` y `>` como `<iostream>` o `<string>`. |
| **identifier**         | `r"[a-zA-Z_][a-zA-Z0-9_]*"`         | Detecta identificadores válidos (caracteres alfanuméricos o guiones).  |
| **number**             | `r"\d+(\.\d+)?"`                 | Detecta números enteros y flotantes.                                   |
| **preprocessor**       | `r"#include"`                       | Detecta directivas de preprocesador como `#include`.                   |
| **comma**              | `r','`                              | Identifica comas usadas como separadores en expresiones o argumentos.  |
| **comment**            | `r"//.*"`                           | Identifica comentarios de una línea que empiezan con `//`.             |
| **block_comment**      | `r"/\*[\s\S]*?\*/"`             | Identifica comentarios de bloque entre `/*` y `*/`.                    |
| **end_of_instruction** | `r';'`                              | Marca el final de una instrucción (normalmente un punto y coma `;`).   |
| **open_parenthesis**   | `r'\('`                             | Identifica el paréntesis de apertura `(`.                              |
| **close_parenthesis**  | `r'\)'`                             | Identifica el paréntesis de cierre `)`.                                |
| **open_brace**         | `r'\{'`                             | Identifica la llave de apertura `{`, que inicia un bloque de código.   |
| **close_brace**        | `r'\}'`                             | Identifica la llave de cierre `}`, que termina un bloque de código.     |
| **dot**                | `r'\.'`                             | Identifica el punto `.` usado en el acceso a propiedades o métodos.    |
| **assignment**         | `r'='`                              | Identifica el operador de asignación `=`.                              |
| **scope_resolution**   | `r'::'`                             | Identifica el operador de resolución de ámbito `::` en C++.            |
| **string**             | `r'"([^"\\]*(\\.[^"\\]*)*)"'` | Detecta cadenas de texto delimitadas por comillas dobles.              |
| **equal_to**           | `r'=='`                             | Detecta el operador de igualdad `==`.                                  |
| **not_equal**          | `r'!='`                             | Detecta el operador de desigualdad `!=`.                               |
| **left_shift**         | `r'<<'`                             | Detecta el operador de desplazamiento a la izquierda `<<`.             |
| **right_shift**        | `r'>>'`                             | Detecta el operador de desplazamiento a la derecha `>>`.               |
| **increment**          | `r'\+\+'`                           | Detecta el operador de incremento `++`.                                |
| **decrement**          | `r'--'`                             | Detecta el operador de decremento `--`.                                |
| **plus_equal**         | `r'\+='`                            | Detecta el operador de suma y asignación `+=`.                         |
| **minus_equal**        | `r'-='`                             | Detecta el operador de resta y asignación `-=`.                        |
| **times_equal**        | `r'\*='`                            | Detecta el operador de multiplicación y asignación `*=`.               |
| **divide_equal**       | `r'/='`                             | Detecta el operador de división y asignación `/=`.                     |
| **modulus**            | `r'%'`                              | Operador que obtiene el resto de una división.                         |
| **and_operator**       | `r'&&'`                             | Operador lógico AND.                                                   |
| **or_operator**        | `r'\|\|'`                           | Operador lógico OR.                                                    |
| **negation**           | `r'!'`                              | Operador de negación lógica.                                           |

### Operadores

El analizador reconoce los siguientes operadores utilizados en C++:

| **Token**            | **Expresión regular**                | **Descripción**                                                   |
|----------------------|--------------------------------------|-------------------------------------------------------------------|
| **modulus**          | `%`                                  | Operador de módulo (resto de una división).                        |
| **equal_to**         | `==`                                 | Operador que compara si dos valores son iguales.                   |
| **not_equal**        | `!=`                                 | Operador que compara si dos valores son distintos.                 |
| **right_shift**      | `>>`                                 | Operador de desplazamiento de bits a la derecha.                   |
| **left_shift**       | `<<`                                 | Operador de desplazamiento de bits a la izquierda.                 |
| **assignment**       | `=`                                  | Operador de asignación.                                            |
| **plus**             | `+`                                  | Operador de suma.                                                  |
| **minus**            | `-`                                  | Operador de resta.                                                 |
| **multiplication**   | `*`                                  | Operador de multiplicación.                                        |
| **division**         | `/`                                  | Operador de división.                                              |
| **and_operator**     | `&&`                                 | Operador lógico AND.                                               |
| **or_operator**      | `||`                                 | Operador lógico OR.                                                |
| **greater_than**     | `>`                                  | Operador que compara si un valor es mayor que otro.                |
| **less_than**        | `<`                                  | Operador que compara si un valor es menor que otro.                |
| **greater_equal_than** | `>=`                               | Operador que compara si un valor es mayor o igual que otro.        |
| **less_equal_than**  | `<=`                                 | Operador que compara si un valor es menor o igual que otro.        |
| **scope_resolution** | `::`                                 | Operador de resolución de ámbito.                                  |
| **negation**         | `!`                                  | Operador de negación lógica.                                       |
| **increment**        | `++`                                 | Operador de incremento.                                            |
| **decrement**        | `--`                                 | Operador de decremento.                                            |
| **plus_equal**       | `+=`                                 | Operador de suma y asignación.                                     |
| **minus_equal**      | `-=`                                 | Operador de resta y asignación.                                    |
| **times_equal**      | `*=`                                 | Operador de multiplicación y asignación.                           |
| **divide_equal**     | `/=`                                 | Operador de división y asignación.                                 |
| **modulus_equal**    | `%=`                                 | Operador de módulo y asignación.                                   |

### Información Adicional

Para probar el analizador, se incluyen archivos de prueba llamados `source1.cpp`, `source2.cpp`, `source3.cpp`, `source4.cpp` y `source5.cpp`. Al ejecutar el script `main.py`, el programa te pedirá seleccionar un archivo fuente, procesará el archivo y mostrará la tabla de símbolos y la lista de tokens resultante en la consola.

### Como ejecutar el programa

Para ejecutar el programa, simplemente ejecuta el script `main.py` en tu entorno de Python 3.9.13. Asegúrate de tener los archivos de prueba `source1.cpp`, `source2.cpp`, `source3.cpp`, `source4.cpp` y `source5.cpp` en el mismo directorio que el script principal.

```bash
python main.py
```
