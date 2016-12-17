#!/usr/bin/env python

# ------------------------------------------------------------------------------
# msxasm.py is an MSX Assembler in Python
#
# Copyright (C) 2016 msxasmpy team <https://github.com/msxdev/msxasmpy>
#
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#  <http://www.apache.org/licenses/LICENSE-2.0>
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ------------------------------------------------------------------------------

import sys, argparse

### ply stuff start
if sys.version_info[0] >= 3:
    raw_input = input

sys.path.insert(0, 'ply-3.9')

tokens = (
    'NAME', 'NUMBER',
)

literals = ['=', '+', '-', '*', '/', '(', ')']

# Tokens

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lex.lex()

# Parsing rules

precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}


def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]


def p_statement_expr(p):
    'statement : expression'
    print(p[1])


def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]


def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]


def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

import ply.yacc as yacc
yacc.yacc(debug=True, write_tables=False)
### ply stuff end

def assemble(asmfile):
    print("Assembling \"%s\"" % asmfile)

    with open(asmfile, 'r') as f:
        s = f.read()
#    print(s)
    yacc.parse(s)

def main():
    app_name = __file__
    app_ver = "0.0.1"
    app_year = "2016"
    app_author = "msxasmpy team"
    app_url = "https://github.com/msxdev/msxasmpy"
    app_banner = "{name} {version} (C) {year} {author} {url}".format(
        name = app_name,
        version = app_ver,
        year = app_year,
        author = app_author,
        url = app_url
    )

    parser = argparse.ArgumentParser(description=app_banner)	# prog='PROG'
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + app_ver)
    parser.add_argument('inputfiles', metavar='file.asm', type=str, nargs='+',
        help='file to assemble')
    args = parser.parse_args()

    for inputfile in args.inputfiles:
        assemble(inputfile)

if __name__ == "__main__": main()
