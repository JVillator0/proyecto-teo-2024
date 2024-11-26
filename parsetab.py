
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CHAR CHARACTER COMMA DIVIDE DO ELSE EQ FLOAT FOR GEQ GT ID IF INT LBRACE LEQ LPAREN LT MINUS MINUSEQ NEQ NUMBER PLUS PLUSEQ RBRACE RETURN RPAREN SEMICOLON TIMES VOID WHILEprogram : declaration_listdeclaration_list : declaration_list declaration\n| declarationdeclaration : var_declaration\n| fun_declarationvar_declaration : type_specifier var_list SEMICOLONvar_list : var_list COMMA var_assign\n| var_assignvar_assign : ID\n| ID ASSIGN expressionfun_declaration : type_specifier ID LPAREN params RPAREN compound_stmttype_specifier : INT\n| FLOAT\n| CHAR\n| VOIDparams : param_list\n| emptyparam_list : param_list COMMA param\n| paramparam : type_specifier IDcompound_stmt : LBRACE local_declarations statement_list RBRACElocal_declarations : local_declarations var_declaration\n| emptystatement_list : statement_list statement\n| emptystatement : expression_stmt\n| compound_stmt\n| if_stmt\n| while_stmt\n| for_stmt\n| return_stmtexpression_stmt : expression SEMICOLON\n| SEMICOLONif_stmt : IF LPAREN expression RPAREN statement\n| IF LPAREN expression RPAREN statement ELSE statementwhile_stmt : WHILE LPAREN expression RPAREN statementfor_stmt : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statementreturn_stmt : RETURN expression SEMICOLONexpression : var ASSIGN expression\n| var PLUSEQ expression\n| var MINUSEQ expression\n| simple_expressionvar : IDsimple_expression : additive_expression relop additive_expression\n| additive_expressionrelop : LT\n| LEQ\n| GT\n| GEQ\n| EQ\n| NEQadditive_expression : additive_expression addop term\n| termaddop : PLUS\n| MINUSterm : term mulop factor\n| factormulop : TIMES\n| DIVIDEfactor : LPAREN expression RPAREN\n| var\n| NUMBERempty :'
    
