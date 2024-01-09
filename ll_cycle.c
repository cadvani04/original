#include <stddef.h>
#include <stdio.h>
#include "ll_cycle.h"

int ll_has_cycle(node *head) {
    node *fst_ptr = head; //initialize the fast ptr
    node *slw_ptr = head; //initialize the slow ptr

    if (head == NULL || head->next == NULL) { //if the head itself isn't null or the next node of the list isn't null
        return 0; //there can't be a cycle
    }

    while (fst_ptr != NULL && fst_ptr->next != NULL) { //if the fast ptr isn't null or the next node isn't null then keep going(step2)
        printf("fst_ptr: %p, slw_ptr: %p\n", (void*)fst_ptr, (void*)slw_ptr); //for debugging
        fst_ptr = fst_ptr->next->next; //+2
        slw_ptr = slw_ptr->next; //+1
        if (slw_ptr == fst_ptr) { 
            return 1; //cycle found!
        }
    }

    return 0; //nocycle
}
