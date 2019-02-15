import ply.yacc as yacc
import lexer
tokens = lexer.tokens

def p_expr(p):
		'''expr : IDENTIFIER OP_ASGN expr
			    | expr DOT IDENTIFIER PARAN_OPEN argument_list_opt PARAN_CLOSE	 
			    | expr AT TYPE DOT IDENTIFIER  PARAN_OPEN argument_list_opt PARAN_CLOSE
			    | conditionals
			    | loop
			    | block_expr
			    | let_expr
			    | NEW TYPE
			    | ISVOID expr
			    | return_statement
			    | break_statement
			    | continue_statement
			    | expr OP_ARITHMETIC_B expr
			    | expr
			    | expr OP_ARITHMETIC_U expr
			    | expr OP_RELATIONAL expr
			    | expr expr OP_LOGICAL expr
			    | OP_ARITHMETIC_U expr
			    | PARAN_OPEN expr PARAN_CLOSE
			    | IDENTIFIER
			    | IDENTIFIER ARRAY_OPEN expr ARRAY_CLOSE
			    | TRUE
			    | FALSE
			    | NUMBER
			    | STRING
		'''

def p_conditionals(p):
	'''	conditionals : case 
					 | if_then_else
	'''

def p_loop(p):
	''' loop : loop while 
			 | for 
			 | do_while
	'''

def p_argument_list_opt(p):
	''' argument_list_opt : argument_list 
	   					   | empty
	'''

def p_argument_list(p):
	''' argument_list : argument_list COMMA expr
					  |  expr
	'''

def p_case(p):
	''' case : CASE expr OF actions ESAC
	'''

def p_actions(p):
	''' actions : action 
				| action actions
	'''

def p_action(p):
	''' action : IDENTIFIER COLON TYPE OP_IMPLIES expr
	'''

def p_if_then_else(p):
	''' if_then_else : IF expr THEN expr ELSE expr FI
	'''

def p_while(p): 
	''' while : WHILE expr LOOP expr POOL
	'''

def p_for(p):
	''' for : FOR PARAN_OPEN expr STMT_TERMINATOR expr STMT_TERMINATOR expr PARAN_CLOSE LOOP expr POOL
	'''

def p_do_while(p):
	''' do_while : DO LOOP expr POOL WHILE expr
	'''

def p_break_statement(p):
	''' break_statement : BREAK
	'''

def p_continue_statement(p):
	''' continue_statement : CONTINUE
	'''
def p_return_statement(p):
	''' return_statement : RETURN
	'''

def p_block_expr(p):
	''' block_expr : PARAN_OPEN block_list PARAN_OPEN 
	'''

def p_block_list(p):
	''' block_list : block_list expr STMT_TERMINATOR
				   | expr STMT_TERMINATOR
	'''

# def p_let_expr(p):
# 	''' let_expr : LET formal COMMA formal IN expr
# 	'''

def p_let_expr(p):
	''' let_expr : LET'''
def p_empty(p):
	''' empty : 
	'''

print(tokens)

parser = yacc.yacc()

for x in args:
	if (x.startswith("--inp=")):
		input_file_name = x[6:]
		# print(config_file_name)
	if (x.startswith("--output=")):
		html_name = x[9:]

input_file = open(input_file_name,'r')
input_str = input_file.read()

parser.parse(input_str)