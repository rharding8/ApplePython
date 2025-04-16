ANTLR = antlr-4.13.2-complete.jar

all: jvmBasic.py

jvmBasic.py: jvmBasic.g4 $(ANTLR)
	CLASSPATH=$(ANTLR):$(CLASSPATH) java org.antlr.v4.Tool -Dlanguage=Python3 -visitor $<

$(ANTLR):
	wget https://www.antlr.org/download/$(ANTLR)

clean:
	rm -f jvmBasic.interp jvmBasicLexer.interp jvmBasicLexer.py jvmBasicLexer.tokens jvmBasicListener.py jvmBasicVisitor.py jvmBasicParser.py jvmBasic.tokens

clobber: clean
	rm -f $(ANTLR)