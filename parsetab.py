
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASSIGN CHAR CHARACTER COMMA DIVIDE DO ELSE EQ FLOAT FOR GEQ GT ID IF INT LBRACE LEQ LPAREN LT MINUS MINUSEQ NEQ NUMBER PLUS PLUSEQ RBRACE RETURN RPAREN SEMICOLON TIMES VOID WHILEprogram : declaration_listdeclaration_list : declaration_list declaration\n                        | declarationdeclaration : var_declaration\n                   | fun_declarationvar_declaration : type_specifier ID SEMICOLON\n                       | type_specifier ID ASSIGN expression SEMICOLONfun_declaration : type_specifier ID LPAREN params RPAREN compound_stmttype_specifier : INT\n                      | FLOAT\n                      | CHAR\n                      | VOIDparams : param_list\n              | emptyparam_list : param_list COMMA param\n                  | paramparam : type_specifier IDcompound_stmt : LBRACE local_declarations statement_list RBRACElocal_declarations : local_declarations var_declaration\n                          | emptystatement_list : statement_list statement\n                      | emptystatement : expression_stmt\n                 | compound_stmt\n                 | if_stmt\n                 | while_stmt\n                 | for_stmt\n                 | return_stmtexpression_stmt : expression SEMICOLON\n                       | SEMICOLONif_stmt : IF LPAREN expression RPAREN statement\n               | IF LPAREN expression RPAREN statement ELSE statementwhile_stmt : WHILE LPAREN expression RPAREN statementfor_stmt : FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statementreturn_stmt : RETURN expression SEMICOLONexpression : var ASSIGN expression\n                  | var PLUSEQ expression\n                  | var MINUSEQ expression\n                  | simple_expressionvar : IDsimple_expression : additive_expression relop additive_expression\n                         | additive_expressionrelop : LT\n             | LEQ\n             | GT\n             | GEQ\n             | EQ\n             | NEQadditive_expression : additive_expression addop term\n                           | termaddop : PLUS\n             | MINUSterm : term mulop factor\n            | factormulop : TIMES\n             | DIVIDEfactor : LPAREN expression RPAREN\n              | var\n              | NUMBERempty :'
    
