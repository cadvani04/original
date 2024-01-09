#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "set.h"

set_t *set_new(void) {
    set_t *newset = malloc(sizeof(set_t)); //make a new set by allocating necessary memory for it
    if (newset != NULL) { //memory allocation failed
        newset->head = NULL;
    }
    return newset;
}

bool set_insert(set_t *set, const char *key, void *item) {
    if (item == NULL) { //if the item is ever null don't do shit
        return false; 
    }
    Node *iterator = set->head; //make an iterator
    while (iterator != NULL) { //if the iterator doesn't not exist
        if (strcmp(iterator->key, key) == 0) { //if the key already exists
            return false; 
        }
        iterator = iterator->next;//go to the next node
    }


    Node *newNode = malloc(sizeof(Node)); //allocate memory of node
    if (newNode == NULL) {//if its null
        return false; 
    }

    newNode->key = strdup(key); //make the node through the table
    newNode->item = item;
    newNode->next = set->head;
    set->head = newNode;

    return true; 
}


void *set_find(set_t *set, const char *key) { 
    if (set == NULL || key == NULL) {
        return NULL; // if there are any invalid arguments don't do anything
    }

    Node *current = set->head;
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            return current->item; //  if the key is found
        }
        current = current->next; //go to the next key
    }

    return NULL; // if the key is not found
}

void set_print(set_t *set, FILE *fp, void (*itemprint)(FILE *fp, const char *key, void *item)) {
    if (fp == NULL) { //if the fp is null
        return;
    }

    if (set == NULL) { //if my set doesn't exist
        fprintf(fp, "(null)\n"); //print to the file null
        return;
    }

    Node *current = set->head; //set the pointer at the head of the table
    while (current != NULL) {
        if (itemprint != NULL) {//print each item to file
            itemprint(fp, current->key, current->item);
        }
        current = current->next; //go to the next node
    }
}

void set_iterate(set_t *set, void *arg, void (*itemfunc)(void *arg, const char *key, void *item)) {
    if (set == NULL || itemfunc == NULL) { //make sure no invalid arguements
        return;
    }

    Node *current = set->head; //set up a pointer to the node at the head of the list
    while (current != NULL) {
        itemfunc(arg, current->key, current->item); //perform the funcion on the key, item
        current = current->next; //go to the next node
    }
}

void set_delete(set_t *set, void (*itemdelete)(void *item)) {
    if (set == NULL) { //go through the set
        return;
    }

    Node *current = set->head; //iterate through the nodes
    Node *next;

    while (current != NULL) {
        next = current->next;

        if (itemdelete != NULL) { //delet eh eitem
            itemdelete(current->item);
        }

        free(current->key); //free the key
        free(current); //free the item

        current = next;//go to the next
    }

    free(set);//free the memory allocated for key
}
