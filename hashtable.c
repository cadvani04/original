
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "hashtable.h"


// A good hash function to just start the hashing
unsigned int hash_function(const char *key) { //imported random hash function from hashtable 
    unsigned int hash = 0;
    while (*key) { //key exists
        hash = (hash * 3) + *key; //hash function to start the hashing 
        key++; //increment the key
    }
    return hash;//return hash to use in the slots
}


/* Create a new (empty) hashtable; return NULL if error. */
hashtable_t *hashtable_new(const int num_slots){
    if (num_slots <= 0) { //number of slots has to be more than one on inititalization
        return NULL; 
    }

    hashtable_t *ht = (hashtable_t *)malloc(sizeof(hashtable_t)); //allocate space for table of hashtable
    if (ht == NULL) { //if the allocation fails
        return NULL;
    }

    ht->num_slots = num_slots; // assign the number of slots to the table
    ht->table = (node_t **)calloc(num_slots, sizeof(node_t *)); //allocate memory for each node in the table for the amount of slots
    if (ht->table == NULL) { // if the table is not allocate(fails)
        free(ht);//free pointer
        return NULL;
    }

    return ht; //make the table
}

/* Insert item, identified by key (string), into the given hashtable.
 * The key string is copied for use by the hashtable.
 * Return false if key exists in ht, any parameter is NULL, or error;
 * return true iff new item was inserted.
 */
bool hashtable_insert(hashtable_t *ht, const char *key, void *item){
     if (ht == NULL || key == NULL || item == NULL) { //if anything is null then don't put it in the table
        return false;
    }

    unsigned int slot = hash_function(key) % ht->num_slots; //use the hash function

    // Check if key already exists through the interation through table
    node_t *current = ht->table[slot]; //use the slot, put it in the hashtable
    while (current != NULL) { //go through
        if (strcmp(current->key, key) == 0) {
            return false; // Key already exists
        }
        current = current->next;
    }

    // Insert new node
    node_t *new_node = (node_t *)malloc(sizeof(node_t)); //put int hte node
    if (new_node == NULL) {
        return false;
    }

    new_node->key = strdup(key);
    new_node->item = item;
    new_node->next = ht->table[slot];
    ht->table[slot] = new_node;

    return true;

}

/* Return the item associated with the given key;
 * return NULL if hashtable is NULL, key is NULL, key is not found.
 */
void *hashtable_find(hashtable_t *ht, const char *key){
        if (ht == NULL || key == NULL) {
        return NULL;
    }

    unsigned int slot = hash_function(key) % ht->num_slots;

    node_t *current = ht->table[slot];
    while (current != NULL) {
        if (strcmp(current->key, key) == 0) {
            return current->item;
        }
        current = current->next;
    }

    return NULL; // Key not found

}

/* Print the whole table; provide the output file and func to print each item.
 * Ignore if NULL fp. Print (null) if NULL ht.
 * Print a table with no items if NULL itemprint.
 */
void hashtable_print(hashtable_t *ht, FILE *fp, void (*itemprint)(FILE *fp, const char *key, void *item)){
        if (fp == NULL || ht == NULL || itemprint == NULL) {
        return;
    }

    for (int i = 0; i < ht->num_slots; ++i) {
        node_t *current = ht->table[i];
        while (current != NULL) {
            itemprint(fp, current->key, current->item);
            current = current->next;
        }
    }

}

/* Iterate over all items in the table; in undefined order.
 * Call the given function on each item, with (arg, key, item).
 * If ht==NULL or itemfunc==NULL, do nothing.
 */
void hashtable_iterate(hashtable_t *ht, void *arg, void (*itemfunc)(void *arg, const char *key, void *item) ){
        if (ht == NULL || itemfunc == NULL) { //check if the pointer or funciton is null 
        return;
    }

    for (int i = 0; i < ht->num_slots; ++i) { //iterate through the i in slots
        node_t *current = ht->table[i]; //go throught the table
        while (current != NULL) { //chec if null
            itemfunc(arg, current->key, current->item); //use the function of itemfunc
            current = current->next; //go to next node
        }
    }

}

/* Delete the whole hashtable; ignore NULL ht.
 * Provide a function that will delete each item (may be NULL).
 */
void hashtable_delete(hashtable_t *ht, void (*itemdelete)(void *item) ){
        if (ht == NULL) { // if the pointer to the array is null 
        return;
    }

    for (int i = 0; i < ht->num_slots; ++i) { //iterate through the table
        node_t *current = ht->table[i];
        while (current != NULL) {
            node_t *next = current->next;
            free(current->key); //free the key
            if (itemdelete != NULL) {//delete item
                itemdelete(current->item); 
            }
            free(current); //free the memory allocated
            current = next;
        }
    }

    free(ht->table); //free the table
    free(ht); //free the pointer
    
}

