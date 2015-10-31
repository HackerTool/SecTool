OBJS=../commandLineParser.o  ../helper.o
READEROBJS=$(OBJS) communicationReader.o
CC=g++
CXXFLAGS= -g3 -ggdb
LDFLAGS= 
LDTESTFLAGS= $(LDFLAGS) -ldl -lcppunit
DEPEND= makedepend $(CFLAGS)

tnav: $(READEROBJS)
	$(CC) $(LDFLAGS) -o $@ $(READEROBJS)

all: unitTest communicationReader 

clean:
	-rm $(READEROBJS) communicationReader
