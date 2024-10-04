# Definition of tokens
tokens = [
    'identifier',
    'number',
    'string',
    'preprocessor',
    'greater_than',
    'greater_equal_than',
    'less_equal_than',
    'equal_to',
    'less_than',
    'scope_resolution',
    'not_equal',
    'right_shift',
    'left_shift',
    'plus',
    'minus',
    'multiplication',
    'division',
    'comma',
    'end_of_instruction',
    'open_parenthesis',
    'open_brace',
    'close_brace',
    'close_parenthesis',
    'boolean',
    'assignment',
    'error'
]

# Reserved words
reserved_words = {
    'class': 'reserved_word',
    'if': 'reserved_word',
    'else': 'reserved_word',
    'using': 'reserved_word',
    'return': 'reserved_word',
    'const': 'reserved_word',
    'int': 'reserved_word',
    'double': 'reserved_word',
    'string': 'reserved_word',
    'bool': 'reserved_word',
    'for': 'reserved_word',
    'while': 'reserved_word',
    'do': 'reserved_word',
    'switch': 'reserved_word',
    'case': 'reserved_word',
    'break': 'reserved_word',
    'continue': 'reserved_word',
    'true': 'boolean',
    'false': 'boolean',
    'cin': 'reserved_word',
    'cout': 'reserved_word',
    'endl': 'reserved_word',
    'void': 'reserved_word',
    'public': 'reserved_word',
    'private': 'reserved_word',
    'protected': 'reserved_word',
    'static': 'reserved_word',
    'new': 'reserved_word',
}

# Operators
operators = {
    '%': 'modulus',
    '==': 'equal_to',
    '!=': 'not_equal',
    '>>': 'right_shift',
    '<<': 'left_shift',
    '=': 'assignment',
    '+': 'plus',
    '-': 'minus',
    '*': 'multiplication',
    '/': 'division',
    '&&': 'and_operator',
    '||': 'or_operator',
    '>': 'greater_than',
    '<': 'less_than',
    '>=': 'greater_equal_than',
    '<=': 'less_equal_than',
    '::': 'scope_resolution',
    '!': 'not_operator'
}

# Delimiters
delimiters = {
    ';': 'end_of_instruction',
    '{': 'open_brace',
    '}': 'close_brace',
    '(': 'open_parenthesis',
    ')': 'close_parenthesis',
    ',': 'comma',
    '.': 'dot'
}
