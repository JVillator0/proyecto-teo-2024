# Imports and global configuration
from lexer import tokens, lexer
from parse_table import *
from collections import defaultdict
import time
import sys

stack = ["EOF", 0]

def parse(code):
    # Open and read a source code file
    lexer.input(code)    
    tok = lexer.token()
    x = stack[-1] # First element of the stack
    # Main parsing loop
    while True:    
        if x is not None and tok is not None:
            # Token and Stack Handling
            if x == tok.type:
                symbol_table_insert(tok.value, tok.type, tok.lineno, tok.lexpos)
                stack.pop()
                x = stack[-1]
                tok = lexer.token()
            
            # Error Handling           
            if x in tokens and x != tok.type:
                print("Error: expected ", x)
                print("Found: ", tok.type)
                print("At position:", tok.lexpos)
                print("At line:", tok.lineno)
                tok = panic_mode_recovery(x, tok)
                continue
            
            if x not in tokens:
                if tok is None:
                    print("Syntax analysis completed successfully")
                    return # Accept
                
                print("Entering symbol table:")
                print(x)
                print(tok.type)
                print("At line:", tok.lineno)
                print("With value: ", tok.value)
                
                cell = search_in_table(x, tok.type)      
                # Error Handling and Recovery                      
                if cell is None:
                    expected_tokens = find_expected_tokens(x)
                    print("Error: expected one of", expected_tokens, "but found", tok.type)
                    print("At position:", tok.lexpos)
                    print("At line:", tok.lineno)
                    print("Cell: ", cell)
                    print("Entering panic mode...")
                    tok = panic_mode_recovery(expected_tokens, tok)
                    
                    if tok is None or tok.type == 'EOF':
                        print("Could not recover from error.")
                        return 0
                    
                    # Resume analysis after recovery
                    x = stack[-1]
                    continue
                else:
                    stack.pop()
                    add_to_stack(cell)
                    print(stack)
                    print("/------------------------------------------------------------------------------/")
                    x = stack[-1]
        else:
            print("Syntax analysis completed successfully")
            return 0

def panic_mode_recovery(recovery_tokens, tok):
    # Loops to find a recovery token and adjust the stack
    while tok is not None and tok.type not in recovery_tokens:
        tok = lexer.token()
        print(f"Searching for {recovery_tokens}")
    
    while stack and (stack[-1] not in recovery_tokens and stack[-1] in tokens):
        stack.pop()

    if stack and tok is not None:
        print(f"Successful recovery, next token: {tok.type}, next in stack: {stack[-1]}")
        return tok
    else:
        print("Stack is empty after panic mode recovery.")
        return tok

def search_in_table(no_terminal, terminal):
    for row in table:
        if row[0] == no_terminal and row[1] == terminal:
            return row[2] # Return the cell

def add_to_stack(production):
    for element in reversed(production):
        if element != 'empty': # Do not insert empty
            stack.append(element)

def find_expected_tokens(no_terminal):
    expected = []
    for row in table:
        if row[0] == no_terminal and row[2] is not None:
            expected.append(row[1])
    return expected

# Symbol table
symbol_table = defaultdict(list)

# Insert into symbol table
def symbol_table_insert(name, var_type, line, pos):
    symbol_table[name].append({"type": var_type, "line": line, "pos": pos})

# Print symbol table
def symbol_table_print():
    print("Name                              Type        Line    Position")
    print("----------------------------------------------------------------------")
    for name, entries in symbol_table.items():
        for entry in entries:
            print(f"{name:<35}{entry['type']:10}{entry['line']:10}{entry['pos']:10}")

# Search in symbol table
def symbol_table_search(name):
    if name in symbol_table:
        for info in symbol_table[name]:
            print(f"{name} - {info}")
    else:
        print(f"'{name}' not found in symbol table.")

# Delete from symbol table
def symbol_table_delete(name):
    if name in symbol_table:
        del symbol_table[name]
        print(f"'{name}' removed from symbol table.")
    else:
        print(f"Could not delete '{name}' as it is not in the symbol table.")

symbol_table_print()