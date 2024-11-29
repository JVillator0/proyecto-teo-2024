import ply.lex as lex

# Token names list
tokens = [
    # Basic tokens
    'ASSIGN', 'CHAR', 'COMMA', 'EOF', 'FLOAT', 'ID', 'INCLUDE', 
    'INT', 'LBRACE', 'LOGIC', 'LPAREN', 'NUMBER', 'OP', 
    'QUOTES', 'RBRACE', 'READ', 'RELATIONAL', 'RETURN', 
    'RPAREN', 'SEMICOLON', 'STRING', 'VOID', 'WRITE',
    
    # Reserved words
    'DO', 'ELSE', 'FOR', 'IF', 'WHILE'
]

# Reserved words dictionary
reserved = {
    'char': 'CHAR',
    'do': 'DO',
    'else': 'ELSE',
    'float': 'FLOAT',
    'for': 'FOR',
    'if': 'IF',
    'int': 'INT',
    'printf': 'WRITE',
    'return': 'RETURN',
    'scanf': 'READ',
    'void': 'VOID', 
    'while': 'WHILE'
}

# Simple regular expression rules
t_ASSIGN = r'='
t_COMMA = r','
t_EOF = r'\$'
t_LBRACE = r'\{'
t_LPAREN = r'\('
t_QUOTES = r'\"'
t_RBRACE = r'\}'
t_RPAREN = r'\)'
t_SEMICOLON = r';'

def t_CHAR(t):
    # Recognize character strings
    r'\"([^\\"]|\\.|\n)*\"'
    return t

def t_COMMENT(t):
    # Handle single and multi-line comments
    r'\/\/.*|\/\*[\s\S]*?\*\/'
    # Increment line number based on newlines in comment
    t.lexer.lineno += t.value.count('\n')
    pass  # Comments are ignored

def t_error(t):
    # Handle lexical errors
    t.lexer.skip(1)

def t_ID(t):
    # Identify identifiers and reserved words
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check for reserved words
    t.type = reserved.get(t.value, 'ID') 
    return t

def t_INCLUDE(t):
    # Recognize include directives
    r'\#include[ ]*<[^>]+>'
    # Increment line number 
    t.lexer.lineno += t.value.count('\n')  
    pass  # Includes are ignored

def t_LOGIC(t):
    # Recognize logical operators
    r'(\>=)|(\<=)|(\==)|(\!=)|(\<)|(\>)'
    return t

def t_newline(t):
    # Track new lines
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_NUMBER(t):
    # Recognize numbers (integers and floats)
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_OP(t):
    # Recognize arithmetic operators
    r'(\+)|(\-)|(\*)|(\/)|(\%)'
    return t

def t_RELATIONAL(t):
    # Recognize relational operators
    r'(\&{2})|(\|{2})'
    return t

def t_STRING(t):
    # Recognize string literals
    r'\"([^\\\n]|(\\.))*\"'
    return t

# Characters to ignore
t_ignore = ' \t'

# Create lexer
lexer = lex.lex(debug=1)