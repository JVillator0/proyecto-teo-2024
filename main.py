from lexer.lexer import Lexer
from parser.parser import Parser
from semantic.analyzer import SemanticAnalyzer

def main():
    # Array de archivos de prueba
    test_files = [
        "tests/test1.c",
        "tests/test2.c",
        "tests/test3.c",
        "tests/test4.c",
        "tests/test5.c"
    ]

    # Mostrar opciones al programador
    print("Archivos disponibles para procesar:")
    for index, file_name in enumerate(test_files, start=1):
        print(f"{index}. {file_name}")

    try:
        # Solicitar selección de archivo
        choice = input("\nSeleccione el archivo a procesar (número): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= len(test_files)):
            print("Selección inválida. Por favor, elija un número válido.")
            return

        # Obtener ruta del archivo seleccionado
        file_path = test_files[int(choice) - 1]

        # Leer el archivo de entrada
        with open(file_path, 'r') as file:
            code = file.read()

        # Etapa 1: Análisis léxico
        print("\n== Etapa 1: Análisis Léxico ==")
        try:
            lexer = Lexer()
            tokens = lexer.tokenize(code)
            for token in tokens:
                print(token)
        except ValueError as e:
            print(f"Error durante el análisis léxico: {e}")
            return

        # Etapa 2: Análisis Sintáctico
        print("\n== Etapa 2: Análisis Sintáctico ==")
        try:
            parser = Parser(tokens)
            parser.parse()
        except ValueError as e:
            print(f"Error durante el análisis sintáctico: {e}")
            return

        # Etapa 3: Análisis Semántico
        print("\n== Etapa 3: Análisis Semántico ==")
        try:
            semantic_analyzer = SemanticAnalyzer()

            declared_variables = set()  # Llevar un registro de variables declaradas

            for token_type, token_value in tokens:
                if token_type == "ID":
                    if token_value not in declared_variables:
                        # Declaración de variable
                        semantic_analyzer.analyze_declaration(token_value, "int", 0, 0)
                        declared_variables.add(token_value)
                    else:
                        # Uso de variable
                        semantic_analyzer.analyze_usage(token_value, 0, 0)
                elif token_type in ["PLUS", "MINUS", "TIMES", "DIVIDE"]:
                    # Validar operación
                    semantic_analyzer.analyze_operation("int", "int", token_value, 0)
        except ValueError as e:
            print(f"Error durante el análisis semántico: {e}")
            return

        print("\nAnálisis completado exitosamente.")
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo '{file_path}'.")
    except Exception as e:
        print(f"Error durante la ejecución: {e}")

if __name__ == "__main__":
    main()
