#G={V,T,P,S}
#V={s,condition,statement}
#T={while,ID,Number,=,{,},(,),;,<=,>=}
#S=s
#P=productions
#s->while(condition){statement}
#condition->ID==ID|Number==ID|ID==Number|Number==Number|ID<=Number|ID>=Number|ID<=ID|ID>=ID
#statement->ID=ID;|ID=Number;|ID++|s|statement

import ply.lex as lex
import ply.yacc as yacc


reserved={'while':'while'}

tokens=['EQUAL','NUMBER','ID','PLUS','LESS','MORE','MINUS']+list(reserved.values())

t_EQUAL=r'\='
t_PLUS=r'\+'
t_MINUS=r'\-'
t_LESS=r'\<'
t_MORE=r'\>'
t_ignore=' '

def t_NUMBER(t):
   r'\d+'
   t.value=int(t.value)
   return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,'ID')
    return t


def t_error(t):
 print("Illegal character '%s'" % t.value[0]) 
 t.lexer.skip(1)

lexer = lex.lex()

def p_s(p):
 's : w con st '

def p_w(p):
 'w : while'

def p_con1(p):
 'con : id eq eq id' 
def p_con2(p):
 'con : id eq eq no' 
def p_con3(p):
 'con : no eq eq id' 
def p_con4(p):
 'con : no eq eq no' 
def p_con5(p):
 'con : id le eq no' 
def p_con6(p):
 'con : id gr eq no' 
def p_con7(p):
 'con : id le eq id' 
def p_con8(p):
 'con : id gr eq id' 
def p_con9(p):
    'con : id pl eq id'
def p_con10(p):
    'con : id pl eq no'

def p_id(p):
 'id : ID'

def p_eq(p):
 'eq : EQUAL'

def p_no(p):
 'no : NUMBER'

def p_st1(p):
 'st : id eq no st'

def p_st2(p):
 'st : id eq id  st'

def p_st3(p):
 'st : s'

def p_st4(p):
 'st : id pl pl st'
def p_st5(p):
 'st : pl pl id st'
def p_st6(p):
 'st : id mi mi st'
def p_st7(p):
 'st : mi mi id st'
def p_pl(p):
 'pl : PLUS'
def p_plm(p):
 'mi : MINUS'

def p_st8(p):
 'st : '

def p_gr(p):
 'gr : MORE'

def p_le(p):
 'le : LESS'

def p_error(t):
 if(t):
   print("Syntax error at %s" %t.value) 
 else:
   print("Syntax error: missing token")

parser = yacc.yacc()

while True:
 try:
   s = input('\nCommand > ')
   if s=='exit':
      print("\n")
      break
   else:
      parser.parse(s)
 except EOFError:
    break


