
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONrightNOTUMENOSAND BOOLEAN CADENA COMA CORDER CORIZQ DECIMAL DIFERENTE DIVISION DOBLEPT ELSE_W ENTERO FALSE FLOAT ID IF_W IGUAL IGUALIGUAL INT MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MULTIPLICACION NOT OR PDER PIZQ PRINT PTCOMA RETURN_W STRING_TYPE TRUE VOIDinit : funciones funciones : funciones funcionfunciones : funcionfuncion : tipo_funcion ID PIZQ  PDER bloque\n               | tipo_funcion ID PIZQ lista_parametros PDER bloque lista_parametros : lista_parametros COMA parametro lista_parametros : parametro parametro : tipo_dato ID bloque  : CORIZQ  CORDER\n                | CORIZQ  instrucciones CORDER instrucciones : instrucciones instruccion instrucciones : instruccioninstruccion : print_inst PTCOMA\n                   | declaracion PTCOMA\n                   | llamada PTCOMA\n                   | return_inst PTCOMA\n                   | if_instr  declaracion : tipo_dato ID  IGUAL expresion\n                    | tipo_dato ID print_inst : PRINT PIZQ expresion PDER llamada : ID PIZQ PDER\n                | ID PIZQ lista_expresiones PDER return_inst : RETURN_W\n                    | RETURN_W expresion if_instr :  IF_W PIZQ expresion PDER bloque\n                 |  IF_W PIZQ expresion PDER bloque ELSE_W bloque\n                 |  IF_W PIZQ expresion PDER bloque  listaelseif\n                 |  IF_W PIZQ expresion PDER bloque  listaelseif ELSE_W bloque listaelseif : listaelseif else_if   listaelseif : else_if else_if : ELSE_W IF_W PIZQ expresion PDER bloque lista_expresiones : lista_expresiones COMA  expresion lista_expresiones : expresionexpresion : expresion OR expresion\n                 | expresion AND expresion\n                 | NOT expresion %prec NOTexpresion : expresion MENOR expresion\n                 | expresion MAYOR expresion\n                 | expresion MAYORIGUAL expresion\n                 | expresion MENORIGUAL expresion\n                 | expresion DIFERENTE expresion\n                 | expresion IGUALIGUAL expresionexpresion : MENOS expresion %prec UMENOS\n                 | expresion MAS expresion\n                 | expresion MENOS expresion\n                 | expresion MULTIPLICACION expresion\n                 | expresion DIVISION expresion\n                 | PIZQ expresion PDERexpresion : ENTERO\n                    | DECIMAL\n                    | ID\n                    | CADENA\n                    | TRUE\n                    | FALSE expresion : llamada\n                   tipo_funcion : INT\n                     | STRING_TYPE\n                     | BOOLEAN\n                     | VOID\n                     | FLOAT tipo_dato : INT\n                     | STRING_TYPE\n                     | BOOLEAN\n                     | FLOAT'
    
