import os
from lexer import lexer
from parser import parser
from symbol_table import SemanticAnalyzer

def main():
    # Mostrar archivos disponibles en la carpeta tests/
    test_folder = "tests"
    if not os.path.exists(test_folder):
        print(f"Error: La carpeta '{test_folder}' no existe.")
        return

    test_files = sorted(f for f in os.listdir(test_folder) if f.endswith(".c"))
    if not test_files:
        print(f"No se encontraron archivos de prueba en la carpeta '{test_folder}'.")
        return

    print("Archivos disponibles para procesar:")
    for index, file_name in enumerate(test_files, start=1):
        print(f"{index}. {file_name}")

    try:
        choice = int(input("\nSeleccione el archivo a procesar (número): ").strip())
        if choice < 1 or choice > len(test_files):
            print("Selección inválida. Por favor, elija un número válido.")
            return
        file_path = os.path.join(test_folder, test_files[choice - 1])
    except ValueError:
        print("Entrada inválida. Por favor, introduzca un número.")
        return

    # Leer el archivo seleccionado
    try:
        with open(file_path, "r") as file:
            code = file.read()
    except FileNotFoundError:
        print(f"Error: No se pudo abrir el archivo '{file_path}'.")
        return

    print(f"\nProcesando el archivo: {file_path}")

    # Etapa 1: Análisis Léxico
    print("\n== Etapa 1: Análisis Léxico ==")
    try:
        lexer.input(code)
        tokens = []

        print("\n== Tokens generados ==")
        for token in lexer:
            print(token)
            tokens.append(token)
    except Exception as e:
        print(f"Error durante el análisis léxico: {e}")
        return

    # Etapa 2: Análisis Sintáctico
    print("\n== Etapa 2: Análisis Sintáctico ==")
    try:
        ast = parser.parse(code, lexer=lexer)
        if ast:
            print("Análisis sintáctico completado con éxito.")
        else:
            print("Error durante el análisis sintáctico: Parsing fallido.")
            return
    except Exception as e:
        print(f"Error durante el análisis sintáctico: {e}")
        return

    # Etapa 3: Análisis Semántico
    print("\n== Etapa 3: Análisis Semántico ==")
    try:
        semantic_analyzer = SemanticAnalyzer()
        semantic_analyzer.analyze(ast)  # Conectamos el AST generado
        semantic_analyzer.print_symbol_table()
        print("Análisis semántico completado con éxito.")
    except Exception as e:
        print(f"Error durante el análisis semántico: {e}")
        return

    print("\nCompilación completada sin errores.")

if __name__ == "__main__":
    main()