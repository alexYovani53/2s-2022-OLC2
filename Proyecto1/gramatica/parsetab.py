
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDnonassocMAYORMENORIGUALMENORMAYORIGUALIGUALIGUALDIFERENTEleftMASMENOSleftMULTIPLICACIONDIVISIONrightNOTUMENOSAND BOOLEAN CADENA CLASS COMA CORDER CORIZQ DECIMAL DIFERENTE DIVISION DOBLEPT ELSE_W ENTERO FALSE FLOAT ID IF_W IGUAL IGUALIGUAL INT LLAVEDER LLAVEIZQ MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS MULTIPLICACION NEW NOT OR PDER PIZQ PRINT PTCOMA PUNTO RETURN_W STRING_TYPE TRUE VOIDinit : clases_funciones  clases_funciones : clases_funciones clase_funcion  clases_funciones : clase_funcion  clase_funcion : clase\n                      | funcion clase_funcion : error LLAVEDER   clase : CLASS ID bloqueClase bloqueClase : LLAVEIZQ instrs_clase LLAVEDER\n                    | LLAVEIZQ  LLAVEDERfuncion : tipo_funcion ID PIZQ  PDER bloque\n               | tipo_funcion ID PIZQ lista_parametros PDER bloque lista_parametros : lista_parametros COMA parametro lista_parametros : parametro parametro : tipo_dato ID\n                  | MULTIPLICACION tipo_dato IDbloque  : LLAVEIZQ  LLAVEDER\n                | LLAVEIZQ  instrucciones LLAVEDER  instrs_clase : instrs_clase instr  instrs_clase :  instr  instr : declaracion PTCOMAinstrucciones : instrucciones instruccion instrucciones : instruccion instruccion : print_inst PTCOMA\n                   | declaracion PTCOMA\n                   | declaracion_objeto PTCOMA\n                   | declaracion_arreglo PTCOMA\n                   | llamada PTCOMA\n                   | return_inst PTCOMA\n                   | if_instr instruccion : error PTCOMA  declaracion : tipo_dato ID IGUAL expresion\n                    | tipo_dato ID  declaracion_arreglo : tipo_dato niveles ID IGUAL expresion niveles : niveles nivel  niveles : nivel  nivel : CORIZQ CORDER  declaracion_objeto : ID ID IGUAL expresion print_inst : PRINT PIZQ expresion PDER llamada : ID PIZQ PDER\n                | ID PIZQ lista_expresiones PDER return_inst : RETURN_W\n                    | RETURN_W expresion if_instr :  IF_W PIZQ expresion PDER bloque\n                 |  IF_W PIZQ expresion PDER bloque ELSE_W bloque\n                 |  IF_W PIZQ expresion PDER bloque  listaelseif\n                 |  IF_W PIZQ expresion PDER bloque  listaelseif ELSE_W bloque listaelseif : listaelseif else_if   listaelseif : else_if else_if : ELSE_W IF_W PIZQ expresion PDER bloque lista_expresiones : lista_expresiones COMA  expresion lista_expresiones : expresionexpresion : expresion OR expresion\n                 | expresion AND expresion\n                 | NOT expresion %prec NOTexpresion : expresion MENOR expresion\n                 | expresion MAYOR expresion\n                 | expresion MAYORIGUAL expresion\n                 | expresion MENORIGUAL expresion\n                 | expresion DIFERENTE expresion\n                 | expresion IGUALIGUAL expresionexpresion : MENOS expresion %prec UMENOS\n                 | expresion MAS expresion\n                 | expresion MENOS expresion\n                 | expresion MULTIPLICACION expresion\n                 | expresion DIVISION expresion\n                 | PIZQ expresion PDERexpresion : ENTERO\n                    | DECIMAL\n                    | ID\n                    | CADENA\n                    | TRUE\n                    | FALSE expresion : llamada\n                  | acceso_objeto_expresion\n                  | acceso_array_expresion\n                  | instancia_objeto\n                  | array_data\n                  | array_instancia\n                  | if_instr array_data : CORIZQ lista_expresiones CORDER array_instancia : NEW tipo_dato dimensiones dimensiones : dimensiones dimension dimensiones : dimension dimension : CORIZQ expresion CORDER instancia_objeto : NEW ID PIZQ PDER\n                         | NEW ID PIZQ lista_expresiones PDER acceso_objeto_expresion : acceso_objeto acceso_objeto : acceso_objeto  PUNTO expresion acceso_objeto : expresionacceso_array_expresion : ID dimensiones tipo_funcion : INT\n                     | STRING_TYPE\n                     | BOOLEAN\n                     | VOID\n                     | FLOAT tipo_dato : INT\n                     | STRING_TYPE\n                     | BOOLEAN\n                     | FLOAT'
    
