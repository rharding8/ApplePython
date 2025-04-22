ANTLR = antlr-4.13.2-complete.jar

all: pyBasic.py

pyBasic.py: pyBasic.g4 $(ANTLR)
	CLASSPATH=$(ANTLR):$(CLASSPATH) java org.antlr.v4.Tool -Dlanguage=Python3 -visitor $<

$(ANTLR):
	wget https://www.antlr.org/download/$(ANTLR)

clean:
	rm -f pyBasic.interp pyBasicLexer.interp pyBasicLexer.py pyBasicLexer.tokens pyBasicListener.py pyBasicVisitor.py pyBasicParser.py pyBasic.tokens

clobber: clean
	rm -f $(ANTLR)