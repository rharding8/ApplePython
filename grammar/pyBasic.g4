// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

grammar pyBasic;

options {
    caseInsensitive = true;
}

/*
[The "BSD licence"]
Copyright (c) 2012 Tom Everett
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:
1. Redistributions of source code must retain the above copyright
notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.
3. The name of the author may not be used to endorse or promote products
derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

// Modified to suit AppleSoft BASIC, and for better ANTLR Python Integration, by Ryan Harding

// a program is a collection of lines
prog
    : line+ EOF
    ;

// a line starts with an INT
line
    : linenumber (amprstmt (COLON amprstmt?)*)
    ;

linenumber
    : NUMBER
    ;

amprstmt
    : AMPERSAND? statement # AmperStatement
    | COMMENT # CommentStatement
    | REM # RemStatement
    ;

statement
    : HOME # HomeStatement
    //| CLS # ClearStatement
    //| LOAD # LoadStatement
    //| SAVE # SaveStatement
    //| TRACE
    //| NOTRACE
    //| FLASH # FlashStatement
    //| INVERSE # InverseStatement
    //| GR
    //| NORMAL # NormalStatement
    //| SHLOAD # SHLoadStatement
    //| CLEAR
    //| RUN
    | STOP # StopStatement
    //| TEXT
    //| HGR
    //| HGR2
    | END # EndStatement
    | RETURN # ReturnStatement
    | RESTORE # RestoreStatement
    //| amptstmt # AmptStatement
    //| popstmt # PopStatement
    //| liststmt
    //| storestmt # StoreStatement
    | GET expression (COMMA expression)* # GetStatement
    //| recallstmt # RecallStatement
    | NEXT (vardecl (',' vardecl)*)? # NextStatement
    //| instmt
    //| prstmt
    //| onerrstmt
    //| hlinstmt
    //| vlinstmt
    //| colorstmt
    //| speedstmt # SpeedStatement
    //| scalestmt # ScaleStatement
    //| rotstmt # RotStatement
    //| hcolorstmt
    //| himemstmt # HimemStatement
    //| lomemstmt # LomemStatement
    | (PRINT | QUESTION) printlist? # PrintStatement
    //| pokestmt
    //| plotstmt
    //| ongotostmt # OnGotoStatement
    //| ongosubstmt # OnGosubStatement
    | IF expression THEN? (statement | linenumber) # IfStatement
    | FOR vardecl EQ expression TO expression (STEP expression)? (statement NEXT vardecl?)? # InLineForStatement
    | FOR vardecl EQ expression TO expression (STEP expression)? # ForStatement
    | INPUT (STRINGLITERAL separator=(COMMA | SEMICOLON))? vardecl (COMMA vardecl)* # InputStatement
    | TAB LPAREN expression RPAREN # TabStatement
    | DIM vardecl (COMMA vardecl)* # DimStatement
    | GOTO linenumber # GotoStatement
    | GOSUB expression # GosubStatement
    //| callstmt # CallStatement
    | READ vardecl (COMMA vardecl)* # ReadStatement
    //| hplotstmt
    //| vplotstmt
    //| vtabstmnt # VTabStatement
    //| htabstmnt # HTabStatement
    //| waitstmt # WaitStatement
    | DATA datum (COMMA datum?)* # DataStatement
    //| xdrawstmt # XDrawStatement
    //| drawstmt # DrawStatement
    | DEF FN? var_ LPAREN var_ RPAREN EQ expression # DefStatement
    | LET? vardecl EQ expression (COMMA expression)* # LetStatement
    //| includestmt # IncludeStatement
    ;

vardecl
    : var_ (LPAREN expression (COMMA expression)* RPAREN)*
    ;

printlist
    : expression (printseparator expression?)*
    ;

printseparator
    : op=(COMMA
    | SEMICOLON)
    ;

/*pokestmt
    : POKE expression COMMA expression
    ;

callstmt
    : CALL exprlist
    ;

hplotstmt
    : HPLOT (expression COMMA expression)? (TO expression COMMA expression)*
    ;

vplotstmt
    : VPLOT (expression COMMA expression)? (TO expression COMMA expression)*
    ;

plotstmt
    : PLOT expression COMMA expression
    ;

ongotostmt
    : ON expression GOTO linenumber (COMMA linenumber)*
    ;

ongosubstmt
    : ON expression GOSUB linenumber (COMMA linenumber)*
    ;

vtabstmnt
    : VTAB expression
    ;

htabstmnt
    : HTAB expression
    ;

himemstmt
    : HIMEM COLON expression
    ;

lomemstmt
    : LOMEM COLON expression
    ;*/

datum
    : number
    | STRINGLITERAL
    ;

/*waitstmt
    : WAIT expression COMMA expression (COMMA expression)?
    ;

xdrawstmt
    : XDRAW expression (AT expression COMMA expression)?
    ;

drawstmt
    : DRAW expression (AT expression COMMA expression)?
    ;

speedstmt
    : SPEED EQ expression
    ;

rotstmt
    : ROT EQ expression
    ;

scalestmt
    : SCALE EQ expression
    ;

colorstmt
    : COLOR EQ expression
    ;

hcolorstmt
    : HCOLOR EQ expression
    ;*/