_lr_action_items = {'INT':([0,2,3,10,12,21,22,24,26,27,28,33,39,41,42,43,44,45,46,102,104,105,107,109,111,114,],[5,5,-3,-2,17,-4,17,17,-9,17,-12,-17,-5,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'STRING_TYPE':([0,2,3,10,12,21,22,24,26,27,28,33,39,41,42,43,44,45,46,102,104,105,107,109,111,114,],[6,6,-3,-2,18,-4,18,18,-9,18,-12,-17,-5,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'BOOLEAN':([0,2,3,10,12,21,22,24,26,27,28,33,39,41,42,43,44,45,46,102,104,105,107,109,111,114,],[7,7,-3,-2,19,-4,19,19,-9,19,-12,-17,-5,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'VOID':([0,2,3,10,21,26,39,41,],[8,8,-3,-2,-4,-9,-5,-10,]),'FLOAT':([0,2,3,10,12,21,22,24,26,27,28,33,39,41,42,43,44,45,46,102,104,105,107,109,111,114,],[9,9,-3,-2,20,-4,20,20,-9,20,-12,-17,-5,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'$end':([1,2,3,10,21,26,39,41,],[0,-1,-3,-2,-4,-9,-5,-10,]),'ID':([4,5,6,7,8,9,16,17,18,19,20,22,26,27,28,33,35,37,41,42,43,44,45,46,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,102,104,105,107,109,110,111,114,],[11,-56,-57,-58,-59,-60,25,-61,-62,-63,-64,36,-9,36,-12,-17,48,56,-10,-11,-13,-14,-15,-16,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-25,-27,-30,-26,-29,56,-28,-31,]),'PIZQ':([11,34,36,37,38,47,49,51,52,53,56,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,106,110,],[12,47,49,53,61,53,53,53,53,53,49,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,110,53,]),'PDER':([12,14,15,25,40,49,54,55,56,57,58,59,60,62,64,65,66,79,80,81,82,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[13,23,-7,-8,-6,64,-49,-50,-51,-52,-53,-54,-55,83,-21,85,-33,-36,-43,99,100,-22,-34,-35,-37,-38,-39,-40,-41,-42,-44,-45,-46,-47,-48,-32,113,]),'CORIZQ':([13,23,100,103,108,113,],[22,22,22,22,22,22,]),'COMA':([14,15,25,40,54,55,56,57,58,59,60,64,65,66,79,80,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,],[24,-7,-8,-6,-49,-50,-51,-52,-53,-54,-55,-21,86,-33,-36,-43,-22,-34,-35,-37,-38,-39,-40,-41,-42,-44,-45,-46,-47,-48,-32,]),'CORDER':([22,26,27,28,33,41,42,43,44,45,46,102,104,105,107,109,111,114,],[26,-9,41,-12,-17,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'PRINT':([22,26,27,28,33,41,42,43,44,45,46,102,104,105,107,109,111,114,],[34,-9,34,-12,-17,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'RETURN_W':([22,26,27,28,33,41,42,43,44,45,46,102,104,105,107,109,111,114,],[37,-9,37,-12,-17,-10,-11,-13,-14,-15,-16,-25,-27,-30,-26,-29,-28,-31,]),'IF_W':([22,26,27,28,33,41,42,43,44,45,46,102,103,104,105,107,108,109,111,114,],[38,-9,38,-12,-17,-10,-11,-13,-14,-15,-16,-25,106,-27,-30,-26,106,-29,-28,-31,]),'ELSE_W':([26,41,102,104,105,109,114,],[-9,-10,103,108,-30,-29,-31,]),'PTCOMA':([29,30,31,32,37,48,50,54,55,56,57,58,59,60,64,79,80,83,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,],[43,44,45,46,-23,-19,-24,-49,-50,-51,-52,-53,-54,-55,-21,-36,-43,-20,-18,-22,-34,-35,-37,-38,-39,-40,-41,-42,-44,-45,-46,-47,-48,]),'NOT':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,]),'MENOS':([37,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,101,110,112,],[52,52,52,76,52,52,52,-49,-50,-51,-52,-53,-54,-55,52,76,52,-21,76,52,52,52,52,52,52,52,52,52,52,52,52,-36,-43,76,76,76,-22,52,76,76,76,76,76,76,76,76,-44,-45,-46,-47,-48,76,52,76,]),'ENTERO':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,]),'DECIMAL':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,]),'CADENA':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,]),'TRUE':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,58,]),'FALSE':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,59,]),'IGUAL':([48,],[63,]),'OR':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[67,-49,-50,-51,-52,-53,-54,-55,67,-21,67,-36,-43,67,67,67,-22,-34,-35,-37,-38,-39,-40,-41,-42,-44,-45,-46,-47,-48,67,67,]),'AND':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[68,-49,-50,-51,-52,-53,-54,-55,68,-21,68,-36,-43,68,68,68,-22,68,-35,-37,-38,-39,-40,-41,-42,-44,-45,-46,-47,-48,68,68,]),'MENOR':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[69,-49,-50,-51,-52,-53,-54,-55,69,-21,69,-36,-43,69,69,69,-22,69,69,None,None,None,None,None,None,-44,-45,-46,-47,-48,69,69,]),'MAYOR':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[70,-49,-50,-51,-52,-53,-54,-55,70,-21,70,-36,-43,70,70,70,-22,70,70,None,None,None,None,None,None,-44,-45,-46,-47,-48,70,70,]),'MAYORIGUAL':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[71,-49,-50,-51,-52,-53,-54,-55,71,-21,71,-36,-43,71,71,71,-22,71,71,None,None,None,None,None,None,-44,-45,-46,-47,-48,71,71,]),'MENORIGUAL':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[72,-49,-50,-51,-52,-53,-54,-55,72,-21,72,-36,-43,72,72,72,-22,72,72,None,None,None,None,None,None,-44,-45,-46,-47,-48,72,72,]),'DIFERENTE':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[73,-49,-50,-51,-52,-53,-54,-55,73,-21,73,-36,-43,73,73,73,-22,73,73,None,None,None,None,None,None,-44,-45,-46,-47,-48,73,73,]),'IGUALIGUAL':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[74,-49,-50,-51,-52,-53,-54,-55,74,-21,74,-36,-43,74,74,74,-22,74,74,None,None,None,None,None,None,-44,-45,-46,-47,-48,74,74,]),'MAS':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[75,-49,-50,-51,-52,-53,-54,-55,75,-21,75,-36,-43,75,75,75,-22,75,75,75,75,75,75,75,75,-44,-45,-46,-47,-48,75,75,]),'MULTIPLICACION':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[77,-49,-50,-51,-52,-53,-54,-55,77,-21,77,-36,-43,77,77,77,-22,77,77,77,77,77,77,77,77,77,77,-46,-47,-48,77,77,]),'DIVISION':([50,54,55,56,57,58,59,60,62,64,66,79,80,81,82,84,85,87,88,89,90,91,92,93,94,95,96,97,98,99,101,112,],[78,-49,-50,-51,-52,-53,-54,-55,78,-21,78,-36,-43,78,78,78,-22,78,78,78,78,78,78,78,78,78,78,-46,-47,-48,78,78,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'funciones':([0,],[2,]),'funcion':([0,2,],[3,10,]),'tipo_funcion':([0,2,],[4,4,]),'lista_parametros':([12,],[14,]),'parametro':([12,24,],[15,40,]),'tipo_dato':([12,22,24,27,],[16,35,16,35,]),'bloque':([13,23,100,103,108,113,],[21,39,102,107,111,114,]),'instrucciones':([22,],[27,]),'instruccion':([22,27,],[28,42,]),'print_inst':([22,27,],[29,29,]),'declaracion':([22,27,],[30,30,]),'llamada':([22,27,37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[31,31,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,]),'return_inst':([22,27,],[32,32,]),'if_instr':([22,27,],[33,33,]),'expresion':([37,47,49,51,52,53,61,63,67,68,69,70,71,72,73,74,75,76,77,78,86,110,],[50,62,66,79,80,81,82,84,87,88,89,90,91,92,93,94,95,96,97,98,101,112,]),'lista_expresiones':([49,],[65,]),'listaelseif':([102,],[104,]),'else_if':([102,104,],[105,109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> funciones','init',1,'p_init','gramatica.py',152),
  ('funciones -> funciones funcion','funciones',2,'p_funciones_lista','gramatica.py',156),
  ('funciones -> funcion','funciones',1,'p_funciones_corte','gramatica.py',161),
  ('funcion -> tipo_funcion ID PIZQ PDER bloque','funcion',5,'p_funcion','gramatica.py',168),
  ('funcion -> tipo_funcion ID PIZQ lista_parametros PDER bloque','funcion',6,'p_funcion','gramatica.py',169),
  ('lista_parametros -> lista_parametros COMA parametro','lista_parametros',3,'p_lista_parametros','gramatica.py',179),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros_corte','gramatica.py',183),
  ('parametro -> tipo_dato ID','parametro',2,'p_parametro','gramatica.py',187),
  ('bloque -> CORIZQ CORDER','bloque',2,'p_bloque','gramatica.py',194),
  ('bloque -> CORIZQ instrucciones CORDER','bloque',3,'p_bloque','gramatica.py',195),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',207),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',213),
  ('instruccion -> print_inst PTCOMA','instruccion',2,'p_instruccion','gramatica.py',218),
  ('instruccion -> declaracion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',219),
  ('instruccion -> llamada PTCOMA','instruccion',2,'p_instruccion','gramatica.py',220),
  ('instruccion -> return_inst PTCOMA','instruccion',2,'p_instruccion','gramatica.py',221),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',222),
  ('declaracion -> tipo_dato ID IGUAL expresion','declaracion',4,'p_declaracion','gramatica.py',226),
  ('declaracion -> tipo_dato ID','declaracion',2,'p_declaracion','gramatica.py',227),
  ('print_inst -> PRINT PIZQ expresion PDER','print_inst',4,'p_print','gramatica.py',233),
  ('llamada -> ID PIZQ PDER','llamada',3,'p_llamada','gramatica.py',239),
  ('llamada -> ID PIZQ lista_expresiones PDER','llamada',4,'p_llamada','gramatica.py',240),
  ('return_inst -> RETURN_W','return_inst',1,'p_return_instr','gramatica.py',248),
  ('return_inst -> RETURN_W expresion','return_inst',2,'p_return_instr','gramatica.py',249),
  ('if_instr -> IF_W PIZQ expresion PDER bloque','if_instr',5,'p_if_instr','gramatica.py',259),
  ('if_instr -> IF_W PIZQ expresion PDER bloque ELSE_W bloque','if_instr',7,'p_if_instr','gramatica.py',260),
  ('if_instr -> IF_W PIZQ expresion PDER bloque listaelseif','if_instr',6,'p_if_instr','gramatica.py',261),
  ('if_instr -> IF_W PIZQ expresion PDER bloque listaelseif ELSE_W bloque','if_instr',8,'p_if_instr','gramatica.py',262),
  ('listaelseif -> listaelseif else_if','listaelseif',2,'p_lista_else_if','gramatica.py',276),
  ('listaelseif -> else_if','listaelseif',1,'p_lista_else_if_corte','gramatica.py',281),
  ('else_if -> ELSE_W IF_W PIZQ expresion PDER bloque','else_if',6,'p_else_if','gramatica.py',285),
  ('lista_expresiones -> lista_expresiones COMA expresion','lista_expresiones',3,'p_lista_expresiones','gramatica.py',291),
  ('lista_expresiones -> expresion','lista_expresiones',1,'p_lista_expresiones_corte','gramatica.py',296),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',302),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',303),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_logica','gramatica.py',304),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',313),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',314),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',315),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',316),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_relacional','gramatica.py',317),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',318),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_aritmetica','gramatica.py',335),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',336),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',337),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',338),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',339),
  ('expresion -> PIZQ expresion PDER','expresion',3,'p_expresion_aritmetica','gramatica.py',340),
  ('expresion -> ENTERO','expresion',1,'p_expresion_primitiva','gramatica.py',354),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_primitiva','gramatica.py',355),
  ('expresion -> ID','expresion',1,'p_expresion_primitiva','gramatica.py',356),
  ('expresion -> CADENA','expresion',1,'p_expresion_primitiva','gramatica.py',357),
  ('expresion -> TRUE','expresion',1,'p_expresion_primitiva','gramatica.py',358),
  ('expresion -> FALSE','expresion',1,'p_expresion_primitiva','gramatica.py',359),
  ('expresion -> llamada','expresion',1,'p_otras_expresiones','gramatica.py',376),
  ('tipo_funcion -> INT','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',384),
  ('tipo_funcion -> STRING_TYPE','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',385),
  ('tipo_funcion -> BOOLEAN','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',386),
  ('tipo_funcion -> VOID','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',387),
  ('tipo_funcion -> FLOAT','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',388),
  ('tipo_dato -> INT','tipo_dato',1,'p_tipo_dato','gramatica.py',403),
  ('tipo_dato -> STRING_TYPE','tipo_dato',1,'p_tipo_dato','gramatica.py',404),
  ('tipo_dato -> BOOLEAN','tipo_dato',1,'p_tipo_dato','gramatica.py',405),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato','gramatica.py',406),
]
