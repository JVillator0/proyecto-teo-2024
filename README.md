
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
| **header_file**    | `r'<[a-zA-Z0-9_]+>'`        | Representa un archivo de encabezado entre `<` y `>` como `<iostream>` o `<string>` o `algo.h`. |
| **identifier**         | `r"[a-zA-Z_][a-zA-Z0-9_]*"`         | Detecta identificadores válidos (caracteres alfanuméricos o guiones).  |
| **número**             | `r"\d+(\.\d+)?"`                 | Detecta números enteros y flotantes.                                   |
| **preprocessor**       | `r"#include"`                       | Detecta directivas de preprocesador como `#include`.                   |
| **coma**               | `r','`                              | Identifica comas usadas como separadores en expresiones o argumentos.  |
| **comentario**         | `r"//.*"`                           | Identifica comentarios de una línea que empiezan con `//`.             |
| **comentario_bloque**  | `r"/\*[\s\S]*?\*/"`             | Identifica comentarios de bloque entre `/*` y `*/`.                    |
| **fin_de_instrucción** | `r';'`                              | Marca el final de una instrucción (normalmente un punto y coma `;`).   |
| **paréntesis_de_apertura** | `r'\('`                        | Identifica el paréntesis de apertura `(`.                              |
| **paréntesis_de_cierre**   | `r'\)'`                        | Identifica el paréntesis de cierre `)`.                                |
| **llave_de_apertura**      | `r'\{'`                        | Identifica la llave de apertura `{`, que inicia un bloque de código.   |
| **llave_de_cierre**        | `r'\}'`                        | Identifica la llave de cierre `}`, que termina un bloque de código.     |
| **punto**              | `r'\.'`                            | Identifica el punto `.` usado en el acceso a propiedades o métodos.    |
| **asignación**         | `r'='`                              | Identifica el operador de asignación `=`.                              |
| **resolución_de_ámbito** | `r'::'`                           | Identifica el operador de resolución de ámbito `::` en C++.            |
| **cadena**             | `r'"([^"\\]*(\\.[^"\\]*)*)"'` | Detecta cadenas de texto delimitadas por comillas dobles.              |
| **igual_a**            | `r'=='`                             | Detecta el operador de igualdad `==`.                                  |
| **diferente_de**       | `r'!='`                             | Detecta el operador de desigualdad `!=`.                               |
| **desplazamiento_izq** | `r'<<'`                             | Detecta el operador de desplazamiento a la izquierda `<<`.             |
| **desplazamiento_der** | `r'>>'`                             | Detecta el operador de desplazamiento a la derecha `>>`.               |

### Operadores

El analizador reconoce diversos operadores, incluidos:

| **Token**        | **Expresión regular/regla** | **Explicación**                                                 |
|------------------|-----------------------------|-----------------------------------------------------------------|
| **mayor**        | `r'>'`                      | Operador que compara si el valor de la izquierda es mayor.       |
| **mayor_igual**  | `r'>='`                     | Operador que compara si el valor de la izquierda es mayor o igual.|
| **menor**        | `r'<'`                      | Operador que compara si el valor de la izquierda es menor.       |
| **menor_igual**  | `r'<='`                     | Operador que compara si el valor de la izquierda es menor o igual.|
| **igual_que**    | `r'=='`                     | Operador que compara si dos valores son iguales.                 |
| **distinto**     | `r'!='`                     | Operador que compara si dos valores son diferentes.              |
| **mas**          | `r'\+'`                     | Operador de suma.                                               |
| **menos**        | `r'-'`                      | Operador de resta.                                              |
| **multiplicacion**| `r'\*'`                    | Operador de multiplicación.                                     |
| **division**     | `r'/'`                      | Operador de división.                                           |
| **modulo**       | `r'%'`                      | Operador que obtiene el resto de una división.                  |
| **and_operator** | `r'&&'`                     | Operador lógico AND.                                            |
| **or_operator**  | `r'\|\|'`                   | Operador lógico OR.                                             |
| **negacion**     | `r'!'`                      | Operador lógico de negación.                                    |
| **scope_resolution** | `r'::'`                 | Operador de resolución de ámbito en C++.                        |
| **left_shift**   | `r'<<'`                     | Operador de desplazamiento a la izquierda.                      |
| **right_shift**  | `r'>>'`                     | Operador de desplazamiento a la derecha.                        |
| **!**            | `r'!'`                      | Operador de negación lógica.                                    |

### Información Adicional

Para probar el analizador, se incluyen archivos de prueba llamados `source1.cpp`, `source2.cpp`, `source3.cpp`, `source4.cpp` y `source5.cpp`. Al ejecutar el script `main.py`, el programa te pedirá seleccionar un archivo fuente, procesará el archivo y mostrará la tabla de símbolos y la lista de tokens resultante en la consola.

### Como ejecutar el programa

Para ejecutar el programa, simplemente ejecuta el script `main.py` en tu entorno de Python 3.9.13. Asegúrate de tener los archivos de prueba `source1.cpp`, `source2.cpp`, `source3.cpp`, `source4.cpp` y `source5.cpp` en el mismo directorio que el script principal.

```bash
python main.py
```