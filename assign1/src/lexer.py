import ply.lex as lex
import sys
reserved = {
    'class': 'CLASS',
    'inherits': 'INHERITS',
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'fi': 'FI',
    'while': 'WHILE',
    'loop': 'LOOP',
    'pool': 'POOL',
    'let': 'LET',
    'in': 'IN',
    'case': 'CASE',
    'of': 'OF',
    'esac': 'ESAC',
    'new': 'NEW',
    'isvoid': 'ISVOID',
    'for' : 'FOR',
    'true' : 'TRUE' , 
    'false' : 'FALSE',
    'not' : 'NOT',
    'do' : 'DO',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN'
}
tokens = ['IGNORE','IDENTIFIER','TYPE','OP_ASGN','OP_IMPLIES','STRING',
           'COMMENT', 'COLON','STMT_TERMINATOR','AT','COMMA','BLOCK_BEGIN','BLOCK_END','PARAN_CLOSE',
           'PARAN_OPEN','ARRAY_OPEN','ARRAY_CLOSE','OP_ARITHMETIC_U','OP_ARITHMETIC_B','OP_RELATIONAL','OP_LOGICAL','NUMBER','NEWLINE','DOT'] + list(reserved.values())
t_OP_ASGN 			=   r"<-"
t_OP_IMPLIES 		=	r"=>"
t_STRING			=	r'\"(\\.|[^\\"])*\"'
t_COMMENT		=	r'--[^\n]+\n|\(\*[^(\*\))]+\*\)'
t_COLON				=   ":"
t_STMT_TERMINATOR  	= 	";"
t_AT				= 	"@"
t_DOT				= 	"\\."
t_COMMA				= 	","
t_BLOCK_BEGIN 		= 	"{"
t_BLOCK_END 		=   "}"
t_PARAN_OPEN		=   r"\("
t_PARAN_CLOSE		=   r"\)"
t_ARRAY_OPEN		=   r"\["
t_ARRAY_CLOSE 		=   r"\]"
t_OP_ARITHMETIC_U	=   r"~"
t_OP_ARITHMETIC_B	=   r'[+-/*]'
t_OP_RELATIONAL		=   r'(<|<=|=|>=|>)'
t_OP_LOGICAL		=   r'(&&|\|\|)'
# t_OP_BITWISE		=   r'(&|\||^)'
t_NEWLINE			= 	r'\n'
t_NUMBER			=	r'[0-9]+'
ignore = [' ']
t_ignore			=	''.join(ignore)
t_IGNORE			=	r'\t|\f|\r|\v'
# t_WHITE				= 	''.join(ignore)
def t_TYPE(t):
	r'[A-Z][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value.lower(),'TYPE')
	return t


def t_IDENTIFIER(t):
    r'[a-z][A-Za-z0-9_]*'
    t.type = reserved.get(t.value.lower(), 'IDENTIFIER')
    return t

lex.lex()         # Build the lexer

file_name = sys.argv[1]
fp = open(file_name)
data = fp.read()

 # Give the lexer some input
lex.input(data)
# print(sys.argv)
args = sys.argv
# print(args)
for x in args:
	if (x.startswith("--cfg=")):
		config_file_name = x[6:]
		# print(config_file_name)
	if (x.startswith("--output=")):
		html_name = x[9:]

config_file = open(config_file_name)
config_data = config_file.read().split('\n')
color_codes = []
color_types = []
# print(config_data)
for x in config_data:
	color_types.append(x.split(',')[0])
	if ','in x:
		color_codes.append(x.split(',')[1])
# print(color_types)
# print(color_codes)

Html_file= open(html_name,"w")

Html_file.write('<html>')
Html_file.write('<body>')
# Html_file.write('<h1>My First Heading</h1>')
Html_file.write('<p>')
 # Tokenize
para = ""
while True:
    tok = lex.token()
    print(tok)
    if not tok: 
        break      # No more input

    if(tok.type=='IGNORE' or tok.type=='NEWLINE'):
    	# print("ignore",tok.value)
    	if(tok.type=='NEWLINE'):
    		para = para + '<br/>'
    	if(tok.value=='\t'):
    		para = para + '&nbsp;'+'&nbsp;'+'&nbsp;'+'&nbsp;'+'&nbsp;'+'&nbsp;'+'&nbsp;'+'&nbsp;'
    for i in range(len(color_types)):
    	if(tok.type==color_types[i]):
    		# print(color_types[i]," ",color_codes[i]," ",tok.type)
    		# Html_file.write('tok.value')
    		para = para + "<span style=\"color:"+color_codes[i]+"\""+">"+ str(tok.value)+" " +"</span>"


Html_file.write(para)
Html_file.write('</p>')
Html_file.write('</body>')
Html_file.write('</html>')
Html_file.close()

# # print(sys.argv)
# args = sys.argv
# # print(args)
# for x in args:
# 	if (x.startswith("--cfg=")):
# 		config_file_name = x[6:]
# 		# print(config_file_name)
# 	if (x.startswith("--out=")):
# 		html_name = x[6:]