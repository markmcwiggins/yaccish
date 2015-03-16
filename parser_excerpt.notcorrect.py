
#
# the 'docstrings' have the top-down specification ... a program is a mainclass + a classlist, and down from there
#
#  This is a piece of a larger Python module and won't compile/run as Python

def p_program(p):
    'program : mainclass classlist'
    p[0] = program(p[1],p[2])
    prettyprint(p[0])

def p_mainclasshdr(p):
    'mainclasshdr :  CLASS IDENTIFIER LBRACE PUBLIC STATIC VOID MAIN LPAREN STRING LBRACK RBRACK IDENTIFIER RPAREN LBRACE'
    p[0] = mainclass(p[2],p[12])
    

def p_mainclass(p):
    'mainclass : mainclasshdr stmtlist  RBRACE RBRACE'
    p[0] = p[1]
    p[0].stmtlist = p[2]
    #prettyprint(p[0])

def p_classlist(p):
    '''classlist : empty
                 | classlist class'''
    try:
        p[1].append(p[2])
        p[0] = p[1]
    except:
        p[0] = classlist()


def p_class(p):
    'class : CLASS IDENTIFIER optextends LBRACE vardecllist methoddecllist RBRACE'
    p[0] = classstmt(p[2],p[3],p[5],p[6])
    #prettyprint(p[0])

def p_optextends(p):
    '''optextends : empty
                  | EXTENDS IDENTIFIER'''
    try:
        p[0] = p[2]
    except:
        p[0] = p[1]


def p_methodheader(p):
    'methodheader : PUBLIC type IDENTIFIER LPAREN optparamlist RPAREN'
    p[0] = methoddecl(p[3],p[2],p[5])


def p_methoddecl(p):
    'methoddecl : methodheader LBRACE vardecllist stmtlist RBRACE'
    p[0] = p[1]
    p[0].decls = p[3]
    p[0].stmts = p[4]
#    prettyprint(p[0])
#    prettyprint(p[8])
#    prettyprint(p[9])

def p_optarglist(p):
    '''optarglist : arglist
                  | empty'''
    p[0] = p[1]

def p_optparamlist(p):
    '''optparamlist : paramlist
                  | empty'''
    p[0] = p[1]


def p_param(p):
    '''param     : type IDENTIFIER'''
    debug( "type = " + p[1])
    p[0] = param(p[1],p[2])

def p_paramlist(p):
    '''paramlist : param
                 | paramlist COMMA param'''
    try:
        p[0] = p[1]
        p[0].append(p[3])
    except:
        p[0] = [p[1]]


def p_stmtlist(p):
    '''stmtlist : statements
                | empty'''
    p[0] =  stmtlist(p[1])

def p_statements(p):
    '''statements : statement
                | statements statement'''
    try:
        p[1].append(p[2])
        p[0] = p[1]
    except:
        p[0] = [p[1]]

def p_block(p):
    '''block : statement
             | LBRACE statements RBRACE'''
    try:
        p[0] = p[2]
    except:
        p[0] = [p[1]]

def p_arglist(p):
    '''arglist : expr
               | arglist COMMA expr'''
    try:
        p[1].append(p[3]) #expr(COMMA,p[1],p[3])
        p[0] = p[1]
    except:
        p[0] = [p[1]]

def p_vardecl(p):
    'vardecl : type IDENTIFIER SEMI'
#    types[p[2]] = p[1]
    p[0] = vardecl(p[1],p[2])

def p_vardecl_error(p):
    'evardecl : type error SEMI'
#    print "Syntax error in initialization, line " + p[0].line 

def p_vardecllist(p):
    '''vardecllist : empty
                   | vardecllist vardecl
                   | vardecllist evardecl'''
    try:
        p[1].append(p[2])
        p[0] = p[1]
    except:
        p[0] = [p[1]]
           


def p_methoddecllist(p):
    '''methoddecllist : empty
                   | methoddecllist methoddecl'''
    try:
        p[1].append(p[2])
        p[0] = p[1]
    except:
        p[0] = [p[1]]

def p_stmt(p):
    '''statement : ifstmt
                 | whilestmt
                 | printstmt
                 | assignstmt
                 | returnstmt
                 | arrayassignstmt
                 | einit'''
    p[0] = p[1]
