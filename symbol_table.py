class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_symbol(self, name, symbol_type, scope):
        if name in self.table:
            raise ValueError(f"Symbol '{name}' already defined in the current scope.")
        self.table[name] = {"type": symbol_type, "scope": scope}

    def get_symbol(self, name):
        return self.table.get(name, None)

    def __str__(self):
        result = "Symbol Table:\n"
        for name, info in self.table.items():
            result += f"{name}: {info}\n"
        return result


class SemanticAnalyzer:
    def __init__(self):
        self.symbol_table = SymbolTable()

    def analyze(self, ast):
        for node in ast:
            self.process_node(node)

    def process_node(self, node):
        if not isinstance(node, tuple):
            return

        kind = node[0]
        
        if kind == "var_decl":
            # Manejar declaraciones de variables
            var_list = node[2];

            for var in var_list:
                name = var[0]
                symbol_type = node[1]
                self.analyze_variable_declaration(name, symbol_type, "global")

        elif kind == "assign":
            # Manejar asignaciones
            name = node[1]
            self.analyze_variable_usage(name)
        elif kind == "fun_decl":
            # Procesar declaraciones de funciones
            name = node[2]
            symbol_type = node[1]
            self.analyze_variable_declaration(name, f"function({symbol_type})", "global")
            body = node[4]
            if isinstance(body, tuple) and body[0] == "compound_stmt":
                self.analyze(body[1])  # Procesar declaraciones locales
                self.analyze(body[2])  # Procesar statements
        elif kind == "compound_stmt":
            # Procesar declaraciones locales y statements
            self.analyze(node[1])  # Local declarations
            self.analyze(node[2])  # Statements
        elif isinstance(node, list):
            # Procesar listas de nodos
            for subnode in node:
                self.process_node(subnode)

    def analyze_variable_declaration(self, name, symbol_type, scope):
        try:
            self.symbol_table.add_symbol(name, symbol_type, scope)
        except ValueError as e:
            print(f"Semantic Error: {e}")

    def analyze_variable_usage(self, name):
        if not self.symbol_table.get_symbol(name):
            print(f"Semantic Error: Variable '{name}' is not declared.")

    def print_symbol_table(self):
        print(self.symbol_table)
