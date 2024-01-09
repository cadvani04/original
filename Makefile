CC = gcc
SOURCE = test_ll_cycle.c ll_cycle.c
CFLAGS = -Wall -Wextra -Wpedantic
OBJ = test_ll_cycle.o ll_cycle.o  
HEADER = ll_cycle.h

TARGET = check_cycle

$(TARGET): ${OBJ} ${HEADER}
	$(CC) $(OBJ) -o $(TARGET)

%.o: %.c $(HEADER)
	$(CC) -c $< -o $@

clean:
	rm -rf $(TARGET)
	rm -rf *.o