/*hlinstmt
    : HLIN expression COMMA expression AT expression
    ;

vlinstmt
    : VLIN expression COMMA expression AT expression
    ;*/

/*onerrstmt
    : ONERR GOTO linenumber
    ;

prstmt
    : PRNUMBER NUMBER
    ;

instmt
    : INNUMBER NUMBER
    ;

storestmt
    : STORE vardecl
    ;

recallstmt
    : RECALL vardecl
    ;

liststmt
    : LIST expression?
    ;

popstmt
    : POP (expression COMMA expression)?
    ;

amptstmt
    : AMPERSAND expression
    ;

includestmt
    : INCLUDE expression
    ;*/

// expressions and such
number
    : ('+' | '-')? (NUMBER | FLOAT)
    ;

func_
    : STRINGLITERAL # StringLiteralFunction
    | number # NumberFunction
    | TAB LPAREN expression RPAREN # TabFunction
    | vardecl # DeclarationFunction
    | CHR LPAREN expression RPAREN # CharacterFunction
    | SQR LPAREN expression RPAREN # SquareRootFunction
    | LEN LPAREN expression RPAREN # LengthFunction
    | STR LPAREN expression RPAREN # StringFunction
    | ASC LPAREN expression RPAREN # AsciiFunction
    //| scrnfunc # ScreenFunction
    | MID LPAREN expression COMMA expression COMMA expression RPAREN # MidFunction
    //| pdlfunc
    //| peekfunc
    | INTF LPAREN expression RPAREN # LargestIntegerFunction
    | SPC LPAREN expression RPAREN # SpcFunction
    //| frefunc # FreFunction
    //| posfunc # PosFunction
    //| usrfunc # UserFunction
    | LEFT LPAREN expression COMMA expression RPAREN # LeftFunction
    | VAL LPAREN expression RPAREN # ValueFunction
    | RIGHT LPAREN expression COMMA expression RPAREN # RightFunction
    | FN var_ LPAREN expression RPAREN # FnFunction
    | SIN LPAREN expression RPAREN # SinFunction
    | COS LPAREN expression RPAREN # CosFunction
    | TAN LPAREN expression RPAREN # TanFunction
    | ATN LPAREN expression RPAREN # ArcTanFunction
    | RND LPAREN expression RPAREN # RandFunction
    | SGN LPAREN expression RPAREN # SignFunction
    | EXP LPAREN expression RPAREN # ExpFunction
    | LOG LPAREN expression RPAREN # NaturalLogFunction
    | ABS LPAREN expression RPAREN # AbsoluteFunction
    | LPAREN expression RPAREN # ParentheticalFunction
    ;

signExpression
    : NOT? (PLUS | MINUS)? func_
    ;

exponentExpression
    : signExpression (EXPONENT signExpression)*
    ;

multiplyingExpression
    : exponentExpression (op=(TIMES | DIV) exponentExpression)*
    ;

addingExpression
    : multiplyingExpression (op=(PLUS | MINUS) multiplyingExpression)*
    ;

relationalExpression
    : addingExpression (op=(GTE | LTE | NEQ | EQ | GT | LT) addingExpression)?
    ;

expression
    : func_
    | relationalExpression (op=(AND | OR) relationalExpression)*
    ;

// lists
var_
    : varname suffix=varsuffix?
    ;

varname
    : LETTERS (LETTERS | NUMBER)*
    ;

varsuffix
    : DOLLAR
    | PERCENT
    ;

// functions

/*pdlfunc
    : PDL LPAREN expression RPAREN
    ;

peekfunc
    : PEEK LPAREN expression RPAREN
    ;

frefunc
    : FRE LPAREN expression RPAREN
    ;

posfunc
    : POS LPAREN expression RPAREN
    ;

usrfunc
    : USR LPAREN expression RPAREN
    ;

scrnfunc
    : SCRN LPAREN expression COMMA expression RPAREN
    ;*/

DOLLAR
    : '$'
    ;

PERCENT
    : '%'
    ;

RETURN
    : 'RETURN'
    ;

PRINT
    : 'PRINT'
    ;

GOTO
    : 'GOTO'
    ;

GOSUB
    : 'GOSUB'
    ;

IF
    : 'IF'
    ;

NEXT
    : 'NEXT'
    ;

THEN
    : 'THEN'
    ;

REM
    : 'REM'
    ;

CHR
    : 'CHR$'
    ;

MID
    : 'MID$'
    ;

LEFT
    : 'LEFT$'
    ;

RIGHT
    : 'RIGHT$'
    ;

STR
    : 'STR$'
    ;

LPAREN
    : '('
    ;

RPAREN
    : ')'
    ;

PLUS
    : '+'
    ;

MINUS
    : '-'
    ;

TIMES
    : '*'
    ;

DIV
    : '/'
    ;

