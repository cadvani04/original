#include <assert.h>
#include <string.h>

#include "password_checker.h"

bool check_range(char letter, char lower, char upper) {
bool is_in_range = (letter >= lower && letter <= upper); //made it either less than or equal to or more than or equal to the char range
return is_in_range;

}


bool check_length(const char *password) {
    int length = strlen(password);
    bool z;
    if (length>=10){    //remade the range function to count if the length is actually 10 or more into a boolean which is the correct data type
    z =true;
    }
    else{ 
    z =false;
    }
    bool meets_len_req = z;
    return meets_len_req;
}


bool check_upper(const char *password) {
    while (*password != '\0') {
        bool is_in_range = check_range(*password, 'A', 'Z');
        if (is_in_range) {
            return true;
        }
        ++password;
    }
    return false;
}


bool check_lower(const char *password) {
    while (*password != '\0') {
        bool is_in_range = check_range(*password, 'a', 'z');
        if (is_in_range) {
            return true;
        }
        ++password;
    }
    return false;
}




bool check_number(const char *password) {
    while (*password != '\0') {     //two problems with this one, there was an infinite loop and also there was a pointer going way higher
        if (check_range(*password, '0', '9')) {
            return true;
        }
        ++password;
    }
    return false;
}


bool check_name(const char *first_name, const char *last_name, const char *password) {
    const char *first = strstr(password, first_name);
    const char *last = strstr(password, last_name);
    return (!first && !last);
}


bool check_password(const char *first_name, const char *last_name, const char *password) {
    bool length, upper, lower, number, name;
    lower = check_lower(password);
   
    length = check_length(password);
   
    name = check_name(first_name, last_name, password);
 
    number = check_number(password);
 
    upper = check_upper(password);
    return (lower && length && name && upper && number);
}
