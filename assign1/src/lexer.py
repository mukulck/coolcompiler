import ply.lex as lex

keywords = ['class', 'else', 'false', 'fi', 'if', 'in', 'inherits', 'isvoid', 'let', 'loop', 'pool', 'then', 'while',
'case', 'esac', 'new', 'of', 'not', 'true']
tokens = [ 'IDENTIFIER','TYPE','OP_ASGN','OP_IMPLIES','STRING',
           'SL_COMMENT', 'ML_COMMENT', 'COLON','STMT_TERMINATOR','AT','DOT','DOTSTAR','COMMA','BLOCK_BEGIN','BLOCK_END','PARAN_CLOSE',
           'PARAN_OPEN','ARRAY_OPEN','ARRAY_CLOSE','OP_ARITHMETIC_U','OP_ARITHMETIC_B','OP_RELATIONAL','OP_LOGICAL','OP_BITWISE''NUMBER','NEWLINE'] + keywords
t_IDENTIFIER		=	r'[a-z][a-zA-Z0-9_]*'
t_TYPE				=	r'[A-Z][a-zA-Z0-9_]*'
t_OP_ASGN 			=   r"<-"
t_OP_IMPLIES 		=	r"=>"
t_STRING			=	r'\"(\\.|[^\\"])*\"'
t_SL_COMMENT		=	r'"--"(.)*'
t_ML_COMMENT		=	r'"(*"([^*]|[\n]|(\*+([^*\)]|[\n])))*\*+")"'
t_COLON				=   r":"
t_STMT_TERMINATOR  	= 	r";"
t_AT				= 	r"@"
t_DOT				= 	r"."
t_DOTSTAR			= 	r".*"
t_COMMA				= 	r","
t_BLOCK_BEGIN 		= 	r"{"
t_BLOCK_END 		=   r"}"
t_PARAN_OPEN		=   r"("
t_PARAN_CLOSE		=   r")"
t_ARRAY_OPEN		=   r"["
t_ARRAY_CLOSE 		=   r"]"
t_OP_ARITHMETIC_U	=   r"~"
t_OP_ARITHMETIC_B	=   r'[+-/*]'
t_OP_RELATIONAL		=   r'(<|<=|=|>=|>)'
t_OP_LOGICAL		=   r'(&&|\|\|)'
t_OP_BITWISE		=   r'(&|\||^)'
t_NEWLINE			= 	r'\n'
t_NUMBER			=	r'[0-9]+'
t_ignore			=	r' |\t|\n|\f|\v|\r'
lex.lex()         # Build the lexer