_lr_action_items = {'error':([0,2,3,4,5,14,15,18,22,35,39,40,46,47,48,55,62,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[6,6,-3,-4,-5,-2,-6,-7,-9,-8,-10,56,-16,56,-22,-29,-11,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'CLASS':([0,2,3,4,5,14,15,18,22,35,39,46,62,85,],[7,7,-3,-4,-5,-2,-6,-7,-9,-8,-10,-16,-11,-17,]),'INT':([0,2,3,4,5,14,15,18,19,20,21,22,23,34,35,36,37,39,40,42,46,47,48,55,62,83,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[9,9,-3,-4,-5,-2,-6,-7,26,26,26,-9,-19,26,-8,-18,-20,-10,26,26,-16,26,-22,-29,-11,26,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'STRING_TYPE':([0,2,3,4,5,14,15,18,19,20,21,22,23,34,35,36,37,39,40,42,46,47,48,55,62,83,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[10,10,-3,-4,-5,-2,-6,-7,27,27,27,-9,-19,27,-8,-18,-20,-10,27,27,-16,27,-22,-29,-11,27,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'BOOLEAN':([0,2,3,4,5,14,15,18,19,20,21,22,23,34,35,36,37,39,40,42,46,47,48,55,62,83,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[11,11,-3,-4,-5,-2,-6,-7,28,28,28,-9,-19,28,-8,-18,-20,-10,28,28,-16,28,-22,-29,-11,28,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'VOID':([0,2,3,4,5,14,15,18,22,35,39,46,62,85,],[12,12,-3,-4,-5,-2,-6,-7,-9,-8,-10,-16,-11,-17,]),'FLOAT':([0,2,3,4,5,14,15,18,19,20,21,22,23,34,35,36,37,39,40,42,46,47,48,55,62,83,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[13,13,-3,-4,-5,-2,-6,-7,29,29,29,-9,-19,29,-8,-18,-20,-10,29,29,-16,29,-22,-29,-11,29,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'$end':([1,2,3,4,5,14,15,18,22,35,39,46,62,85,],[0,-1,-3,-4,-5,-2,-6,-7,-9,-8,-10,-16,-11,-17,]),'LLAVEDER':([6,19,21,23,36,37,40,46,47,48,55,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[15,22,35,-19,-18,-20,46,-16,85,-22,-29,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'ID':([7,8,9,10,11,12,13,25,26,27,28,29,33,40,44,45,46,47,48,55,58,59,60,67,68,69,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,127,128,129,149,152,154,163,166,167,169,171,172,173,176,],[16,17,-91,-92,-93,-94,-95,38,-96,-97,-98,-99,43,59,64,65,-16,59,-22,-29,38,98,65,65,65,65,121,65,-17,-21,-23,-24,-25,-26,-27,-28,-30,65,126,-35,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,65,-34,-36,65,65,65,65,-43,-45,-48,-44,-47,65,-46,-49,]),'LLAVEIZQ':([16,30,41,157,165,170,175,],[19,40,40,40,40,40,40,]),'PIZQ':([17,45,57,59,60,61,65,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,121,129,149,152,154,168,172,],[20,69,94,99,69,101,99,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,69,149,69,69,69,69,172,69,]),'PDER':([20,31,32,43,46,63,64,65,70,71,72,73,74,75,76,77,78,79,80,81,82,85,99,102,103,117,118,119,124,125,130,131,132,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,156,158,159,160,161,163,164,166,167,169,171,173,174,176,],[30,41,-13,-14,-16,-12,-15,-69,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,130,-90,-83,-54,-61,147,-51,153,-39,156,157,-82,-52,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,-88,159,-81,-80,-40,-84,-85,164,-50,-43,-86,-45,-48,-44,-47,-46,175,-49,]),'MULTIPLICACION':([20,42,46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[34,34,-16,-69,115,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,115,-90,-83,-54,-61,115,115,115,-39,115,-82,115,115,115,115,115,115,115,115,115,115,115,-64,-65,-66,115,-81,-80,115,-40,-84,-85,115,115,-43,-86,-45,-48,-44,-47,-46,115,-49,]),'PTCOMA':([24,38,46,49,50,51,52,53,54,56,60,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,130,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,153,155,156,158,159,162,163,164,166,167,169,171,173,176,],[37,-32,-16,87,88,89,90,91,92,93,-41,-69,-31,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,-42,-90,-83,-54,-61,-39,-82,-52,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,-88,-81,-80,-38,-37,-40,-84,-85,-33,-43,-86,-45,-48,-44,-47,-46,-49,]),'CORIZQ':([26,27,28,29,45,58,60,65,67,68,69,84,94,95,96,99,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,120,122,127,128,129,133,149,150,152,154,158,172,],[-96,-97,-98,-99,84,97,84,104,84,84,84,84,84,97,-35,84,84,104,-83,84,84,84,84,84,84,84,84,84,84,84,84,84,84,104,-34,-36,84,-82,84,104,84,84,-84,84,]),'COMA':([31,32,43,46,63,64,65,70,71,72,73,74,75,76,77,78,79,80,81,82,85,102,103,117,118,123,124,130,131,133,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,156,158,159,160,161,163,164,166,167,169,171,173,176,],[42,-13,-14,-16,-12,-15,-69,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,-90,-83,-54,-61,152,-51,-39,152,-82,-52,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,-88,-81,-80,-40,-84,-85,152,-50,-43,-86,-45,-48,-44,-47,-46,-49,]),'IGUAL':([38,98,126,],[45,129,154,]),'PRINT':([40,46,47,48,55,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[57,-16,57,-22,-29,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'RETURN_W':([40,46,47,48,55,85,86,87,88,89,90,91,92,93,163,166,167,169,171,173,176,],[60,-16,60,-22,-29,-17,-21,-23,-24,-25,-26,-27,-28,-30,-43,-45,-48,-44,-47,-46,-49,]),'IF_W':([40,45,46,47,48,55,60,67,68,69,84,85,86,87,88,89,90,91,92,93,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,163,165,166,167,169,170,171,172,173,176,],[61,61,-16,61,-22,-29,61,61,61,61,61,-17,-21,-23,-24,-25,-26,-27,-28,-30,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,61,-43,168,-45,-48,-44,168,-47,61,-46,-49,]),'NOT':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,67,]),'MENOS':([45,46,60,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,84,85,94,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,124,125,129,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,154,155,156,158,159,161,162,163,164,166,167,169,171,172,173,174,176,],[68,-16,68,-69,114,68,68,68,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,68,-17,68,68,114,68,-90,-83,68,68,68,68,68,68,68,68,68,68,68,68,68,-54,-61,114,68,114,114,68,-39,114,-82,114,114,114,114,114,114,114,114,114,-62,-63,-64,-65,-66,114,68,-81,-80,68,68,114,-40,-84,-85,114,114,-43,-86,-45,-48,-44,-47,68,-46,114,-49,]),'ENTERO':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,]),'DECIMAL':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,71,]),'CADENA':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,72,]),'TRUE':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,73,]),'FALSE':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,74,]),'NEW':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,83,]),'ELSE_W':([46,85,163,166,167,171,176,],[-16,-17,165,170,-48,-47,-49,]),'OR':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,105,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,105,-90,-83,-54,-61,105,105,105,-39,105,-82,105,-52,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,105,-81,-80,105,-40,-84,-85,105,105,-43,-86,-45,-48,-44,-47,-46,105,-49,]),'AND':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,106,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,106,-90,-83,-54,-61,106,106,106,-39,106,-82,106,106,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,106,-81,-80,106,-40,-84,-85,106,106,-43,-86,-45,-48,-44,-47,-46,106,-49,]),'MENOR':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,107,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,107,-90,-83,-54,-61,107,107,107,-39,107,-82,107,107,107,-89,-89,-89,-89,-89,-89,-62,-63,-64,-65,-66,107,-81,-80,107,-40,-84,-85,107,107,-43,-86,-45,-48,-44,-47,-46,107,-49,]),'MAYOR':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,108,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,108,-90,-83,-54,-61,108,108,108,-39,108,-82,108,108,108,-89,-89,-89,-89,-89,-89,-62,-63,-64,-65,-66,108,-81,-80,108,-40,-84,-85,108,108,-43,-86,-45,-48,-44,-47,-46,108,-49,]),'MAYORIGUAL':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,109,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,109,-90,-83,-54,-61,109,109,109,-39,109,-82,109,109,109,-89,-89,-89,-89,-89,-89,-62,-63,-64,-65,-66,109,-81,-80,109,-40,-84,-85,109,109,-43,-86,-45,-48,-44,-47,-46,109,-49,]),'MENORIGUAL':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,110,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,110,-90,-83,-54,-61,110,110,110,-39,110,-82,110,110,110,-89,-89,-89,-89,-89,-89,-62,-63,-64,-65,-66,110,-81,-80,110,-40,-84,-85,110,110,-43,-86,-45,-48,-44,-47,-46,110,-49,]),'DIFERENTE':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,111,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,111,-90,-83,-54,-61,111,111,111,-39,111,-82,111,111,111,-89,-89,-89,-89,-89,-89,-62,-63,-64,-65,-66,111,-81,-80,111,-40,-84,-85,111,111,-43,-86,-45,-48,-44,-47,-46,111,-49,]),'IGUALIGUAL':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,112,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,112,-90,-83,-54,-61,112,112,112,-39,112,-82,112,112,112,-89,-89,-89,-89,-89,-89,-62,-63,-64,-65,-66,112,-81,-80,112,-40,-84,-85,112,112,-43,-86,-45,-48,-44,-47,-46,112,-49,]),'MAS':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,113,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,113,-90,-83,-54,-61,113,113,113,-39,113,-82,113,113,113,113,113,113,113,113,113,-62,-63,-64,-65,-66,113,-81,-80,113,-40,-84,-85,113,113,-43,-86,-45,-48,-44,-47,-46,113,-49,]),'DIVISION':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,116,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,116,-90,-83,-54,-61,116,116,116,-39,116,-82,116,116,116,116,116,116,116,116,116,116,116,-64,-65,-66,116,-81,-80,116,-40,-84,-85,116,116,-43,-86,-45,-48,-44,-47,-46,116,-49,]),'PUNTO':([46,65,66,70,71,72,73,74,75,76,77,78,79,80,81,82,85,100,102,103,117,118,119,124,125,130,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,155,156,158,159,161,162,163,164,166,167,169,171,173,174,176,],[-16,-69,-89,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,120,-17,-89,-90,-83,-54,-61,-89,-89,-89,-39,-89,-82,-89,-52,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,-88,-81,-80,-89,-40,-84,-85,-89,-89,-43,-86,-45,-48,-44,-47,-46,-89,-49,]),'CORDER':([46,65,70,71,72,73,74,75,76,77,78,79,80,81,82,85,97,102,103,117,118,123,124,130,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,150,151,156,158,159,161,163,164,166,167,169,171,173,176,],[-16,-69,-67,-68,-70,-71,-72,-73,-74,-75,-76,-77,-78,-79,-87,-17,128,-90,-83,-54,-61,151,-51,-39,-82,158,-52,-53,-55,-56,-57,-58,-59,-60,-62,-63,-64,-65,-66,-88,-81,-80,-40,-84,-85,-50,-43,-86,-45,-48,-44,-47,-46,-49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'init':([0,],[1,]),'clases_funciones':([0,],[2,]),'clase_funcion':([0,2,],[3,14,]),'clase':([0,2,],[4,4,]),'funcion':([0,2,],[5,5,]),'tipo_funcion':([0,2,],[8,8,]),'bloqueClase':([16,],[18,]),'instrs_clase':([19,],[21,]),'instr':([19,21,],[23,36,]),'declaracion':([19,21,40,47,],[24,24,50,50,]),'tipo_dato':([19,20,21,34,40,42,47,83,],[25,33,25,44,58,33,58,122,]),'lista_parametros':([20,],[31,]),'parametro':([20,42,],[32,63,]),'bloque':([30,41,157,165,170,175,],[39,62,163,169,173,176,]),'instrucciones':([40,],[47,]),'instruccion':([40,47,],[48,86,]),'print_inst':([40,47,],[49,49,]),'declaracion_objeto':([40,47,],[51,51,]),'declaracion_arreglo':([40,47,],[52,52,]),'llamada':([40,45,47,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[53,75,53,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,75,]),'return_inst':([40,47,],[54,54,]),'if_instr':([40,45,47,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[55,81,55,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,81,]),'expresion':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[66,100,117,118,119,124,125,124,132,134,135,136,137,138,139,140,141,142,143,144,145,146,148,155,124,161,162,174,]),'acceso_objeto_expresion':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,76,]),'acceso_array_expresion':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,77,]),'instancia_objeto':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,78,]),'array_data':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,79,]),'array_instancia':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,]),'acceso_objeto':([45,60,67,68,69,84,94,99,101,104,105,106,107,108,109,110,111,112,113,114,115,116,120,129,149,152,154,172,],[82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,82,]),'niveles':([58,],[95,]),'nivel':([58,95,],[96,127,]),'dimensiones':([65,122,],[102,150,]),'dimension':([65,102,122,150,],[103,133,103,133,]),'lista_expresiones':([84,99,149,],[123,131,160,]),'listaelseif':([163,],[166,]),'else_if':([163,166,],[167,171,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> init","S'",1,None,None,None),
  ('init -> clases_funciones','init',1,'p_init','gramatica.py',183),
  ('clases_funciones -> clases_funciones clase_funcion','clases_funciones',2,'p_clases_funciones','gramatica.py',189),
  ('clases_funciones -> clase_funcion','clases_funciones',1,'p_clases_funciones_corte','gramatica.py',195),
  ('clase_funcion -> clase','clase_funcion',1,'p_clase_funcion','gramatica.py',200),
  ('clase_funcion -> funcion','clase_funcion',1,'p_clase_funcion','gramatica.py',201),
  ('clase_funcion -> error LLAVEDER','clase_funcion',2,'p_clase_funcion_error','gramatica.py',205),
  ('clase -> CLASS ID bloqueClase','clase',3,'p_clase','gramatica.py',210),
  ('bloqueClase -> LLAVEIZQ instrs_clase LLAVEDER','bloqueClase',3,'p_bloque_clase','gramatica.py',215),
  ('bloqueClase -> LLAVEIZQ LLAVEDER','bloqueClase',2,'p_bloque_clase','gramatica.py',216),
  ('funcion -> tipo_funcion ID PIZQ PDER bloque','funcion',5,'p_funcion','gramatica.py',224),
  ('funcion -> tipo_funcion ID PIZQ lista_parametros PDER bloque','funcion',6,'p_funcion','gramatica.py',225),
  ('lista_parametros -> lista_parametros COMA parametro','lista_parametros',3,'p_lista_parametros','gramatica.py',236),
  ('lista_parametros -> parametro','lista_parametros',1,'p_lista_parametros_corte','gramatica.py',242),
  ('parametro -> tipo_dato ID','parametro',2,'p_parametro','gramatica.py',247),
  ('parametro -> MULTIPLICACION tipo_dato ID','parametro',3,'p_parametro','gramatica.py',248),
  ('bloque -> LLAVEIZQ LLAVEDER','bloque',2,'p_bloque','gramatica.py',261),
  ('bloque -> LLAVEIZQ instrucciones LLAVEDER','bloque',3,'p_bloque','gramatica.py',262),
  ('instrs_clase -> instrs_clase instr','instrs_clase',2,'p_instrs_clase','gramatica.py',272),
  ('instrs_clase -> instr','instrs_clase',1,'p_instrs_clase_corte','gramatica.py',278),
  ('instr -> declaracion PTCOMA','instr',2,'p_instr','gramatica.py',283),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones','gramatica.py',290),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','gramatica.py',296),
  ('instruccion -> print_inst PTCOMA','instruccion',2,'p_instruccion','gramatica.py',304),
  ('instruccion -> declaracion PTCOMA','instruccion',2,'p_instruccion','gramatica.py',305),
  ('instruccion -> declaracion_objeto PTCOMA','instruccion',2,'p_instruccion','gramatica.py',306),
  ('instruccion -> declaracion_arreglo PTCOMA','instruccion',2,'p_instruccion','gramatica.py',307),
  ('instruccion -> llamada PTCOMA','instruccion',2,'p_instruccion','gramatica.py',308),
  ('instruccion -> return_inst PTCOMA','instruccion',2,'p_instruccion','gramatica.py',309),
  ('instruccion -> if_instr','instruccion',1,'p_instruccion','gramatica.py',310),
  ('instruccion -> error PTCOMA','instruccion',2,'p_error_sintaxis','gramatica.py',315),
  ('declaracion -> tipo_dato ID IGUAL expresion','declaracion',4,'p_declaracion','gramatica.py',323),
  ('declaracion -> tipo_dato ID','declaracion',2,'p_declaracion','gramatica.py',324),
  ('declaracion_arreglo -> tipo_dato niveles ID IGUAL expresion','declaracion_arreglo',5,'p_declaracion_arreglo','gramatica.py',335),
  ('niveles -> niveles nivel','niveles',2,'p_niveles','gramatica.py',340),
  ('niveles -> nivel','niveles',1,'p_niveles_corte','gramatica.py',345),
  ('nivel -> CORIZQ CORDER','nivel',2,'p_nivel','gramatica.py',349),
  ('declaracion_objeto -> ID ID IGUAL expresion','declaracion_objeto',4,'p_declaracion_objeto','gramatica.py',354),
  ('print_inst -> PRINT PIZQ expresion PDER','print_inst',4,'p_print','gramatica.py',361),
  ('llamada -> ID PIZQ PDER','llamada',3,'p_llamada','gramatica.py',368),
  ('llamada -> ID PIZQ lista_expresiones PDER','llamada',4,'p_llamada','gramatica.py',369),
  ('return_inst -> RETURN_W','return_inst',1,'p_return_instr','gramatica.py',379),
  ('return_inst -> RETURN_W expresion','return_inst',2,'p_return_instr','gramatica.py',380),
  ('if_instr -> IF_W PIZQ expresion PDER bloque','if_instr',5,'p_if_instr','gramatica.py',390),
  ('if_instr -> IF_W PIZQ expresion PDER bloque ELSE_W bloque','if_instr',7,'p_if_instr','gramatica.py',391),
  ('if_instr -> IF_W PIZQ expresion PDER bloque listaelseif','if_instr',6,'p_if_instr','gramatica.py',392),
  ('if_instr -> IF_W PIZQ expresion PDER bloque listaelseif ELSE_W bloque','if_instr',8,'p_if_instr','gramatica.py',393),
  ('listaelseif -> listaelseif else_if','listaelseif',2,'p_lista_else_if','gramatica.py',406),
  ('listaelseif -> else_if','listaelseif',1,'p_lista_else_if_corte','gramatica.py',412),
  ('else_if -> ELSE_W IF_W PIZQ expresion PDER bloque','else_if',6,'p_else_if','gramatica.py',417),
  ('lista_expresiones -> lista_expresiones COMA expresion','lista_expresiones',3,'p_lista_expresiones','gramatica.py',423),
  ('lista_expresiones -> expresion','lista_expresiones',1,'p_lista_expresiones_corte','gramatica.py',429),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_logica','gramatica.py',436),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_logica','gramatica.py',437),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_logica','gramatica.py',438),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',447),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_relacional','gramatica.py',448),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',449),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',450),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_relacional','gramatica.py',451),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_relacional','gramatica.py',452),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_aritmetica','gramatica.py',469),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',470),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',471),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',472),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_aritmetica','gramatica.py',473),
  ('expresion -> PIZQ expresion PDER','expresion',3,'p_expresion_aritmetica','gramatica.py',474),
  ('expresion -> ENTERO','expresion',1,'p_expresion_primitiva','gramatica.py',488),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_primitiva','gramatica.py',489),
  ('expresion -> ID','expresion',1,'p_expresion_primitiva','gramatica.py',490),
  ('expresion -> CADENA','expresion',1,'p_expresion_primitiva','gramatica.py',491),
  ('expresion -> TRUE','expresion',1,'p_expresion_primitiva','gramatica.py',492),
  ('expresion -> FALSE','expresion',1,'p_expresion_primitiva','gramatica.py',493),
  ('expresion -> llamada','expresion',1,'p_otras_expresiones','gramatica.py',510),
  ('expresion -> acceso_objeto_expresion','expresion',1,'p_otras_expresiones','gramatica.py',511),
  ('expresion -> acceso_array_expresion','expresion',1,'p_otras_expresiones','gramatica.py',512),
  ('expresion -> instancia_objeto','expresion',1,'p_otras_expresiones','gramatica.py',513),
  ('expresion -> array_data','expresion',1,'p_otras_expresiones','gramatica.py',514),
  ('expresion -> array_instancia','expresion',1,'p_otras_expresiones','gramatica.py',515),
  ('expresion -> if_instr','expresion',1,'p_otras_expresiones','gramatica.py',516),
  ('array_data -> CORIZQ lista_expresiones CORDER','array_data',3,'p_array_data','gramatica.py',522),
  ('array_instancia -> NEW tipo_dato dimensiones','array_instancia',3,'p_array_instancia','gramatica.py',527),
  ('dimensiones -> dimensiones dimension','dimensiones',2,'p_dimensiones','gramatica.py',531),
  ('dimensiones -> dimension','dimensiones',1,'p_dimensiones_corte','gramatica.py',537),
  ('dimension -> CORIZQ expresion CORDER','dimension',3,'p_dimension','gramatica.py',541),
  ('instancia_objeto -> NEW ID PIZQ PDER','instancia_objeto',4,'p_instancia_objeto','gramatica.py',546),
  ('instancia_objeto -> NEW ID PIZQ lista_expresiones PDER','instancia_objeto',5,'p_instancia_objeto','gramatica.py',547),
  ('acceso_objeto_expresion -> acceso_objeto','acceso_objeto_expresion',1,'p_acceso_objeto_expresion','gramatica.py',557),
  ('acceso_objeto -> acceso_objeto PUNTO expresion','acceso_objeto',3,'p_acceso_objeto','gramatica.py',562),
  ('acceso_objeto -> expresion','acceso_objeto',1,'p_acceso_objeto_cort','gramatica.py',568),
  ('acceso_array_expresion -> ID dimensiones','acceso_array_expresion',2,'p_acceso_array','gramatica.py',573),
  ('tipo_funcion -> INT','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',584),
  ('tipo_funcion -> STRING_TYPE','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',585),
  ('tipo_funcion -> BOOLEAN','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',586),
  ('tipo_funcion -> VOID','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',587),
  ('tipo_funcion -> FLOAT','tipo_funcion',1,'p_tipo_retorno_funcion','gramatica.py',588),
  ('tipo_dato -> INT','tipo_dato',1,'p_tipo_dato','gramatica.py',603),
  ('tipo_dato -> STRING_TYPE','tipo_dato',1,'p_tipo_dato','gramatica.py',604),
  ('tipo_dato -> BOOLEAN','tipo_dato',1,'p_tipo_dato','gramatica.py',605),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato','gramatica.py',606),
]
