#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include "lru.h"


/* Create a new (empty) lru; return NULL if error. */
lru_t *lru_new(const int capacity){ //same thing as hashtable
    if (capacity <= 0) {
        return NULL;
    }

    lru_t *ht = (lru_t *)malloc(sizeof(lru_t));
    if (ht == NULL) {
        return NULL;
    }

    ht->capacity = capacity;
    ht->table = (node_t **)calloc(capacity, sizeof(node_t *));
    if (ht->table == NULL) {
        free(ht);
        return NULL;
    }

    return ht;
}

/* Insert item, identified by key (string), into the given lru.
 * The key string is copied for use by the lru.
 * Return false if key exists in ht, any parameter is NULL, or error;
 * return true iff new item was inserted.
 */

bool lru_insert(lru_t *ht, const char *key, void *item) {
	if (ht == NULL || key == NULL || item == NULL) {
    	return false;
	}

	node_t *current = ht->table[0];//checking if the key is in the table
	while (current != NULL) {//while the node isn't at the last one
    	if (strcmp(current->key, key) == 0) { //if the key is equal to the new node then don't put it in
        	return false; // Key already exists
    	}
    	current = current->next;//go to the next node in the while loop
	}

	// Insert new node
	node_t *new_node = (node_t *)malloc(sizeof(node_t)); //allocate memory for new node
	if (new_node == NULL) { //]if the new node is false
    	return false; // Memory allocation error
	}

	new_node->key = strdup(key); // duplicate the key and make it the node name of the 'key'
	new_node->item = item; //make the item of the key 
	new_node->next = ht->table[0]; // Fix: Use ht->table[0] as the head of the linked list
	ht->table[0] = new_node; // Fix: Update ht->table[0] to point to the new node

	return true; // Insertion successful
}



/* Return the item associated with the given key;
 * return NULL if lru is NULL, key is NULL, key is not found.
 */
void *lru_find(lru_t *ht, const char *key){
            if (ht == NULL || key == NULL) {
        return NULL; //the any of the hashtable or key is null then nevermind
    }


    node_t *current = ht->table[0]; // start from the first part of the hastable
    while (current != NULL) { //if the node isn't null then keep going in the whil loop
        if (strcmp(current->key, key) == 0) {//compare and return if found
            return current->item;
        }
        current = current->next;
    }

    return NULL; // if the key not found, return null


}

/* Print the whole table; provide the output file and func to print each item.
 * Ignore if NULL fp. Print (null) if NULL ht.
 * Print a table with no items if NULL itemprint.
 */
void lru_print(lru_t *ht, FILE *fp, void (*itemprint)(FILE *fp, const char *key, void *item)){
        if (fp == NULL || ht == NULL || itemprint == NULL) { //if anything is null don't do anything
        return;
    }

    for (int i = 0; i < ht->capacity; ++i) {//until the capacity is reached by i keep going
        node_t *current = ht->table[i]; //iterate through please
        while (current != NULL) { //if the key has a value
            itemprint(fp, current->key, current->item); //print the item and key
            current = current->next; //go to the next
        }
    }

}

/* Iterate over all items in the table; in undefined order.
 * Call the given function on each item, with (arg, key, item).
 * If ht==NULL or itemfunc==NULL, do nothing.
 */
void lru_iterate(lru_t *ht, void *arg, void (*itemfunc)(void *arg, const char *key, void *item) ){
    if (ht == NULL || itemfunc == NULL) { //both ht and itemfunc checked to be not null
        return;
    }

    for (int i = 0; i < ht->capacity; ++i) { //until i reaches capacity
        node_t *current = ht->table[i];
        while (current != NULL) {
            itemfunc(arg, current->key, current->item); //use the function on the key, item
            current = current->next; //go to the next
        }
    }


}

/* Delete the whole lru; ignore NULL ht.   --*/


void lru_delete(lru_t *ht, void (*itemdelete)(void *item) ){
            if (ht == NULL) { //if the ht is null
        return;
    }

    for (int i = 0; i < ht->capacity; ++i) { //iterates through lru table
        node_t *current = ht->table[i]; // set the current node to the i-th item in the talbe of the lru
        while (current != NULL) {
            node_t *next = current->next;
            free(current->key);
            if (itemdelete != NULL) {
                itemdelete(current->item);
            }
            free(current); //free memory allocated
            current = next; //go to the next node
        }
    }

    free(ht->table);//free every memory allocated in the table
    free(ht); //free the pointer

}

