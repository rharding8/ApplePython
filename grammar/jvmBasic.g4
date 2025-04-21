// $antlr-format alignTrailingComments true, columnLimit 150, minEmptyLines 1, maxEmptyLinesToKeep 1, reflowComments false, useTab false
// $antlr-format allowShortRulesOnASingleLine false, allowShortBlocksOnASingleLine true, alignSemicolons hanging, alignColons hanging

grammar jvmBasic;

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
*/ // a program is a collection of lines
prog
    : line+ EOF
    ;

// a line starts with an INT
line
    : linenumber (amprstmt (COLON amprstmt?)*)
    ;

amperoper
    : AMPERSAND
    ;

linenumber
    : NUMBER
    ;

amprstmt
    : amperoper? statement
    | COMMENT
    | REM
    ;

statement
    : CLS # ClearStatement
    //| LOAD
    | SAVE # SaveStatement
    //| TRACE
    //| NOTRACE
    | FLASH # FlashStatement
    | INVERSE # InverseStatement
    //| GR
    | NORMAL # NormalStatement
    | SHLOAD # SHLoadStatement
    //| CLEAR
    //| RUN
    | STOP # StopStatement
    //| TEXT
    | HOME # HomeStatement
    //| HGR
    //| HGR2
    | endstmt # EndStatement
    | returnstmt # ReturnStatement
    | restorestmt # RestoreStatement
    | amptstmt # AmptStatement
    | popstmt # PopStatement
    //| liststmt
    | storestmt # StoreStatement
    | getstmt # GetStatement
    | recallstmt # RecallStatement
    | nextstmt # NextStatement
    //| instmt
    //| prstmt
    //| onerrstmt
    //| hlinstmt
    //| vlinstmt
    //| colorstmt
    | speedstmt # SpeedStatement
    | scalestmt # ScaleStatement
    | rotstmt # RotStatement
    //| hcolorstmt
    | himemstmt # HimemStatement
    | lomemstmt # LomemStatement
    | printstmt1 # PrintStatement
    //| pokestmt
    //| plotstmt
    | ongotostmt # OnGotoStatement
    | ongosubstmt # OnGosubStatement
    | ifstmt # IfStatement
    | forstmt1 # ForStatementIn
    | forstmt2 # ForStatementOut
    | inputstmt # InputStatement
    | tabstmt # TabStatement
    | dimstmt # DimStatement
    | gotostmt # GotoStatement
    | gosubstmt # GosubStatement
    | callstmt # CallStatement
    | readstmt # ReadStatement
    //| hplotstmt
    //| vplotstmt
    | vtabstmnt # VTabStatement
    | htabstmnt # HTabStatement
    | waitstmt # WaitStatement
    | datastmt # DataStatement
    | xdrawstmt # XDrawStatement
    | drawstmt # DrawStatement
    | defstmt # DefStatement
    | letstmt # LetStatement
    | includestmt # IncludeStatement
    ;

vardecl
    : var_ (LPAREN exprlist RPAREN)*
    ;

printstmt1
    : (PRINT | QUESTION) printlist?
    ;

printlist
    : expression (separator=(COMMA | SEMICOLON) expression?)*
    ;

getstmt
    : GET exprlist
    ;

letstmt
    : LET? variableassignment
    ;

variableassignment
    : vardecl EQ exprlist
    ;

ifstmt
    : IF expression THEN? (statement | linenumber)
    ;

// for stmt 1 puts the for-next on one line
forstmt1
    : FOR vardecl EQ expression TO expression (STEP expression)? (statement NEXT vardecl?)?
    ;

// for stmt 2 puts the for, the statment, and the next on 3 lines.  It needs "nextstmt"
forstmt2
    : FOR vardecl EQ expression TO expression (STEP expression)?
    ;

nextstmt
    : NEXT (vardecl (',' vardecl)*)?
    ;

inputstmt
    : INPUT (STRINGLITERAL separator=(COMMA | SEMICOLON))? varlist
    ;

readstmt
    : READ varlist
    ;

dimstmt
    : DIM varlist
    ;

gotostmt
    : GOTO linenumber
    ;

gosubstmt
    : GOSUB expression
    ;

/*pokestmt
    : POKE expression COMMA expression
    ;*/

callstmt
    : CALL exprlist
    ;

/*hplotstmt
    : HPLOT (expression COMMA expression)? (TO expression COMMA expression)*
    ;

vplotstmt
    : VPLOT (expression COMMA expression)? (TO expression COMMA expression)*
    ;*/

/*plotstmt
    : PLOT expression COMMA expression
    ;*/

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
    ;

datastmt
    : DATA datum (COMMA datum?)*
    ;

datum
    : number
    | STRINGLITERAL
    ;

waitstmt
    : WAIT expression COMMA expression (COMMA expression)?
    ;

xdrawstmt
    : XDRAW expression (AT expression COMMA expression)?
    ;

drawstmt
    : DRAW expression (AT expression COMMA expression)?
    ;

defstmt
    : DEF FN? var_ LPAREN var_ RPAREN EQ expression
    ;

tabstmt
    : TAB LPAREN expression RPAREN
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

