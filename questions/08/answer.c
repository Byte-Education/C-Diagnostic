#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

struct user {
  char username[50];
  char password[50];
};

void createUser(struct user *user, char username[], char password[]){
  /*
  Your code goes here.
  */
}

bool login(struct user user, char username[], char password[]){
  /*
  Your code goes here.
  */
}

int main(void){
  struct user user;
  createUser(&user, "admin", "admin");
  if(login(user, "admin", "admin")){ 
    printf("login successful!\n");
  } else {
    printf("login failed!\n");
  }
  // If login failed, something is wrong with the code.
  return 0;
}