/*CLEAR
    : 'CLEAR'
    ;*/

GTE
    : '>= '
    | '=>'
    ;

LTE
    : '<='
    | '=<'
    ;

GT
    : '>'
    ;

LT
    : '<'
    ;

COMMA
    : ','
    ;

/*LIST
    : 'LIST'
    ;*/

/*RUN
    : 'RUN'
    ;*/

END
    : 'END'
    ;

LET
    : 'LET'
    ;

EQ
    : '='
    ;

NEQ
    : '<>'
    | '><'
    ;

FOR
    : 'FOR'
    ;

TO
    : 'TO'
    ;

STEP
    : 'STEP'
    ;

INPUT
    : 'INPUT'
    ;

SEMICOLON
    : ';'
    ;

DIM
    : 'DIM'
    ;

SQR
    : 'SQR'
    ;

COLON
    : ':'
    ;

/*TEXT
    : 'TEXT'
    ;*/

/*HGR
    : 'HGR'
    ;

HGR2
    : 'HGR2'
    ;*/

LEN
    : 'LEN'
    ;

/*CALL
    : 'CALL'
    ;*/

ASC
    : 'ASC'
    ;

/*HPLOT
    : 'HPLOT'
    ;

VPLOT
    : 'VPLOT'
    ;

PRNUMBER
    : 'PR#'
    ;

INNUMBER
    : 'IN#'
    ;

VTAB
    : 'VTAB'
    ;

HTAB
    : 'HTAB'
    ;*/

HOME
    : 'HOME'
    ;

/*ON
    : 'ON'
    ;

PDL
    : 'PDL'
    ;*/

/*PLOT
    : 'PLOT'
    ;*/

/*PEEK
    : 'PEEK'
    ;

POKE
    : 'POKE'
    ;*/

INTF
    : 'INT'
    ;

STOP
    : 'STOP'
    ;

/*HIMEM
    : 'HIMEM'
    ;

LOMEM
    : 'LOMEM'
    ;

FLASH
    : 'FLASH'
    ;

INVERSE
    : 'INVERSE'
    ;

NORMAL
    : 'NORMAL'
    ;

ONERR
    : 'ONERR'
    ;*/

SPC
    : 'SPC'
    ;

/*FRE
    : 'FRE'
    ;

POS
    : 'POS'
    ;

USR
    : 'USR'
    ;

TRACE
    : 'TRACE'
    ;

NOTRACE
    : 'NOTRACE'
    ;*/

AND
    : 'AND'
    ;

OR
    : 'OR'
    ;

DATA
    : 'DATA'
    ;

/*WAIT
    : 'WAIT'
    ;*/

READ
    : 'READ'
    ;

/*XDRAW
    : 'XDRAW'
    ;

DRAW
    : 'DRAW'
    ;*/

AT
    : 'AT'
    ;

DEF
    : 'DEF'
    ;

FN
    : 'FN'
    ;

VAL
    : 'VAL'
    ;

TAB
    : 'TAB'
    ;

/*SPEED
    : 'SPEED'
    ;

ROT
    : 'ROT'
    ;

SCALE
    : 'SCALE'
    ;

COLOR
    : 'COLOR'
    ;

HCOLOR
    : 'HCOLOR'
    ;*/

/*HLIN
    : 'HLIN'
    ;

VLIN
    : 'VLIN'
    ;

SCRN
    : 'SCRN'
    ;

POP
    : 'POP'
    ;

SHLOAD
    : 'SHLOAD'
    ;*/

SIN
    : 'SIN'
    ;

COS
    : 'COS'
    ;

TAN
    : 'TAN'
    ;

ATN
    : 'ATN'
    ;

RND
    : 'RND'
    ;

SGN
    : 'SGN'
    ;

EXP
    : 'EXP'
    ;

LOG
    : 'LOG'
    ;

ABS
    : 'ABS'
    ;

/*STORE
    : 'STORE'
    ;

RECALL
    : 'RECALL'
    ;*/

GET
    : 'GET'
    ;

EXPONENT
    : '^'
    ;

AMPERSAND
    : '&'
    ;

/*GR
    : 'GR'
    ;*/

NOT
    : 'NOT'
    ;

RESTORE
    : 'RESTORE'
    ;

/*SAVE
    : 'SAVE'
    ;

LOAD
    : 'LOAD'
    ;
*/
QUESTION
    : '?'
    ;

/*INCLUDE
    : 'INCLUDE'
    ;

CLS
    : 'CLS'
    ;*/

COMMENT
    : REM ~ [\r\n]*
    ;

STRINGLITERAL
    : '"' ~ ["\r\n]* '"'
    ;

LETTERS
    : ('A' .. 'Z')+
    ;

NUMBER
    : ('0' .. '9')+ ('E' NUMBER)*
    ;

FLOAT
    : ('0' .. '9')* '.' ('0' .. '9')+ ('E' ('0' .. '9')+)*
    ;

WS
    : [ \r\n\t]+ -> channel (HIDDEN)
    ;