_lr_action_items = {'INT':([0,2,3,4,5,11,15,17,37,55,56,66,67,69,72,],[7,7,-3,-4,-5,-2,-6,7,7,-11,-63,7,-23,-22,-21,]),'FLOAT':([0,2,3,4,5,11,15,17,37,55,56,66,67,69,72,],[8,8,-3,-4,-5,-2,-6,8,8,-11,-63,8,-23,-22,-21,]),'CHAR':([0,2,3,4,5,11,15,17,37,55,56,66,67,69,72,],[9,9,-3,-4,-5,-2,-6,9,9,-11,-63,9,-23,-22,-21,]),'VOID':([0,2,3,4,5,11,15,17,37,55,56,66,67,69,72,],[10,10,-3,-4,-5,-2,-6,10,10,-11,-63,10,-23,-22,-21,]),'$end':([1,2,3,4,5,11,15,55,72,],[0,-1,-3,-4,-5,-2,-6,-11,-21,]),'ID':([6,7,8,9,10,15,16,18,21,33,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,66,67,68,69,70,71,72,73,74,75,76,77,78,79,81,85,86,87,88,89,94,95,96,97,98,99,101,102,103,105,106,],[13,-12,-13,-14,-15,-6,20,26,35,26,26,26,26,26,26,-46,-47,-48,-49,-50,-51,-54,-55,26,-58,-59,-63,-63,-23,26,-22,-25,20,-21,-24,-26,-27,-28,-29,-30,-31,-33,26,-32,26,26,26,-38,26,26,26,-34,-36,26,26,-35,26,-37,]),'SEMICOLON':([12,13,14,15,19,20,26,27,28,29,30,31,32,34,56,58,59,60,61,62,63,64,65,66,67,68,69,70,72,73,74,75,76,77,78,79,80,81,86,90,93,94,95,96,98,99,100,101,103,105,106,],[15,-9,-8,-6,-7,-9,-43,-10,-61,-42,-45,-53,-57,-62,-63,-39,-40,-41,-44,-61,-52,-56,-60,-63,-23,81,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,86,-33,-32,94,97,-38,81,81,-34,-36,102,81,-35,81,-37,]),'COMMA':([12,13,14,19,20,23,25,26,27,28,29,30,31,32,34,35,57,58,59,60,61,62,63,64,65,],[16,-9,-8,-7,-9,37,-19,-43,-10,-61,-42,-45,-53,-57,-62,-20,-18,-39,-40,-41,-44,-61,-52,-56,-60,]),'LPAREN':([13,15,18,33,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,82,83,84,85,86,87,88,89,94,95,96,97,98,99,101,102,103,105,106,],[17,-6,33,33,33,33,33,33,33,-46,-47,-48,-49,-50,-51,-54,-55,33,-58,-59,-63,-63,-23,33,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,87,88,89,33,-32,33,33,33,-38,33,33,33,-34,-36,33,33,-35,33,-37,]),'ASSIGN':([13,20,26,28,],[18,18,-43,38,]),'RBRACE':([15,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,86,94,98,99,103,106,],[-6,-63,-63,-23,72,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,-32,-38,-34,-36,-35,-37,]),'LBRACE':([15,36,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,86,94,95,96,98,99,101,103,105,106,],[-6,56,-63,-63,-23,56,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,-32,-38,56,56,-34,-36,56,-35,56,-37,]),'IF':([15,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,86,94,95,96,98,99,101,103,105,106,],[-6,-63,-63,-23,82,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,-32,-38,82,82,-34,-36,82,-35,82,-37,]),'WHILE':([15,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,86,94,95,96,98,99,101,103,105,106,],[-6,-63,-63,-23,83,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,-32,-38,83,83,-34,-36,83,-35,83,-37,]),'FOR':([15,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,86,94,95,96,98,99,101,103,105,106,],[-6,-63,-63,-23,84,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,-32,-38,84,84,-34,-36,84,-35,84,-37,]),'RETURN':([15,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,86,94,95,96,98,99,101,103,105,106,],[-6,-63,-63,-23,85,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,-32,-38,85,85,-34,-36,85,-35,85,-37,]),'NUMBER':([15,18,33,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,66,67,68,69,70,72,73,74,75,76,77,78,79,81,85,86,87,88,89,94,95,96,97,98,99,101,102,103,105,106,],[-6,34,34,34,34,34,34,34,-46,-47,-48,-49,-50,-51,-54,-55,34,-58,-59,-63,-63,-23,34,-22,-25,-21,-24,-26,-27,-28,-29,-30,-31,-33,34,-32,34,34,34,-38,34,34,34,-34,-36,34,34,-35,34,-37,]),'RPAREN':([17,22,23,24,25,26,28,29,30,31,32,34,35,54,57,58,59,60,61,62,63,64,65,91,92,104,],[-63,36,-16,-17,-19,-43,-61,-42,-45,-53,-57,-62,-20,65,-18,-39,-40,-41,-44,-61,-52,-56,-60,95,96,105,]),'PLUSEQ':([26,28,],[-43,39,]),'MINUSEQ':([26,28,],[-43,40,]),'TIMES':([26,28,31,32,34,62,63,64,65,],[-43,-61,52,-57,-62,-61,52,-56,-60,]),'DIVIDE':([26,28,31,32,34,62,63,64,65,],[-43,-61,53,-57,-62,-61,53,-56,-60,]),'LT':([26,28,30,31,32,34,62,63,64,65,],[-43,-61,43,-53,-57,-62,-61,-52,-56,-60,]),'LEQ':([26,28,30,31,32,34,62,63,64,65,],[-43,-61,44,-53,-57,-62,-61,-52,-56,-60,]),'GT':([26,28,30,31,32,34,62,63,64,65,],[-43,-61,45,-53,-57,-62,-61,-52,-56,-60,]),'GEQ':([26,28,30,31,32,34,62,63,64,65,],[-43,-61,46,-53,-57,-62,-61,-52,-56,-60,]),'EQ':([26,28,30,31,32,34,62,63,64,65,],[-43,-61,47,-53,-57,-62,-61,-52,-56,-60,]),'NEQ':([26,28,30,31,32,34,62,63,64,65,],[-43,-61,48,-53,-57,-62,-61,-52,-56,-60,]),'PLUS':([26,28,30,31,32,34,61,62,63,64,65,],[-43,-61,49,-53,-57,-62,49,-61,-52,-56,-60,]),'MINUS':([26,28,30,31,32,34,61,62,63,64,65,],[-43,-61,50,-53,-57,-62,50,-61,-52,-56,-60,]),'ELSE':([72,74,75,76,77,78,79,81,86,94,98,99,103,106,],[-21,-26,-27,-28,-29,-30,-31,-33,-32,-38,101,-36,-35,-37,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,11,]),'var_declaration':([0,2,66,],[4,4,69,]),'fun_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,17,37,66,],[6,6,21,21,71,]),'var_list':([6,71,],[12,12,]),'var_assign':([6,16,71,],[14,19,14,]),'params':([17,],[22,]),'param_list':([17,],[23,]),'empty':([17,56,66,],[24,67,70,]),'param':([17,37,],[25,57,]),'expression':([18,33,38,39,40,68,85,87,88,89,95,96,97,101,102,105,],[27,54,58,59,60,80,90,91,92,93,80,80,100,80,104,80,]),'var':([18,33,38,39,40,41,42,51,68,85,87,88,89,95,96,97,101,102,105,],[28,28,28,28,28,62,62,62,28,28,28,28,28,28,28,28,28,28,28,]),'simple_expression':([18,33,38,39,40,68,85,87,88,89,95,96,97,101,102,105,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'additive_expression':([18,33,38,39,40,41,68,85,87,88,89,95,96,97,101,102,105,],[30,30,30,30,30,61,30,30,30,30,30,30,30,30,30,30,30,]),'term':([18,33,38,39,40,41,42,68,85,87,88,89,95,96,97,101,102,105,],[31,31,31,31,31,31,63,31,31,31,31,31,31,31,31,31,31,31,]),'factor':([18,33,38,39,40,41,42,51,68,85,87,88,89,95,96,97,101,102,105,],[32,32,32,32,32,32,32,64,32,32,32,32,32,32,32,32,32,32,32,]),'relop':([30,],[41,]),'addop':([30,61,],[42,42,]),'mulop':([31,63,],[51,51,]),'compound_stmt':([36,68,95,96,101,105,],[55,75,75,75,75,75,]),'local_declarations':([56,],[66,]),'statement_list':([66,],[68,]),'statement':([68,95,96,101,105,],[73,98,99,103,106,]),'expression_stmt':([68,95,96,101,105,],[74,74,74,74,74,]),'if_stmt':([68,95,96,101,105,],[76,76,76,76,76,]),'while_stmt':([68,95,96,101,105,],[77,77,77,77,77,]),'for_stmt':([68,95,96,101,105,],[78,78,78,78,78,]),'return_stmt':([68,95,96,101,105,],[79,79,79,79,79,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declaration_list','program',1,'p_program','parser.py',5),
  ('declaration_list -> declaration_list declaration','declaration_list',2,'p_declaration_list','parser.py',9),
  ('declaration_list -> declaration','declaration_list',1,'p_declaration_list','parser.py',10),
  ('declaration -> var_declaration','declaration',1,'p_declaration','parser.py',17),
  ('declaration -> fun_declaration','declaration',1,'p_declaration','parser.py',18),
  ('var_declaration -> type_specifier var_list SEMICOLON','var_declaration',3,'p_var_declaration','parser.py',27),
  ('var_list -> var_list COMMA var_assign','var_list',3,'p_var_list','parser.py',31),
  ('var_list -> var_assign','var_list',1,'p_var_list','parser.py',32),
  ('var_assign -> ID','var_assign',1,'p_var_assign','parser.py',39),
  ('var_assign -> ID ASSIGN expression','var_assign',3,'p_var_assign','parser.py',40),
  ('fun_declaration -> type_specifier ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','parser.py',48),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',52),
  ('type_specifier -> FLOAT','type_specifier',1,'p_type_specifier','parser.py',53),
  ('type_specifier -> CHAR','type_specifier',1,'p_type_specifier','parser.py',54),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','parser.py',55),
  ('params -> param_list','params',1,'p_params','parser.py',59),
  ('params -> empty','params',1,'p_params','parser.py',60),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parser.py',64),
  ('param_list -> param','param_list',1,'p_param_list','parser.py',65),
  ('param -> type_specifier ID','param',2,'p_param','parser.py',72),
  ('compound_stmt -> LBRACE local_declarations statement_list RBRACE','compound_stmt',4,'p_compound_stmt','parser.py',76),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations','parser.py',80),
  ('local_declarations -> empty','local_declarations',1,'p_local_declarations','parser.py',81),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',88),
  ('statement_list -> empty','statement_list',1,'p_statement_list','parser.py',89),
  ('statement -> expression_stmt','statement',1,'p_statement','parser.py',96),
  ('statement -> compound_stmt','statement',1,'p_statement','parser.py',97),
  ('statement -> if_stmt','statement',1,'p_statement','parser.py',98),
  ('statement -> while_stmt','statement',1,'p_statement','parser.py',99),
  ('statement -> for_stmt','statement',1,'p_statement','parser.py',100),
  ('statement -> return_stmt','statement',1,'p_statement','parser.py',101),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt','parser.py',105),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt','parser.py',106),
  ('if_stmt -> IF LPAREN expression RPAREN statement','if_stmt',5,'p_if_stmt','parser.py',110),
  ('if_stmt -> IF LPAREN expression RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','parser.py',111),
  ('while_stmt -> WHILE LPAREN expression RPAREN statement','while_stmt',5,'p_while_stmt','parser.py',115),
  ('for_stmt -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement','for_stmt',9,'p_for_stmt','parser.py',119),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt','parser.py',123),
  ('expression -> var ASSIGN expression','expression',3,'p_expression','parser.py',127),
  ('expression -> var PLUSEQ expression','expression',3,'p_expression','parser.py',128),
  ('expression -> var MINUSEQ expression','expression',3,'p_expression','parser.py',129),
  ('expression -> simple_expression','expression',1,'p_expression','parser.py',130),
  ('var -> ID','var',1,'p_var','parser.py',137),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression','parser.py',141),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression','parser.py',142),
  ('relop -> LT','relop',1,'p_relop','parser.py',146),
  ('relop -> LEQ','relop',1,'p_relop','parser.py',147),
  ('relop -> GT','relop',1,'p_relop','parser.py',148),
  ('relop -> GEQ','relop',1,'p_relop','parser.py',149),
  ('relop -> EQ','relop',1,'p_relop','parser.py',150),
  ('relop -> NEQ','relop',1,'p_relop','parser.py',151),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression','parser.py',155),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression','parser.py',156),
  ('addop -> PLUS','addop',1,'p_addop','parser.py',160),
  ('addop -> MINUS','addop',1,'p_addop','parser.py',161),
  ('term -> term mulop factor','term',3,'p_term','parser.py',165),
  ('term -> factor','term',1,'p_term','parser.py',166),
  ('mulop -> TIMES','mulop',1,'p_mulop','parser.py',170),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','parser.py',171),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',175),
  ('factor -> var','factor',1,'p_factor','parser.py',176),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',177),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',181),
]
