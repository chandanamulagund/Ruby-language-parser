import ply.lex as lex
import ply.yacc as yacc
import argparse
reserved={
'for':'for','do':'do','end':'end','in':'in'
}
tokens=[
    'EQUAL',
    'NUMBER',
    'ID',
    'RANGE',
    'PLUS',
    'MINUS',
    'DOT',
    
]+list(reserved.values())

t_EQUAL=r'\='
t_PLUS=r'\+'
t_MINUS=r'\-'
t_ignore=' '
t_DOT =r'\.'

def t_NUMBER(t):
    r'\d+'
    t.value=int(t.value)
    return t
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno+=len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()

def p_start(p):
    's : f id i con d st e'
def p_for(p):
    'f : for'

def p_in(p):
    'i : in'
def p_do(p):
    'd : do'
def p_e(p):
    'e : end'
def p_dot(p):
    'dot : DOT'
def p_st1(p):
    'st : id eq no '
def p_st2(p):
    'st : id eq id '
def p_st3(p):
    'st : s'
def p_st4(p):
 'st : id pl pl'

def p_st5(p):
 'st : pl pl id  '

def p_st6(p):
 'st : id mi mi '

def p_st7(p):
 'st : mi mi id '

def p_id(p):
    'id : ID'
def p_eq(p):
    'eq : EQUAL'
def p_no(p):
    'no : NUMBER'
def p_con(p):
    'con : no dot dot no'
def p_pl(p):
 'pl : PLUS'
def p_plm(p):
 'mi : MINUS'

def p_error(t):
    if(t):
        print("Syntax error at %s" %t.value)
    else:
        print("Syntax error: missing token")
parser = yacc.yacc()
while True:
    try:
        s = input('\nEnter the command:  ')
        if s=='exit':
            print("\n")
            break
    except EOFError:
        break
    parser.parse(s)