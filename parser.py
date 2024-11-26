import ply.yacc as yacc
from lexer import tokens

def p_program(p):
    'program : declaration_list'
    p[0] = p[1]

def p_declaration_list(p):
    '''declaration_list : declaration_list declaration
                        | declaration'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_declaration(p):
    '''declaration : var_declaration
                   | fun_declaration'''
    p[0] = p[1]

# def p_var_declaration(p):
#     '''var_declaration : type_specifier ID SEMICOLON
#                        | type_specifier ID ASSIGN expression SEMICOLON'''
#     p[0] = ('var_decl', p[1], p[2], p[4] if len(p) > 4 else None)

def p_var_declaration(p):
    '''var_declaration : type_specifier var_list SEMICOLON'''
    p[0] = ('var_decl', p[1], p[2])

def p_var_list(p):
    '''var_list : var_list COMMA var_assign
                | var_assign'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]

def p_var_assign(p):
    '''var_assign : ID
                  | ID ASSIGN expression'''
    if len(p) == 2:
        p[0] = (p[1], None)
    else:
        p[0] = (p[1], p[3])


def p_fun_declaration(p):
    '''fun_declaration : type_specifier ID LPAREN params RPAREN compound_stmt'''
    p[0] = ('fun_decl', p[1], p[2], p[4], p[6])

def p_type_specifier(p):
    '''type_specifier : INT
                      | FLOAT
                      | CHAR
                      | VOID'''
    p[0] = p[1]

def p_params(p):
    '''params : param_list
              | empty'''
    p[0] = p[1]

def p_param_list(p):
    '''param_list : param_list COMMA param
                  | param'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_param(p):
    '''param : type_specifier ID'''
    p[0] = ('param', p[1], p[2])

def p_compound_stmt(p):
    '''compound_stmt : LBRACE local_declarations statement_list RBRACE'''
    p[0] = ('compound_stmt', p[2], p[3])

def p_local_declarations(p):
    '''local_declarations : local_declarations var_declaration
                          | empty'''
    if len(p) == 2:
        p[0] = [] if p[1] is None else p[1]
    else:
        p[0] = p[1] + [p[2]]

def p_statement_list(p):
    '''statement_list : statement_list statement
                      | empty'''
    if len(p) == 2:
        p[0] = [] if p[1] is None else p[1]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : expression_stmt
                 | compound_stmt
                 | if_stmt
                 | while_stmt
                 | for_stmt
                 | return_stmt'''
    p[0] = p[1]

def p_expression_stmt(p):
    '''expression_stmt : expression SEMICOLON
                       | SEMICOLON'''
    p[0] = p[1] if len(p) > 2 else None

def p_if_stmt(p):
    '''if_stmt : IF LPAREN expression RPAREN statement
               | IF LPAREN expression RPAREN statement ELSE statement'''
    p[0] = ('if_stmt', p[3], p[5], p[7] if len(p) > 6 else None)

def p_while_stmt(p):
    '''while_stmt : WHILE LPAREN expression RPAREN statement'''
    p[0] = ('while_stmt', p[3], p[5])

def p_for_stmt(p):
    '''for_stmt : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement'''
    p[0] = ('for_stmt', p[3], p[5], p[7], p[9])

def p_return_stmt(p):
    '''return_stmt : RETURN expression SEMICOLON'''
    p[0] = ('return', p[2])

def p_expression(p):
    '''expression : var ASSIGN expression
                  | var PLUSEQ expression
                  | var MINUSEQ expression
                  | simple_expression'''
    if len(p) == 4:
        p[0] = ('assign', p[1], p[2], p[3])
    else:
        p[0] = p[1]  # Para manejar `simple_expression`

def p_var(p):
    '''var : ID'''
    p[0] = p[1]

def p_simple_expression(p):
    '''simple_expression : additive_expression relop additive_expression
                         | additive_expression'''
    p[0] = p[1:]

def p_relop(p):
    '''relop : LT
             | LEQ
             | GT
             | GEQ
             | EQ
             | NEQ'''
    p[0] = p[1]

def p_additive_expression(p):
    '''additive_expression : additive_expression addop term
                           | term'''
    p[0] = p[1:]

def p_addop(p):
    '''addop : PLUS
             | MINUS'''
    p[0] = p[1]

def p_term(p):
    '''term : term mulop factor
            | factor'''
    p[0] = p[1:]

def p_mulop(p):
    '''mulop : TIMES
             | DIVIDE'''
    p[0] = p[1]

def p_factor(p):
    '''factor : LPAREN expression RPAREN
              | var
              | NUMBER'''
    p[0] = p[1]

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at '{p.value}', line {p.lineno}")
    else:
        print("Syntax error at EOF")

parser = yacc.yacc()
