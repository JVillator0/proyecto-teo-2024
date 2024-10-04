import re
from tokens import tokens, reserved_words, operators, delimiters

# Array to store the symbol table
symbol_table = []

# Function to add a symbol to the table
def add_symbol(line, position, type, value):
    symbol_table.append({
        'line': line,
        'position': position,
        'type': type,
        'value': value
    })

# Function to print the symbol table
def print_symbol_table():
    # Order the symbols by line number and position
    sorted_symbols = sorted(symbol_table, key=lambda symbol: (symbol['line'], symbol['position']))
    print(f"{'Línea':<10} {'Posición':<10} {'Tipo':<20} {'Valor':<20}")
    print('-' * 60)
    for symbol in sorted_symbols:
        print(f"{symbol['line']:<10} {symbol['position']:<10} {symbol['type']:<20} {symbol['value']:<20}")

# Regular expressions for comments, numbers, strings, and operators
comment_single_line_regex = r"//.*"
comment_block_regex = r"/\*[\s\S]*?\*/"
number_regex = r"\d+(\.\d+)?"
string_regex = r'"([^"\\]*(\\.[^"\\]*)*)"'
complex_operator_regex = r"(==|!=|>>|<<|::|\+\+|--|\+=|-=|\*=|/=|&&|\|\||>=|<=)"  # Operadores compuestos
simple_operator_regex = r"[+\-*/%<>=!&|^~]"
header_file_regex = r"<[a-zA-Z0-9_]+\.h>"

# Function to analyze the C++ file
def analyze_code(file):
    global symbol_table
    symbol_table.clear()
    with open(file, 'r') as f:
        lines = f.readlines()

    for line_num, line in enumerate(lines, 1):
        tokens = []
        current_pos = 0

        # Detect single-line comments first
        if re.search(comment_single_line_regex, line):
            comment = re.search(comment_single_line_regex, line).group()
            tokens.append((current_pos, 'comment', comment))
            continue  # Ignore the rest of the line

        # Detect block comments
        if re.search(comment_block_regex, line):
            block_comment = re.search(comment_block_regex, line).group()
            tokens.append((current_pos, 'block_comment', block_comment))
            continue  # Ignore the rest of the line

        # Detect strings first to avoid splitting them
        string_match = re.search(string_regex, line)
        if string_match:
            string_value = string_match.group()
            start_pos = line.find(string_value)
            tokens.append((start_pos, 'string', string_value))
            line = line.replace(string_value, '', 1)  # Remove the string from the line to process the rest

        # Reconocer directivas de preprocesador como #include
        if line.strip().startswith('#'):
            preprocessor_match = re.search(r'#\s*include', line)
            if preprocessor_match:
                add_symbol(line_num, current_pos, 'preprocessor_include', preprocessor_match.group())
                continue

        # Reconocer encabezados como <iostream> o <algo.h>
        header_match = re.search(header_file_regex, line)
        if header_match:
            header_value = header_match.group()
            start_pos = line.find(header_value)
            tokens.append((start_pos, 'header_file', header_value))
            line = line.replace(header_value, '', 1)  # Elimina el encabezado para evitar procesarlo de nuevo

        # Tokenize complex operators first (==, !=, >>, <<, ::)
        complex_matches = list(re.finditer(complex_operator_regex, line))
        for match in complex_matches:
            tokens.append((match.start(), operators[match.group()], match.group()))
            line = line[:match.start()] + ' ' * len(match.group()) + line[match.end():]

        # Tokenize simple operators
        simple_matches = list(re.finditer(simple_operator_regex, line))
        for match in simple_matches:
            tokens.append((match.start(), operators[match.group()], match.group()))
            line = line[:match.start()] + ' ' * len(match.group()) + line[match.end():]

        # Split the remaining line by non-alphanumeric characters
        rest_tokens = re.split(r'(\W)', line)
        rest_tokens = [token for token in rest_tokens if token.strip()]

        # Add rest tokens to the list
        for token in rest_tokens:
            if token.startswith('#'):
                tokens.append((current_pos, 'preprocessor', token))

            elif re.match(r'[a-zA-Z_][a-zA-Z0-9_]*', token):
                if token in reserved_words:
                    tokens.append((current_pos, reserved_words[token], token))
                else:
                    tokens.append((current_pos, 'identifier', token))

            elif re.match(number_regex, token):
                tokens.append((current_pos, 'number', token))

            elif token in delimiters:
                tokens.append((current_pos, delimiters[token], token))

            else:
                tokens.append((current_pos, 'error', token))
            current_pos += len(token) + 1

        # Sort tokens by their position in the line
        tokens.sort(key=lambda t: t[0])

        # Process each token and add it to the symbol table
        for position, token_type, token_value in tokens:
            add_symbol(line_num, position, token_type, token_value)

# Menu function to select and run examples
def display_menu():
    print("\nSeleccione el archivo que desea analizar:")
    print("1. source1.cpp (Ejemplo básico con variables y operadores)")
    print("2. source2.cpp (Condicionales y bucles)")
    print("3. source3.cpp (Funciones con parámetros y comentarios)")
    print("4. source4.cpp (Comentarios de bloque y línea)")
    print("5. source5.cpp (Manejo de cadenas de texto y estructuras de control)")
    print("0. Salir")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Ingrese el número del archivo que desea analizar: ")

        if choice == '1':
            analyze_code('source1.cpp')
        elif choice == '2':
            analyze_code('source2.cpp')
        elif choice == '3':
            analyze_code('source3.cpp')
        elif choice == '4':
            analyze_code('source4.cpp')
        elif choice == '5':
            analyze_code('source5.cpp')
        elif choice == '0':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número entre 0 y 5.")
            continue # Return to the menu without executing print_symbol_table()

        # Only print the symbol table if a valid option was selected
        print("\nTabla de símbolos:")
        print_symbol_table()
        print('-' * 60)
