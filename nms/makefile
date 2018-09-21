run : nms.o main.o
	g++ nms.o main.o -o run
main.o: main.cpp
	g++ -c main.cpp
nms.o: nms.cpp
	g++ -c nms.cpp
clean:
	rm run *.o