_lr_action_items = {'INT':([0,2,3,4,5,11,13,15,30,50,59,60,62,63,65,68,],[7,7,-3,-4,-5,-2,-6,7,-7,7,-8,-60,7,-20,-19,-18,]),'FLOAT':([0,2,3,4,5,11,13,15,30,50,59,60,62,63,65,68,],[8,8,-3,-4,-5,-2,-6,8,-7,8,-8,-60,8,-20,-19,-18,]),'CHAR':([0,2,3,4,5,11,13,15,30,50,59,60,62,63,65,68,],[9,9,-3,-4,-5,-2,-6,9,-7,9,-8,-60,9,-20,-19,-18,]),'VOID':([0,2,3,4,5,11,13,15,30,50,59,60,62,63,65,68,],[10,10,-3,-4,-5,-2,-6,10,-7,10,-8,-60,10,-20,-19,-18,]),'$end':([1,2,3,4,5,11,13,30,59,68,],[0,-1,-3,-4,-5,-2,-6,-7,-8,-18,]),'ID':([6,7,8,9,10,13,14,23,25,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,60,62,63,64,65,66,67,68,69,70,71,72,73,74,75,77,81,83,84,85,86,91,92,93,94,95,96,98,99,100,102,103,],[12,-9,-10,-11,-12,-6,16,16,48,-7,16,16,16,16,16,-43,-44,-45,-46,-47,-48,-51,-52,16,-55,-56,-60,-60,-20,16,-19,-22,82,-18,-21,-23,-24,-25,-26,-27,-28,-30,16,-29,16,16,16,-35,16,16,16,-31,-33,16,16,-32,16,-34,]),'SEMICOLON':([12,13,16,17,18,19,20,21,22,24,30,51,52,53,54,55,56,57,58,60,62,63,64,65,66,68,69,70,71,72,73,74,75,76,77,82,83,87,90,91,92,93,95,96,97,98,100,102,103,],[13,-6,-40,30,-58,-39,-42,-50,-54,-59,-7,-36,-37,-38,-41,-58,-49,-53,-57,-60,-60,-20,77,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,83,-30,13,-29,91,94,-35,77,77,-31,-33,99,77,-32,77,-34,]),'ASSIGN':([12,16,18,82,],[14,-40,31,14,]),'LPAREN':([12,13,14,23,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,78,79,80,81,83,84,85,86,91,92,93,94,95,96,98,99,100,102,103,],[15,-6,23,23,-7,23,23,23,23,23,-43,-44,-45,-46,-47,-48,-51,-52,23,-55,-56,-60,-60,-20,23,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,84,85,86,23,-29,23,23,23,-35,23,23,23,-31,-33,23,23,-32,23,-34,]),'RBRACE':([13,30,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,83,91,95,96,100,103,],[-6,-7,-60,-60,-20,68,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,-29,-35,-31,-33,-32,-34,]),'LBRACE':([13,30,49,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,83,91,92,93,95,96,98,100,102,103,],[-6,-7,60,-60,-60,-20,60,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,-29,-35,60,60,-31,-33,60,-32,60,-34,]),'IF':([13,30,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,83,91,92,93,95,96,98,100,102,103,],[-6,-7,-60,-60,-20,78,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,-29,-35,78,78,-31,-33,78,-32,78,-34,]),'WHILE':([13,30,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,83,91,92,93,95,96,98,100,102,103,],[-6,-7,-60,-60,-20,79,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,-29,-35,79,79,-31,-33,79,-32,79,-34,]),'FOR':([13,30,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,83,91,92,93,95,96,98,100,102,103,],[-6,-7,-60,-60,-20,80,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,-29,-35,80,80,-31,-33,80,-32,80,-34,]),'RETURN':([13,30,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,83,91,92,93,95,96,98,100,102,103,],[-6,-7,-60,-60,-20,81,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,-29,-35,81,81,-31,-33,81,-32,81,-34,]),'NUMBER':([13,14,23,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,60,62,63,64,65,66,68,69,70,71,72,73,74,75,77,81,83,84,85,86,91,92,93,94,95,96,98,99,100,102,103,],[-6,24,24,-7,24,24,24,24,24,-43,-44,-45,-46,-47,-48,-51,-52,24,-55,-56,-60,-60,-20,24,-19,-22,-18,-21,-23,-24,-25,-26,-27,-28,-30,24,-29,24,24,24,-35,24,24,24,-31,-33,24,24,-32,24,-34,]),'RPAREN':([15,16,18,19,20,21,22,24,26,27,28,29,47,48,51,52,53,54,55,56,57,58,61,88,89,101,],[-60,-40,-58,-39,-42,-50,-54,-59,49,-13,-14,-16,58,-17,-36,-37,-38,-41,-58,-49,-53,-57,-15,92,93,102,]),'PLUSEQ':([16,18,],[-40,32,]),'MINUSEQ':([16,18,],[-40,33,]),'TIMES':([16,18,21,22,24,55,56,57,58,],[-40,-58,45,-54,-59,-58,45,-53,-57,]),'DIVIDE':([16,18,21,22,24,55,56,57,58,],[-40,-58,46,-54,-59,-58,46,-53,-57,]),'LT':([16,18,20,21,22,24,55,56,57,58,],[-40,-58,36,-50,-54,-59,-58,-49,-53,-57,]),'LEQ':([16,18,20,21,22,24,55,56,57,58,],[-40,-58,37,-50,-54,-59,-58,-49,-53,-57,]),'GT':([16,18,20,21,22,24,55,56,57,58,],[-40,-58,38,-50,-54,-59,-58,-49,-53,-57,]),'GEQ':([16,18,20,21,22,24,55,56,57,58,],[-40,-58,39,-50,-54,-59,-58,-49,-53,-57,]),'EQ':([16,18,20,21,22,24,55,56,57,58,],[-40,-58,40,-50,-54,-59,-58,-49,-53,-57,]),'NEQ':([16,18,20,21,22,24,55,56,57,58,],[-40,-58,41,-50,-54,-59,-58,-49,-53,-57,]),'PLUS':([16,18,20,21,22,24,54,55,56,57,58,],[-40,-58,42,-50,-54,-59,42,-58,-49,-53,-57,]),'MINUS':([16,18,20,21,22,24,54,55,56,57,58,],[-40,-58,43,-50,-54,-59,43,-58,-49,-53,-57,]),'COMMA':([27,29,48,61,],[50,-16,-17,-15,]),'ELSE':([68,70,71,72,73,74,75,77,83,91,95,96,100,103,],[-18,-23,-24,-25,-26,-27,-28,-30,-29,-35,98,-33,-32,-34,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declaration_list':([0,],[2,]),'declaration':([0,2,],[3,11,]),'var_declaration':([0,2,62,],[4,4,65,]),'fun_declaration':([0,2,],[5,5,]),'type_specifier':([0,2,15,50,62,],[6,6,25,25,67,]),'expression':([14,23,31,32,33,64,81,84,85,86,92,93,94,98,99,102,],[17,47,51,52,53,76,87,88,89,90,76,76,97,76,101,76,]),'var':([14,23,31,32,33,34,35,44,64,81,84,85,86,92,93,94,98,99,102,],[18,18,18,18,18,55,55,55,18,18,18,18,18,18,18,18,18,18,18,]),'simple_expression':([14,23,31,32,33,64,81,84,85,86,92,93,94,98,99,102,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'additive_expression':([14,23,31,32,33,34,64,81,84,85,86,92,93,94,98,99,102,],[20,20,20,20,20,54,20,20,20,20,20,20,20,20,20,20,20,]),'term':([14,23,31,32,33,34,35,64,81,84,85,86,92,93,94,98,99,102,],[21,21,21,21,21,21,56,21,21,21,21,21,21,21,21,21,21,21,]),'factor':([14,23,31,32,33,34,35,44,64,81,84,85,86,92,93,94,98,99,102,],[22,22,22,22,22,22,22,57,22,22,22,22,22,22,22,22,22,22,22,]),'params':([15,],[26,]),'param_list':([15,],[27,]),'empty':([15,60,62,],[28,63,66,]),'param':([15,50,],[29,61,]),'relop':([20,],[34,]),'addop':([20,54,],[35,35,]),'mulop':([21,56,],[44,44,]),'compound_stmt':([49,64,92,93,98,102,],[59,71,71,71,71,71,]),'local_declarations':([60,],[62,]),'statement_list':([62,],[64,]),'statement':([64,92,93,98,102,],[69,95,96,100,103,]),'expression_stmt':([64,92,93,98,102,],[70,70,70,70,70,]),'if_stmt':([64,92,93,98,102,],[72,72,72,72,72,]),'while_stmt':([64,92,93,98,102,],[73,73,73,73,73,]),'for_stmt':([64,92,93,98,102,],[74,74,74,74,74,]),'return_stmt':([64,92,93,98,102,],[75,75,75,75,75,]),}

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
  ('var_declaration -> type_specifier ID SEMICOLON','var_declaration',3,'p_var_declaration','parser.py',22),
  ('var_declaration -> type_specifier ID ASSIGN expression SEMICOLON','var_declaration',5,'p_var_declaration','parser.py',23),
  ('fun_declaration -> type_specifier ID LPAREN params RPAREN compound_stmt','fun_declaration',6,'p_fun_declaration','parser.py',27),
  ('type_specifier -> INT','type_specifier',1,'p_type_specifier','parser.py',31),
  ('type_specifier -> FLOAT','type_specifier',1,'p_type_specifier','parser.py',32),
  ('type_specifier -> CHAR','type_specifier',1,'p_type_specifier','parser.py',33),
  ('type_specifier -> VOID','type_specifier',1,'p_type_specifier','parser.py',34),
  ('params -> param_list','params',1,'p_params','parser.py',38),
  ('params -> empty','params',1,'p_params','parser.py',39),
  ('param_list -> param_list COMMA param','param_list',3,'p_param_list','parser.py',43),
  ('param_list -> param','param_list',1,'p_param_list','parser.py',44),
  ('param -> type_specifier ID','param',2,'p_param','parser.py',51),
  ('compound_stmt -> LBRACE local_declarations statement_list RBRACE','compound_stmt',4,'p_compound_stmt','parser.py',55),
  ('local_declarations -> local_declarations var_declaration','local_declarations',2,'p_local_declarations','parser.py',59),
  ('local_declarations -> empty','local_declarations',1,'p_local_declarations','parser.py',60),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',67),
  ('statement_list -> empty','statement_list',1,'p_statement_list','parser.py',68),
  ('statement -> expression_stmt','statement',1,'p_statement','parser.py',75),
  ('statement -> compound_stmt','statement',1,'p_statement','parser.py',76),
  ('statement -> if_stmt','statement',1,'p_statement','parser.py',77),
  ('statement -> while_stmt','statement',1,'p_statement','parser.py',78),
  ('statement -> for_stmt','statement',1,'p_statement','parser.py',79),
  ('statement -> return_stmt','statement',1,'p_statement','parser.py',80),
  ('expression_stmt -> expression SEMICOLON','expression_stmt',2,'p_expression_stmt','parser.py',84),
  ('expression_stmt -> SEMICOLON','expression_stmt',1,'p_expression_stmt','parser.py',85),
  ('if_stmt -> IF LPAREN expression RPAREN statement','if_stmt',5,'p_if_stmt','parser.py',89),
  ('if_stmt -> IF LPAREN expression RPAREN statement ELSE statement','if_stmt',7,'p_if_stmt','parser.py',90),
  ('while_stmt -> WHILE LPAREN expression RPAREN statement','while_stmt',5,'p_while_stmt','parser.py',94),
  ('for_stmt -> FOR LPAREN expression SEMICOLON expression SEMICOLON expression RPAREN statement','for_stmt',9,'p_for_stmt','parser.py',98),
  ('return_stmt -> RETURN expression SEMICOLON','return_stmt',3,'p_return_stmt','parser.py',102),
  ('expression -> var ASSIGN expression','expression',3,'p_expression','parser.py',106),
  ('expression -> var PLUSEQ expression','expression',3,'p_expression','parser.py',107),
  ('expression -> var MINUSEQ expression','expression',3,'p_expression','parser.py',108),
  ('expression -> simple_expression','expression',1,'p_expression','parser.py',109),
  ('var -> ID','var',1,'p_var','parser.py',116),
  ('simple_expression -> additive_expression relop additive_expression','simple_expression',3,'p_simple_expression','parser.py',120),
  ('simple_expression -> additive_expression','simple_expression',1,'p_simple_expression','parser.py',121),
  ('relop -> LT','relop',1,'p_relop','parser.py',125),
  ('relop -> LEQ','relop',1,'p_relop','parser.py',126),
  ('relop -> GT','relop',1,'p_relop','parser.py',127),
  ('relop -> GEQ','relop',1,'p_relop','parser.py',128),
  ('relop -> EQ','relop',1,'p_relop','parser.py',129),
  ('relop -> NEQ','relop',1,'p_relop','parser.py',130),
  ('additive_expression -> additive_expression addop term','additive_expression',3,'p_additive_expression','parser.py',134),
  ('additive_expression -> term','additive_expression',1,'p_additive_expression','parser.py',135),
  ('addop -> PLUS','addop',1,'p_addop','parser.py',139),
  ('addop -> MINUS','addop',1,'p_addop','parser.py',140),
  ('term -> term mulop factor','term',3,'p_term','parser.py',144),
  ('term -> factor','term',1,'p_term','parser.py',145),
  ('mulop -> TIMES','mulop',1,'p_mulop','parser.py',149),
  ('mulop -> DIVIDE','mulop',1,'p_mulop','parser.py',150),
  ('factor -> LPAREN expression RPAREN','factor',3,'p_factor','parser.py',154),
  ('factor -> var','factor',1,'p_factor','parser.py',155),
  ('factor -> NUMBER','factor',1,'p_factor','parser.py',156),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',160),
]