/*colorstmt
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
    ;*/

storestmt
    : STORE vardecl
    ;

recallstmt
    : RECALL vardecl
    ;

/*liststmt
    : LIST expression?
    ;*/

popstmt
    : POP (expression COMMA expression)?
    ;

amptstmt
    : AMPERSAND expression
    ;

includestmt
    : INCLUDE expression
    ;

endstmt
    : END
    ;

returnstmt
    : RETURN
    ;

restorestmt
    : RESTORE
    ;

// expressions and such
number
    : ('+' | '-')? (NUMBER | FLOAT)
    ;

func_
    : STRINGLITERAL # StringLiteralFunction
    | number # NumberFunction
    | tabfunc # TabFunction
    | vardecl # DeclarationFunction
    | chrfunc # CharacterFunction
    | sqrfunc # SquareRootFunction
    | lenfunc # LengthFunction
    | strfunc # StringFunction
    | ascfunc # AsciiFunction
    | scrnfunc # ScreenFunction
    | midfunc # MidFunction
    //| pdlfunc
    //| peekfunc
    | intfunc # IntegerFunction
    | spcfunc # SpcFunction
    | frefunc # FreFunction
    | posfunc # PosFunction
    | usrfunc # UserFunction
    | leftfunc # LeftFunction
    | valfunc # ValueFunction
    | rightfunc # RightFunction
    | fnfunc # FnFunction
    | sinfunc # SinFunction
    | cosfunc # CosFunction
    | tanfunc # TanFunction
    | atnfunc # AtnFunction
    | rndfunc # RandFunction
    | sgnfunc # SignFunction
    | expfunc # ExponentialFunction
    | logfunc # LogFunction
    | absfunc # AbsoluteFunction
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

varlist
    : vardecl (COMMA vardecl)*
    ;

exprlist
    : expression (COMMA expression)*
    ;

// functions
sqrfunc
    : SQR LPAREN expression RPAREN
    ;

chrfunc
    : CHR LPAREN expression RPAREN
    ;

lenfunc
    : LEN LPAREN expression RPAREN
    ;

ascfunc
    : ASC LPAREN expression RPAREN
    ;

midfunc
    : MID LPAREN expression COMMA expression COMMA expression RPAREN
    ;

/*pdlfunc
    : PDL LPAREN expression RPAREN
    ;*/

/*peekfunc
    : PEEK LPAREN expression RPAREN
    ;*/

intfunc
    : INTF LPAREN expression RPAREN
    ;

spcfunc
    : SPC LPAREN expression RPAREN
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

leftfunc
    : LEFT LPAREN expression COMMA expression RPAREN
    ;

rightfunc
    : RIGHT LPAREN expression COMMA expression RPAREN
    ;

strfunc
    : STR LPAREN expression RPAREN
    ;

fnfunc
    : FN var_ LPAREN expression RPAREN
    ;

valfunc
    : VAL LPAREN expression RPAREN
    ;

scrnfunc
    : SCRN LPAREN expression COMMA expression RPAREN
    ;

sinfunc
    : SIN LPAREN expression RPAREN
    ;

cosfunc
    : COS LPAREN expression RPAREN
    ;

tanfunc
    : TAN LPAREN expression RPAREN
    ;

atnfunc
    : ATN LPAREN expression RPAREN
    ;

rndfunc
    : RND LPAREN expression RPAREN
    ;

sgnfunc
    : SGN LPAREN expression RPAREN
    ;

expfunc
    : EXP LPAREN expression RPAREN
    ;

logfunc
    : LOG LPAREN expression RPAREN
    ;

absfunc
    : ABS LPAREN expression RPAREN
    ;

tabfunc
    : TAB LPAREN expression RPAREN
    ;

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

CALL
    : 'CALL'
    ;

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
    ;*/

VTAB
    : 'VTAB'
    ;

HTAB
    : 'HTAB'
    ;

HOME
    : 'HOME'
    ;

ON
    : 'ON'
    ;

/*PDL
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

HIMEM
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

/*ONERR
    : 'ONERR'
    ;*/

SPC
    : 'SPC'
    ;

FRE
    : 'FRE'
    ;

POS
    : 'POS'
    ;

USR
    : 'USR'
    ;

/*TRACE
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

WAIT
    : 'WAIT'
    ;

READ
    : 'READ'
    ;

XDRAW
    : 'XDRAW'
    ;

DRAW
    : 'DRAW'
    ;

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

SPEED
    : 'SPEED'
    ;

ROT
    : 'ROT'
    ;

SCALE
    : 'SCALE'
    ;

/*COLOR
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
    ;*/

SCRN
    : 'SCRN'
    ;

POP
    : 'POP'
    ;

SHLOAD
    : 'SHLOAD'
    ;

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

STORE
    : 'STORE'
    ;

RECALL
    : 'RECALL'
    ;

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

SAVE
    : 'SAVE'
    ;

/*LOAD
    : 'LOAD'
    ;
*/
QUESTION
    : '?'
    ;

INCLUDE
    : 'INCLUDE'
    ;

CLS
    : 'CLS'
    ;

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