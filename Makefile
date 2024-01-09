CC = gcc
SOURCE = test_set.c set.c
CFLAGS = -Wall -Wextra -Wpedantic
OBJ = test_set.o set.o  
HEADER = set.h

TARGET = set

$(TARGET): ${OBJ} ${HEADER}
	$(CC) $(OBJ) -o $(TARGET)

%.o: %.c $(HEADER)
	$(CC) -c $< -o $@

clean:
	rm -rf $(TARGET)
	rm -rf *.o

